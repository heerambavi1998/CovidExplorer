from collections import OrderedDict
from operator import itemgetter
from .config import READMEPATH
# Helper functions

def return_yearwise_paper(paper_data):
    """
    Returns the reverse sorted year-wise paper data list
    :param paper_data: list of dicts
    :return: list of tuples. First item of tuple is year. Second item is dict
    """
    paper_yearwise = {}
    for pdata in paper_data:
        year = int(pdata['ptime'][:4])
        if year in paper_yearwise:
            paper_yearwise[year].append(pdata)
        else:
            paper_yearwise[year] = [pdata]
    paper_yearwise = sorted(paper_yearwise.items(), reverse=True)
    return paper_yearwise


def top_ents_results(papers, ent_type):
    """
    papers: list of dictionaries (coming from paper search query)
    return: dictionary of entitiy frequencies in descending order
    """
    entity_dict = {}
    for paper in papers:
        ents = paper['ner'][ent_type]
        for ent in ents:
            try:
                entity_dict[ent]+=1
            except:
                entity_dict[ent]=1

    d = OrderedDict(sorted(entity_dict.items(), key=itemgetter(1), reverse=True))
    # print(d)
    return d

def get_ent_names(ents):
    """
    ents: dictionary_item with entity type as key and list as value
    returns: list of formatted entity type names
    """
    mapp = {'ner_dna':"DNA",
            'ner_rna':"RNA",
            'ner_protein':"Proteins",
            'ner_cell_type': "Cell Types",
            'ner_cell_line': "Cell Lines",
            'ner_ched': "Chemical Entities",
            'ner_disease': "Diseases",
            }
    formatted_names = []
    for t in ents:
        formatted_names.append(mapp[t[0]])

    return formatted_names


def get_ent_type_name(ent_type):
    """
    ent_type: string
    returns: string
    """
    mapp = {'ner_dna':"DNA entities",
            'ner_rna':"RNA entities",
            'ner_protein':"Proteins entities",
            'ner_cell_type': "Cell Types entities",
            'ner_cell_line': "Cell Lines entities",
            'ner_ched': "Chemical entities",
            'ner_disease': "Diseases",
            }

    return mapp[ent_type]


def get_metadata_numbers():
    """
    :return: dict with number of papers for each of: 'biorxiv_medrxiv',
    'comm_use_subset', 'custom_license', 'noncomm_use_subset'
    """
    with open(READMEPATH) as f:
        lines = f.readlines()

    i = 0
    for line in range(len(lines)):
        if 'SUMMARY' in lines[line]:
            i = line
    last_update = lines[i:]
    papers = ['biorxiv_medrxiv', 'comm_use_subset', 'custom_license', 'noncomm_use_subset','Full text']
    d = {}
    for paper in papers:
        for line in range(len(last_update)):
            if last_update[line].startswith(paper):
                c = 0
                c += int(last_update[line].split(':')[1].split()[0])
                # if 'PDF' in last_update[line + 1]:
                #     c += int(last_update[line + 1].split('-')[1].split()[0])
                # if 'PMC' in last_update[line + 2]:
                #     c += int(last_update[line + 2].split('-')[1].split()[0])
                d[paper] = c
    return d