from elasticsearch import Elasticsearch
from pymongo import MongoClient
from . import ES_CLIENT as es

def paper_es(paper_name):
    res =es.search(index="covid19_fulltext",body={
        "from":0,
        "size":100,
        "query":{
            "match":{
                "title":{
                    "query": paper_name,
                    "fuzziness": 50
                }
                }
            }
        })
    papers=[]
    try:
        for i in range(len(res['hits']['hits'])):
            ptitle=res['hits']['hits'][i]['_source']['title']
            papers.append(ptitle)
    except:
        None
    return papers

def author_es(author):
    res = es.search(index="covid19_authorz",body={
        "from":0,
        "size":50,
        "query":{
            "match":{
                "author_name":{
                    "query":author,
                    "fuzziness": 2
                }
                }}})
    authors=[]
    try:
        for i in range(len(res['hits']['hits'])):
            aname = res['hits']['hits'][i]['_source']['author_name']
            # aid = res['hits']['hits'][i]['_source']['id']
            authors.append(aname)
    except:
        None
    return authors

def author_findpapers(author):
    # print("1")
    res = es.search(index="covid19_authorz",body={
        "query":{
            "match_phrase":{
                "author_name":author
            }
        }
    })
    papers = res['hits']['hits'][0]['_source']['paper_ids']
    return papers

def paper_namefromid(pid):
    res = es.get(index="covid19_fulltext", id=pid, doc_type="papers")
    return res['_source']['title']

# def conf_es(conf_name):
#     es=Elasticsearch(port=9210)
#     res =es.search(index="newacl",body={"from":0, "size":100,"query":{"match":{"venue_name":conf_name}}})
#     confs=[]
#     try:
#         for i in range(len(res['hits']['hits'])):
#             confs.append([res['hits']['hits'][i]['_source']['venue_name'],res['hits']['hits'][i]['_source']['year']])
#     except:
#         None
#     if len(confs)==0:
#         res =es.search(index="newacl",body={"from":0, "size":100,"query":{"query_string":{"default_field" : "venue_name", "query" : "*"+conf_name+"*"}}})
#         confs=[]
#         try:
#             for i in range(len(res['hits']['hits'])):
#                 confs.append([res['hits']['hits'][i]['_source']['venue_name'],res['hits']['hits'][i]['_source']['year']])
#         except:
#             None

#     return confs


def fulltextsearch(search_item):
    res = es.search(index='covid19_fulltext', doc_type='papers', body={
        'from': 0,
        'size': 50,
        'query': {
            'multi_match': {
                'query': search_item,
                'fields': ['title', 'abstract', 'body_text'],
                'fuzziness': 2
            }
        }
    })
    papers=[]
    try:
        for i in range(len(res['hits']['hits'])):
            ptitle=res['hits']['hits'][i]['_source']['title']
            # x=list(db.new_papers.find({'_id':pid},{'paper_title':1,'_id':0}))
            # papers.append([res['hits']['hits'][i]['_source']['id'],x[0]['paper_title']])
            papers.append(ptitle)
    except:
        None
    return papers
