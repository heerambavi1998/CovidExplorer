from . import ES_CLIENT as es
from collections import OrderedDict
from operator import itemgetter

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
    pids = []
    try:
        for i in range(len(res['hits']['hits'])):
            papers.append({'title': res['hits']['hits'][i]['_source']['title'],
            'url': res['hits']['hits'][i]['_source']['url'],
            'ptime' : res['hits']['hits'][i]['_source']['publish_time'],
            'journ' : res['hits']['hits'][i]['_source']['journal'],
            'auth' : res['hits']['hits'][i]['_source']['authors'],
            'ner': res['hits']['hits'][i]['_source']['named_entities'] })
            pids.append(res['hits']['hits'][i]['_source']['paper_id'])
    except:
        None
    return papers,pids

def paper_filteryr(paper_name,yr_s,yr_e):
    res = es.search(index="covid19_fulltext", body={
        "from":0,
        "size":100,
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
    pids = []
    try:
        for i in range(len(res['hits']['hits'])):
            papers.append({'title': res['hits']['hits'][i]['_source']['title'],
                           'url': res['hits']['hits'][i]['_source']['url'],
                           'ptime': res['hits']['hits'][i]['_source']['publish_time'],
                           'journ': res['hits']['hits'][i]['_source']['journal'],
                           'auth': res['hits']['hits'][i]['_source']['authors'],
                           'ner': res['hits']['hits'][i]['_source']['named_entities']})
            pids.append(res['hits']['hits'][i]['_source']['paper_id'])
    except:
        None
    return papers,pids


def author_es(author):
    res = es.search(index="covid19_authors",body={
        "from":0,
        "size":100,
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
        
        r = {'title': res['hits']['hits'][0]['_source']['title'],
             'url' : res['hits']['hits'][0]['_source']['url'],
             'journ': res['hits']['hits'][0]['_source']['journal'],
             'ptime': res['hits']['hits'][0]['_source']['publish_time'],
             'ner': res['hits']['hits'][0]['_source']['named_entities'],
             'auth': res['hits']['hits'][0]['_source']['authors']}
    except:
        r = None
        print(res)
    return r


def fulltextsearch(search_item):
    res = es.search(index='covid19_fulltext', body={
        'from': 0,
        'size': 100,
        'query': {
            'multi_match': {
                'query': search_item,
                'fields': ['title', 'abstract', 'body_text'],
                'fuzziness': 2
            }
        }
    })
    papers=[]
    pids = []
    try:
        for i in range(len(res['hits']['hits'])):
            papers.append({'title': res['hits']['hits'][i]['_source']['title'],
                           'url': res['hits']['hits'][i]['_source']['url'],
                           'ptime': res['hits']['hits'][i]['_source']['publish_time'],
                           'journ': res['hits']['hits'][i]['_source']['journal'],
                           'auth': res['hits']['hits'][i]['_source']['authors'],
                           'ner': res['hits']['hits'][i]['_source']['named_entities']})
            pids.append(res['hits']['hits'][i]['_source']['paper_id'])
    except:
        None
    return papers,pids

def fulltextsearch_filteryr(search_item, yr_s, yr_e):
    res = es.search(index="covid19_fulltext", body={
        'from':0,
        'size':100,
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
    pids = []
    try:
        for i in range(len(res['hits']['hits'])):
            papers.append({'title': res['hits']['hits'][i]['_source']['title'],
                           'url': res['hits']['hits'][i]['_source']['url'],
                           'ptime': res['hits']['hits'][i]['_source']['publish_time'],
                           'journ': res['hits']['hits'][i]['_source']['journal'],
                           'auth': res['hits']['hits'][i]['_source']['authors'],
                           'ner': res['hits']['hits'][i]['_source']['named_entities']})
            pids.append(res['hits']['hits'][i]['_source']['paper_id'])
    except:
        None
    return (papers, pids)


def top_doc_freq_ne(entity_list, n):
    entity_dict = {}
    for entity in entity_list:
        res = es.search(index="covid19_ner", body={
            'from': 0,
            'size': 10000,
            "query": {
                "match_phrase": {
                    "entity": entity
                }
            }
        })
        entity_dict[entity] = res['hits']['hits'][0]['_source']['doc_freq']
    if len(entity_list) <= n:
        return entity_dict
    else:
        d = OrderedDict(sorted(entity_dict.items(), key=itemgetter(1))[:n])
        return d

def named_entities_es(pid_list):

    ne_list = {'prge':[], 'ched':[]}
    for pid in pid_list:
        res = es.search(index="covid19_fulltext", body={
            'from': 0,
            'size': 10000,
            "query": {
                "match_phrase": {
                    "paper_id": pid
                }
            }
        })
        ne_list['prge'].extend(res['hits']['hits'][0]['_source']['named_entities'])
        ne_list['ched'].extend(res['hits']['hits'][0]['_source']['ched_entities'])
    ne_list['prge'] = list(set(ne_list['prge']))
    ne_list['ched'] = list(set(ne_list['ched']))
    # TODO: currently not returning top genes, but all genes
    #top_ne = top_doc_freq_ne(ne_list,16)
    return ne_list


def named_entity_filter(pid_list, entity, entity_type):
    index = 'covid19_ner'
    res = es.search(index=index, body={
        'from': 0,
        'size': 10000,
        "query": {
            "match_phrase": {
                "entity": entity
            }
        }
    })
    pids = res['hits']['hits'][0]['_source']['pids']

    l = []
    for id in pids:
        if id in pid_list:
            l.append(id)
    return l

def get_named_entity_info(entity, entity_type):
    index = 'covid19_ner'    
    res = es.search(index=index, body={
        'from':0,
        'size':100,
        "query": {
            "match_phrase": {
                "entity": entity
            }
        }
    })
    try:
        # print(res)
        r = (res['hits']['hits'][0]['_source']['entity'],
             res['hits']['hits'][0]['_source']['pids'],
             res['hits']['hits'][0]['_source']['doc_freq'],
             res['hits']['hits'][0]['_source']['first_mention'],
             res['hits']['hits'][0]['_source']['co_mentions'])
    except:
        r = None
    return r

