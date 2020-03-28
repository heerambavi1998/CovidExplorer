import glob
import json

def index_fulltext_search(es_client, path, index):

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

        res = es_client.index(index=index,
                       doc_type='papers',
                       id=doc['paper_id'],
                       body=b)
    return
