import glob
import json
import csv

def index_fulltext(es_client, path, index):
    print("adding full-text index...")
    for file in glob.glob(path):
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

        es_client.index(index=index,
                       doc_type='papers',
                       id=doc['paper_id'],
                       body=b)
    return

def index_authorsfromMD(es_client, filepath, index):
    all_authors = {}
    with open(filepath, newline='') as csvfile:
        f = csv.DictReader(csvfile)
        print("csv opened")
        for row in f:
            if row['has_full_text']=='True':
                print("found file")
                authors = row['authors'].split(";")
                for a_name in authors:
                    if a_name not in all_authors:
                        b={}
                        b['author_name'] = a_name
                        b['paper_ids'] = [row['sha']]
                        all_authors[a_name] = b
                    else:
                        all_authors[a_name]['paper_ids'].append(row['sha'])
    i=0            
    for author in all_authors.keys():
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
