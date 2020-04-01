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
                    "fuzziness": 2
                }
                }
            }
        })
    papers=[]
    try:
        for i in range(len(res['hits']['hits'])):
            ptitle=res['hits']['hits'][i]['_source']['title']
            url = res['hits']['hits'][i]['_source']['url']
            ptime = res['hits']['hits'][i]['_source']['publish_time']
            journ = res['hits']['hits'][i]['_source']['journal']
            papers.append((ptitle, url, journ, ptime))
    except:
        None
    return papers

def paper_filteryr(paper_name,yr_s,yr_e):
    res = es.search(index="covid19_fulltext", body={
        "from":0,
        "size":50,
        "query":{
            "bool":{
                "must":[{
                    "range":{
                        "publish_time":{
                            "lte": yr_e,
                            "gte": yr_s
                        }
                    }
                },
                {
                    "match":{
                        "title":{
                            "query": paper_name,
                            "fuzziness":2
                        }
                    }
                }]
            }
        }
    })

    papers=[]
    try:
        for i in range(len(res['hits']['hits'])):
            ptitle=res['hits']['hits'][i]['_source']['title']
            url = res['hits']['hits'][i]['_source']['url']
            ptime = res['hits']['hits'][i]['_source']['publish_time']
            journ = res['hits']['hits'][i]['_source']['journal']
            papers.append((ptitle, url, journ, ptime))
    except:
        None
    return papers

def author_es(author):
    res = es.search(index="covid19_authors",body={
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
    res = es.search(index="covid19_authors",body={
        "query":{
            "match_phrase":{
                "author_name":author
            }
        }
    })
    papers = res['hits']['hits'][0]['_source']['paper_ids']
    return papers

def paper_namefromid(pid):
    res = es.search(index="covid19_fulltext", body={
        'from':0,
        'size':10000,
        "query": {
            "match_phrase": {
                "paper_id": pid
            }
        }
    })
    try:
        #print(res)
        r = (res['hits']['hits'][0]['_source']['title'],
             res['hits']['hits'][0]['_source']['url'],
             res['hits']['hits'][0]['_source']['journal'],
             res['hits']['hits'][0]['_source']['publish_time'])
    except:
        r = None
    return r


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
    res = es.search(index='covid19_fulltext', body={
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
            url = res['hits']['hits'][i]['_source']['url']
            ptime = res['hits']['hits'][i]['_source']['publish_time']
            journ = res['hits']['hits'][i]['_source']['journal']
            papers.append((ptitle,url,journ,ptime))
    except:
        None
    return papers

def fulltextsearch_filteryr(search_item, yr_s, yr_e):
    res = es.search(index="covid19_fulltext", body={
        'from':0,
        'size':50,
        'query':{
            'bool':{
                'must':[
                    {
                        'range':{
                            'publish_time':{
                                'lte':yr_e,
                                'gte':yr_s
                            }
                        }
                    },
                    {
                        'multi_match': {
                            'query': search_item,
                            'fields': ['title', 'abstract', 'body_text'],
                            'fuzziness': 2
                        }
                    }
                ]
            }
        }
    })
    papers=[]
    try:
        for i in range(len(res['hits']['hits'])):
            ptitle=res['hits']['hits'][i]['_source']['title']
            url = res['hits']['hits'][i]['_source']['url']
            ptime = res['hits']['hits'][i]['_source']['publish_time']
            journ = res['hits']['hits'][i]['_source']['journal']
            papers.append((ptitle,url,journ,ptime))
    except:
        None
    return papers
