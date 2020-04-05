from flask import render_template, request, redirect, session, flash, jsonify, make_response
from app import app

from pymongo import MongoClient
import pandas as pd
from .elasticSearch import *

from datetime import datetime
current_year = int(datetime.now().year)

#mongoClient = MongoClient('localhost', 20000)
#db = mongoClient.new_papers

#author_db = mongoClient.author
#authorCollection = author_db.author

#subscriptionCollection = db['subscriptions']
#papers = db['new_papers']

def FirstNameLastName(name):
    l_n = name.split(",")
    return l_n[-1]+', '+ l_n[0]

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
        entities = named_entities_es(pids)
        return render_template('search_paper.html', items = papers, keyword=text, field=field,
                               ners=entities)

    if field == 'FullText':
        papers, pids = fulltextsearch(text)
        entities = named_entities_es(pids)
        return render_template('search_paper.html', items=papers, keyword=text, field=field,
                               ners=entities)

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
        entities = named_entities_es(pids)
        return render_template('filter_results.html', items=papers_filt, ners=entities)
    if field == 'FullText':
        papers_filt, pids = fulltextsearch_filteryr(text, int(yr_s), int(yr_e))
        entities = named_entities_es(pids)
        return render_template('filter_results.html', items=papers_filt, ners=entities)

@app.route('/gene_filter')
def get_html_gene_filter():
    yr_s = request.args.get("yr_s")
    yr_e = request.args.get("yr_e")
    field = request.args.get("field")
    text = request.args.get("searchtext")
    gene = request.args.get("gene")

    if field == 'Paper':
        papers_filt, pids = paper_filteryr(text, int(yr_s), int(yr_e))
        pids_new = named_entity_filter(pids,gene)
        d = []
        for i in range(len(pids)):
            if pids[i] in pids_new:
                d.append(papers_filt[i])
        return render_template('filter_results_gene.html', items=d)

    if field == 'FullText':
        papers_filt, pids = fulltextsearch_filteryr(text, int(yr_s), int(yr_e))
        pids_new = named_entity_filter(pids, gene)
        d = []
        for i in range(len(pids)):
            if pids[i] in pids_new:
                d.append(papers_filt[i])
        return render_template('filter_results_gene.html', items=d)

@app.route('/prge/<ent_name>')
def get_indv_page(ent_name):
    ent = get_prge_info(ent_name)
    pids = ent[1]
    doc_freq = ent[2]
    first_mention_pid = ent[3]
    co_mentions = ent[4]
    return render_template('prge_indv.html',
    ent_name = ent_name,
    paper_mentions = [paper_namefromid(pid) for pid in pids],
    doc_freq = doc_freq,
    first_mention = paper_namefromid(first_mention_pid),
    co_mentions = co_mentions
    )

@app.route('/get_data/prge', methods=["GET", "POST"])
def graph_data():
    ent_name = request.json["ent_name"]
    ent = get_prge_info(ent_name)
    first_mention = paper_namefromid(ent[3])
    first_yr = int(first_mention[3][:4])
    gene_data = {}

    mention_distribution = {}
    for pid in ent[1]:
        p = paper_namefromid(pid)
        y = p[3][:4]
        try:
            mention_distribution[y]+=1
        except:
            mention_distribution[y]=1
    
    yearwise_mentions = []
    for y in range(current_year,first_yr-5,-1):
    # print(y)
        try:
            yearwise_mentions.append(mention_distribution[str(y)])
        except:
            yearwise_mentions.append(0)

    gene_data['yearwise_mentions'] = yearwise_mentions
    gene_data["years"] = list(range(current_year, first_yr - 5, -1))

    resp = jsonify(gene_data)
    return resp
