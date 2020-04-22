from collections import OrderedDict
from operator import itemgetter

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