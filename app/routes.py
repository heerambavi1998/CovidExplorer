from flask import render_template, request, redirect, session, flash, jsonify, make_response
from app import app

from pymongo import MongoClient
import pandas as pd
from .elasticSearch import author_es, paper_es, fulltextsearch, paper_filteryr, fulltextsearch_filteryr

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

# @app.route('/team', methods=['GET'])
# def team():
#     return render_template('team.html')
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
        papers = paper_es(text)
        return render_template('search_paper.html', items = papers, keyword=text, field=field)

    if field == 'FullText':
        papers = fulltextsearch(text)
        return render_template('search_paper.html', items=papers, keyword=text, field=field)

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
        papers_filt = paper_filteryr(text, int(yr_s), int(yr_e))
        return render_template('filter_results.html', items=papers_filt)
    if field == 'FullText':
        papers_filt = fulltextsearch_filteryr(text, int(yr_s), int(yr_e))
        return render_template('filter_results.html', items=papers_filt)
