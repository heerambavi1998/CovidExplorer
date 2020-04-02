import glob
import json
import csv
from datetime import datetime

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
            if row['sha'] != '':
                for sha in _format_sha(row['sha']):
                    metadata_dict[sha] = row

    named_ent_dict = {}
    with open('prge_from_abs_comb.csv', newline='') as csvfile:
        f = csv.reader(csvfile)
        for row in f:
            named_ent_dict[row[0]] = row[1]

    i = 0
    for path in paths:
        for file in glob.glob(path):
            i+=1
            doc = json.load(open(file, 'r'))
            b = {}
            b['paper_id'] = doc['paper_id']
            b['title'] = doc["metadata"]["title"]

            abst = ""
            for para in doc['abstract']:
                abst += para['text']
                abst += '\n'
            b['abstract'] = abst

            body = ""
            for para in doc['body_text']:
                body += para['text']
                body += '\n'
            b['body_text'] = body

            # adding metadata
            metadata = metadata_dict[doc['paper_id']]
            b['doi'] = metadata['doi']
            b['url'] = metadata['url']
            b['publish_time'] = metadata['publish_time']
            b['journal'] = metadata['journal']
            b['authors'] = metadata['authors']
            b['named_entities'] = _format_sha(named_ent_dict[doc['paper_id']])
            es_client.index(index=index,
                           id=i,
                           body=b)
    return

def index_authorsfromMD(es_client, filepath, index):
    print("adding author index...")

    all_authors = {}
    with open(filepath, newline='') as csvfile:
        f = csv.DictReader(csvfile)
        #print("csv opened")
        for row in f:
            if row['has_full_text']=='True':
                #print("found file")
                authors = row['authors'].split(";")
                for a_name in authors:
                    if a_name not in all_authors:
                        b={}
                        b['author_name'] = a_name
                        b['paper_ids'] = _format_sha(row['sha'])
                        all_authors[a_name] = b
                    else:
                        all_authors[a_name]['paper_ids'].extend(_format_sha(row['sha']))
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


def index_named_entities(es_client, path, index):
    print("adding Named Entity index...")

    named_ent_dict = {}
    with open(path, newline='') as csvfile:
        f = csv.reader(csvfile)
        for row in f:
            if row[1] == '':
                continue
            nes = row[1].split(';')
            for ne in nes:
                if ne in named_ent_dict:
                    named_ent_dict[ne].append(row[0])
                else:
                    named_ent_dict[ne] = [row[0]]

    i = 0
    for item in named_ent_dict:
        i = i + 1
        b = {}
        b['entity'] = item
        b['pids'] = named_ent_dict[item]
        b['doc_freq'] = len(named_ent_dict[item])

        es_client.index(index=index, id=i, body=b)

    return


def _format_sha(sha):
    l = sha.split(';')
    l_1 = [i.strip() for i in l]
    return l_1