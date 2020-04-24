import networkx as nx
from operator import itemgetter
from collections import OrderedDict
from . import ES_CLIENT as es
from .helper import get_ent_type_name

def _get_comentions_by_ent_type(gene, ent_type=None):
    # gets comentions for the entity by each pid where entity is
    # present which are of type ent_type
    res = es.search(index='covid19_ner', body={
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
        nes = res['hits']['hits'][0]['_source']['named_entities'][ent_type]
        co_men = [x for x in nes if x != gene]
        co_ment[pid] = (res['hits']['hits'][0]['_source']['title'], co_men)
    return co_ment

def _get_comentions(gene, max=None):
    # gets all comentions with their occurance numbers for the entity by each entity type.
    # returns { ent_type : {ent:occ_no} }
    # returns the dictionary sorted in descending order by occurance number.
    # max is the maximum entities returned for each entity type
    res = es.search(index='covid19_ner', body={
        'from': 0,
        'size': 10,
        "query": {
            "match_phrase": {
                "entity": gene
            }
        }
    })
    pid_list = res['hits']['hits'][0]['_source']['pids']
    co_ment = {'ner_ched':{},'ner_dna':{},'ner_rna':{},
               'ner_protein':{},'ner_cell_line':{},'ner_cell_type':{}}
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
        nes = res['hits']['hits'][0]['_source']['named_entities']
        for type in nes:
            for ne in nes[type]:
                if ne == gene:
                    continue
                try:
                    co_ment[type][ne] += 1
                except:
                    co_ment[type][ne] = 1
            if max:
                if len(co_ment[type]) > max:
                    l = sorted(co_ment[type].items(), key=itemgetter(1), reverse=True)[:max]
                else:
                    l = sorted(co_ment[type].items(), key=itemgetter(1), reverse=True)
            else:
                l = sorted(co_ment[type].items(), key=itemgetter(1), reverse=True)
            co_ment[type] = OrderedDict(l)

    return co_ment

def create_network(gene, ent_type):
    """
    create network using networkx for an entity and its co-mentions.
    each comention is connected to the entity. Each comention from the same paper are connected to each other.
    comentions in same paper have same color.
    :param gene: string (entity name)
    :param ent_type: string (entity type)
    :return: Graph object (for network)
    """
    co_ment = _get_comentions_by_ent_type(gene, ent_type)
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


def create_sanky(gene):

    # getting top 10 genes only
    co_ment = _get_comentions(gene, 10)

    #labled dict for mapping from a gene to its int label
    label_dict = {gene:0}
    source = []
    target = []
    value = []
    c = 1
    for type in co_ment:
        type_name = get_ent_type_name(type)
        label_dict[type_name] = c
        c+=1

        tot_val = 0
        # add flow from entity_type node to each entity
        for ne in co_ment[type]:
            label_dict[ne] = c
            c+=1
            source.append(label_dict[type_name])
            target.append(label_dict[ne])
            value.append(co_ment[type][ne])
            tot_val += co_ment[type][ne]

        # add flow from search gene to entity type
        source.append(label_dict[gene])
        target.append(label_dict[type_name])
        value.append(tot_val)

    d = {'label':list(label_dict.keys()),
         'source': source,
         'target': target,
         'value': value}
    return d