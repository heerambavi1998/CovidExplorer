from elasticsearch import Elasticsearch
from pymongo import MongoClient
from . import ES_CLIENT as es

def paper_es(paper_name):
    res =es.search(index="newacl",body={"from":0, "size":100,"query":{"match":{"ocr_title":paper_name}}})
    papers=[]
    try:
        for i in range(len(res['hits']['hits'])):
            papers.append([res['hits']['hits'][i]['_source']['id'],res['hits']['hits'][i]['_source']['paper_title']])
    except:
        None
    if len(papers)==0:
        res =es.search(index="newacl",body={"from":0, "size":100,"query":{"query_string":{"default_field" : "ocr_title", "query" : "*"+paper_name+"*"}}})
        try:
            for i in range(len(res['hits']['hits'])):
                papers.append([res['hits']['hits'][i]['_source']['id'],res['hits']['hits'][i]['_source']['paper_title']])
        except:
            None
    return papers

def author_es(author):
    res = es.search(index="acl_author",body={"from":0, "size":100,"query":{"match":{"id":author}}})
    authors=[]
    try:
        for i in range(len(res['hits']['hits'])):
            authors.append([res['hits']['hits'][i]['_source']['id'],res['hits']['hits'][i]['_source']['id'].replace("-"," ")])
    except:
        pass
    if len(authors)==0:
        res =es.search(index="acl_author",body={"from":0, "size":100,"query":{"query_string":{"default_field" : "id", "query" : "*"+author+"*"}}})
        try:
            for i in range(len(res['hits']['hits'])):
                authors.append([res['hits']['hits'][i]['_source']['id'],res['hits']['hits'][i]['_source']['id'].replace("-"," ")])
        except:
            pass
    return authors

def conf_es(conf_name):
    es=Elasticsearch(port=9210)
    res =es.search(index="newacl",body={"from":0, "size":100,"query":{"match":{"venue_name":conf_name}}})
    confs=[]
    try:
        for i in range(len(res['hits']['hits'])):
            confs.append([res['hits']['hits'][i]['_source']['venue_name'],res['hits']['hits'][i]['_source']['year']])
    except:
        None
    if len(confs)==0:
        res =es.search(index="newacl",body={"from":0, "size":100,"query":{"query_string":{"default_field" : "venue_name", "query" : "*"+conf_name+"*"}}})
        confs=[]
        try:
            for i in range(len(res['hits']['hits'])):
                confs.append([res['hits']['hits'][i]['_source']['venue_name'],res['hits']['hits'][i]['_source']['year']])
        except:
            None

    return confs


def fulltextsearch(search_item):
    res = es.search(index='test', doc_type='papers', body={
        'query': {
            'bool': {
                'should': [{
                    'match_phrase': {
                        "abstract": search_item
                    }
                }, {
                    'match_phrase': {
                        "body_text": search_item
                    }
                }]
            }
        }
    })
    papers=[]
    try:
        for i in range(len(res['hits']['hits'])):
            pid=res['hits']['hits'][i]['_source']['paper_id']
            # x=list(db.new_papers.find({'_id':pid},{'paper_title':1,'_id':0}))
            # papers.append([res['hits']['hits'][i]['_source']['id'],x[0]['paper_title']])
            papers.append(pid)
    except:
        None
    return papers
