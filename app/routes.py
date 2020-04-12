from flask import render_template, request, redirect, session, flash, jsonify
from datetime import datetime
from app import app
from .elasticSearch import *
from .helper import *

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    session.clear()
    # Todo : Make search
    
    return render_template('index.html', title='Covid-19')

@app.route('/team', methods=['GET'])
def team():
    return render_template('team.html')


@app.route('/search_all')
def search_all():
    return render_template('search_main.html')

@app.route('/search', methods=["GET", "POST"])
def overall_search():
    #this comes from main search box
    field = request.form.get("field")
    text = request.form.get("search-text")
    return redirect('/search/%s/%s' %(field,text))

@app.route('/search/<field>/<text>', methods=["GET", "POST"])
def search_field(field, text):
    if field == 'Paper':
        papers, pids = paper_es(text)
        paper_data = return_yearwise_paper(papers)
        ordered_ents_prge = top_ents_results(papers,'prge')
        ordered_ents_ched = top_ents_results(papers,'ched')
        # entities = named_entities_es(pids)
        return render_template('search_paper.html', items=paper_data, keyword=text, field=field,
                               prge=ordered_ents_prge.keys(), ched=ordered_ents_ched.keys())

    if field == 'FullText':
        papers, pids = fulltextsearch(text)
        paper_data = return_yearwise_paper(papers)
        ordered_ents_prge = top_ents_results(papers,'prge')
        ordered_ents_ched = top_ents_results(papers,'ched')
        # entities = named_entities_es(pids)
        return render_template('search_paper.html', items=paper_data, keyword=text, field=field,
                               prge=ordered_ents_prge.keys(), ched=ordered_ents_ched.keys())

    if field == 'Author':
        authors = author_es(text)
        return  render_template('search_author.html', items = authors, keyword=text)


# route for search jquery with year filter
@app.route('/year_filter')
def get_html_year_filter():
    yr_s = request.args.get("yr_s")
    yr_e = request.args.get("yr_e")
    field = request.args.get("field")
    text = request.args.get("searchtext")
    if field == 'Paper':
        papers_filt, pids = paper_filteryr(text, int(yr_s), int(yr_e))
        paper_data = return_yearwise_paper(papers_filt)

        ordered_ents_prge = top_ents_results(papers_filt,'prge')
        ordered_ents_ched = top_ents_results(papers_filt,'ched')
        return render_template('filter_results.html', items=paper_data,
                               prge=ordered_ents_prge.keys(), ched=ordered_ents_ched.keys())
    if field == 'FullText':
        papers_filt, pids = fulltextsearch_filteryr(text, int(yr_s), int(yr_e))
        paper_data = return_yearwise_paper(papers_filt)

        ordered_ents_prge = top_ents_results(papers_filt,'prge')
        ordered_ents_ched = top_ents_results(papers_filt,'ched')
        return render_template('filter_results.html', items=paper_data,
                               prge=ordered_ents_prge.keys(), ched=ordered_ents_ched.keys())


@app.route('/gene_filter')
def get_html_gene_filter():
    yr_s = request.args.get("yr_s")
    yr_e = request.args.get("yr_e")
    field = request.args.get("field")
    text = request.args.get("searchtext")
    print(request.args.get("entity"))
    ent_type = request.args.get("entity").split(':')[0]
    entity = request.args.get("entity").split(':')[1]

    if field == 'Paper':
        papers_filt, pids = paper_filteryr(text, int(yr_s), int(yr_e))
        pids_new = named_entity_filter(pids,entity, ent_type)
        d = []
        for i in range(len(pids)):
            if pids[i] in pids_new:
                d.append(papers_filt[i])
        paper_data = return_yearwise_paper(d)
        return render_template('filter_results_gene.html', items=paper_data)

    if field == 'FullText':
        papers_filt, pids = fulltextsearch_filteryr(text, int(yr_s), int(yr_e))
        pids_new = named_entity_filter(pids, entity, ent_type)
        d = []
        for i in range(len(pids)):
            if pids[i] in pids_new:
                d.append(papers_filt[i])
        paper_data = return_yearwise_paper(d)
        return render_template('filter_results_gene.html', items=paper_data)

@app.route('/entity/<ent_type>/<ent_name>')
def get_indv_page(ent_type, ent_name):
    ent = get_named_entity_info(ent_name, ent_type)
    pids = ent[1]
    doc_freq = ent[2]
    first_mention_pid = ent[3]
    co_mentions = ent[4]

    paper_data = return_yearwise_paper([paper_namefromid(pid) for pid in pids])
    return render_template('prge_indv.html',
        ent_type = ent_type,
        ent_name = ent_name,
        paper_mentions = paper_data,
        doc_freq = doc_freq,
        first_mention = paper_namefromid(first_mention_pid),
        co_mentions = co_mentions
        )

@app.route('/get_data/prge', methods=["GET", "POST"])
def graph_data():
    current_year = int(datetime.now().year)
    ent_name = request.json["ent_name"]
    ent_type = request.json["ent_type"]
    ent = get_named_entity_info(ent_name, ent_type)
    first_mention = paper_namefromid(ent[3])
    first_yr = int(first_mention['ptime'][:4])
    gene_data = {}

    mention_distribution = {}
    for pid in ent[1]:
        p = paper_namefromid(pid)
        y = p['ptime'][:4]
        try:
            mention_distribution[y]+=1
        except:
            mention_distribution[y]=1
    
    yearwise_mentions = []
    for y in range(current_year,first_yr-1,-1):
    # print(y)
        try:
            yearwise_mentions.append(mention_distribution[str(y)])
        except:
            yearwise_mentions.append(0)

    gene_data['yearwise_mentions'] = yearwise_mentions
    gene_data["years"] = list(range(current_year, first_yr - 1, -1))

    resp = jsonify(gene_data)
    return resp
