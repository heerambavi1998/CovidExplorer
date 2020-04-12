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