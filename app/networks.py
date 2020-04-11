from .config import *
from . import ES_CLIENT as es
import networkx as nx

def _get_comentions(gene, ent_type):
    if ent_type == 'prge':
        index = 'covid19_ner'
        ent = 'named_entities'
    elif ent_type == 'ched':
        index = 'covid19_ched'
        ent = 'ched_entities'
    res = es.search(index=index, body={
        'from': 0,
        'size': 10,
        "query": {
            "match_phrase": {
                "entity": gene
            }
        }
    })
    pid_list = res['hits']['hits'][0]['_source']['pids']
    co_ment = {}
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
        nes = res['hits']['hits'][0]['_source'][ent]
        co_men = [x for x in nes if x != gene]
        co_ment[pid] = (res['hits']['hits'][0]['_source']['title'], co_men)
    return co_ment


def create_network(gene, ent_type):
    co_ment = _get_comentions(gene, ent_type)
    graph = nx.Graph()

    graph.add_node(gene)
    communities = {gene:0}
    i = 0
    for item in co_ment:
        i+=1
        for ne in co_ment[item][1]:
            graph.add_node(ne)
            graph.add_edge(gene, ne)
            communities[ne] = i
            for ne2 in co_ment[item][1]:
                if ne==ne2:
                    continue
                graph.add_node(ne2)

                communities[ne] = i
                communities[ne2] = i
                graph.add_edge(ne, ne2)
    nx.set_node_attributes(graph, name='community', values=communities)
    return graph