import glob
import json
import csv
from datetime import datetime
from .elasticSearch import paper_namefromid

def index_fulltext(es_client, metadatapath, paths, index):
    print("creating full-text index mapping...")
    mapping = json.load(open('app/static/json/es_fulltext_mapping.json','r'))
    response = es_client.indices.create(
        index=index,
        body=mapping,
        ignore=400  # ignore 400 already exists code
    )
    if 'acknowledged' in response:
        if response['acknowledged'] == True:
            print("INDEX MAPPING SUCCESS FOR INDEX:", response['index'])
    # catch API error response
    elif 'error' in response:
        print("ERROR:", response['error']['root_cause'])
        print("TYPE:", response['error']['type'])

    print("adding full-text index...")
    
    metadata_dict = {}
    with open(metadatapath, newline='') as csvfile:
        f = csv.DictReader(csvfile)
        for row in f:
            if row['full_text_file']=='custom_license' or row['full_text_file']=='comm_use_subset' or row['full_text_file']=='noncomm_use_subset' or row['full_text_file']=='biorxiv_medrxiv':
                if row['sha'] != '' and row['has_pdf_parse'] == 'True':
                    for sha in _format_sha(row['sha']):
                        metadata_dict[sha] = row
                elif row['pmcid'] != "" and row['has_pmc_xml_parse'] == 'True':
                    for pmc in _format_sha(row['pmcid']):
                        metadata_dict[pmc] = row
    _, named_entity_dict = _ner_filter()
    i = 0
    sha_tillnow={}
    for path in paths:
        print("indexing path %s" %path)

        for file in glob.glob(path):
            doc = json.load(open(file, 'r'))
            
            if doc['paper_id'] in sha_tillnow:
                continue

            try:
                # find the paper in metadatadict
                metadata = metadata_dict[doc['paper_id']]
            except:
                # error due to missing paper ID in metadatadict
                # paper already accounted for via different format
                continue
            i += 1
            # start building index doc
            b = {}
            b['paper_id'] = doc['paper_id']
            sha_tillnow[doc['paper_id']] = 1
            b['title'] = doc["metadata"]["title"]

            # abst = ""
            # for para in doc['abstract']:
            #     abst += para['text']
            #     abst += '\n'
            # b['abstract'] = abst

            body = ""
            for para in doc['body_text']:
                body += para['text']
                body += '\n'
            b['body_text'] = body

            # adding metadata to doc
            b['abstract'] = metadata['abstract']
            b['doi'] = metadata['doi']
            b['url'] = metadata['url']
            b['publish_time'] = metadata['publish_time']
            b['journal'] = metadata['journal']
            b['authors'] = _format_sha(metadata['authors'])

            # adding named entities
            b['named_entities'] = named_entity_dict[doc['paper_id']]

            res = es_client.index(index=index,
                        id=i,
                        body=b)
            #print(res)
    return

def index_authorsfromMD(es_client, filepath, index):
    print("adding author index...")

    all_authors = {}
    with open(filepath, newline='') as csvfile:
        f = csv.DictReader(csvfile)
        #print("csv opened")
        for row in f:
            if row['full_text_file']=='custom_license' or row['full_text_file']=='comm_use_subset' or row['full_text_file']=='noncomm_use_subset' or row['full_text_file']=='biorxiv_medrxiv':
                #print("found file")
                authors = row['authors'].split(";")
                for a_name in authors:
                    if a_name not in all_authors:
                        b={}
                        b['author_name'] = a_name
                        if row['sha'] != "":
                            b['paper_ids'] = _format_sha(row['sha'])
                        elif row['pmcid'] != "":
                            b['paper_ids'] = _format_sha(row['pmcid'])
                        else:
                            b['paper_ids'] = []
                        all_authors[a_name] = b
                    else:
                        if row['sha'] != "":
                            all_authors[a_name]['paper_ids'].extend(_format_sha(row['sha']))
                        elif row['pmcid'] != "":
                            all_authors[a_name]['paper_ids'].extend(_format_sha(row['pmcid']))
                        else:
                            continue
    i=0
    for author in all_authors:
        i+=1
        b = all_authors[author]
        es_client.index(index=index,
                        id=i,
                        doc_type='authors',
                        body=b)
    return
                    

def index_authors(es_client, paths, index):
    
    all_authors = {}
    for path in paths:
        print("adding author index...")
        for file in glob.glob(path):
            doc = json.load(open(file, 'r'))

            for author in doc["metadata"]["authors"]:
                a_name = author["first"]
                for m in author["middle"]:
                    a_name += " " + m 
                a_name += " " + author["last"]
                if a_name not in all_authors:
                    b = {}
                    b['author_name'] = a_name
                    b['paper_ids'] = [doc['paper_id']]
                    all_authors[a_name] = b
                else:
                    all_authors[a_name]['paper_ids'].append(doc['paper_id'])
    i=0            
    for author in all_authors.keys():
        i+=1
        b = all_authors[author]        
        es_client.index(index=index,
                        id=i,
                        doc_type='authors',
                        body=b)
    return


def index_named_entities(es_client, index):
    print("adding Named Entity index...")

    named_ent_dict, _ = _ner_filter()
    i = 0
    for item in named_ent_dict:
        i = i + 1
        b = {}
        b['entity'] = item
        b['pids'] = named_ent_dict[item]['pids']
        b['type'] = named_ent_dict[item]['type']
        y_min = datetime.now().date()
        #first_p = ''
        for pid in b['pids']:
            p = paper_namefromid(pid)
            # print(p['ptime'])
            try:
                y = datetime.strptime(p['ptime'], '%Y-%m-%d').date()
            except:
                try:
                    y = datetime.strptime(p['ptime'], '%Y').date()
                except:
                    continue
            if y <= y_min:
                y_min = y
                first_p = pid
        b['doc_freq'] = len(b['pids'])
        b['first_mention'] = first_p
        b['co_mentions'] = named_ent_dict[item]['comen']
        es_client.index(index=index, id=i, body=b)

    return


def _format_sha(sha):
    l = sha.split(';')
    l_1 = [i.strip() for i in l]
    return l_1

def _format_ne(ne):
    l = ne.split(';')
    l_1 = [i.strip() for i in l if len(i)>1]
    return l_1



def _ner_filter():
    """
    filters the NERs from csvs
    :return: (map of ner to sha, map of sha to ner)
    """
    print("creating dicts from csvs...")
    sha_to_ent_dict = {}
    ent_to_sha_dict = {}

    mapp = {0: 'ner_ched', 1: 'ner_dna', 2: 'ner_rna', 3: 'ner_protein', 4: 'ner_cell_line', 5: 'ner_cell_type'}

    # scibert entities
    # first finding the entity type for each entity
    # ched entities have not been included as it is possible that other entities maybe a subset
    # of ched entities. Hence any entity which is of type ched and Xyz is assigned type Xyz.
    ent_type_dict = {}
    with open('ners.csv', newline='') as csvfile:
        f = csv.reader(csvfile)
        for row in f:
            for i in range(1, 6):
                nes = _format_ne(row[i])
                for ne in nes:
                    if ne in ent_type_dict:
                        ent_type_dict[ne].append(i)
                    else:
                        ent_type_dict[ne] = [i]
                #ched entities
            nes = _format_ne(row[6])
            for ne in nes:
                if ne not in ent_type_dict:
                    ent_type_dict[ne] = [0]

    for ne in ent_type_dict:
        mode = max(ent_type_dict[ne], key=ent_type_dict[ne].count)
        ent_type_dict[ne] = mapp[mode]

    with open('ners.csv', newline='') as csvfile:
        f = csv.reader(csvfile)
        for row in f:
            if row[0] not in sha_to_ent_dict:
                sha_to_ent_dict[row[0]] = {'ner_ched':[],
                                          'ner_dna':[],
                                          'ner_rna':[],
                                          'ner_protein':[],
                                          'ner_cell_line':[],
                                          'ner_cell_type':[]}
            nes = {}
            for i in range(1,7):
                if row[i] == '':
                    continue   
                nes[mapp[i-1]] = _format_ne(row[i])
            #print(nes)
            for t in nes:
                other_comen = nes.copy()
                other_comen.pop(t) 
                for ne in nes[t]:
                    try:
                        typ = ent_type_dict[ne]
                    except:
                        #print(ne, t)
                        break

                    sha_to_ent_dict[row[0]][typ].append(ne)

                    co_men = [x for x in nes[t] if x != ne]  # all nes except current ne
                    if ne in ent_to_sha_dict:
                        ent_to_sha_dict[ne]['pids'].append(row[0])
                    else:
                        ent_to_sha_dict[ne] = {}
                        ent_to_sha_dict[ne]['pids'] = [row[0]]
                        ent_to_sha_dict[ne]['comen'] = {'ner_ched':[],
                                                        'ner_dna':[],
                                                        'ner_rna':[],
                                                        'ner_protein':[],
                                                        'ner_cell_line':[],
                                                        'ner_cell_type':[]}
                        ent_to_sha_dict[ne]['type'] = typ
                    ent_to_sha_dict[ne]['comen'][typ].extend(co_men)
                    for tt in other_comen:
                        ent_to_sha_dict[ne]['comen'][tt].extend(other_comen[tt])

    #changing sets to list
    for ne in ent_to_sha_dict:
        for j in ent_to_sha_dict[ne]['comen']:
            ent_to_sha_dict[ne]['comen'][j] = list(set(ent_to_sha_dict[ne]['comen'][j]))

    print("creating dicts from csvs...DONE")
    return ent_to_sha_dict, sha_to_ent_dict



