from flask import render_template, request, redirect, session, flash, jsonify
from app import app

from pymongo import MongoClient
import pandas as pd
from .elasticSearch import conf_es, author_es, paper_es, fulltextsearch

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
    
    return render_template('index.html', title='CSE DB')

# @app.route('/team', methods=['GET'])
# def team():
#     return render_template('team.html')

@app.route('/search', methods=["GET", "POST"])
def overall_search():
    field = request.form.get("field")
    text = request.form.get("search-text")
    # if field == 'Author':
    #     p = []
    #     authors = author_es(text)
    #     for t in authors:
    #         temp = {"title" : t[1], "id" : t[0]}
    #         p.append(temp)
    #     return  render_template('search_author.html', items = p)
    # if field == 'Paper':
    #     papers = paper_es(text)
    #     return  render_template('search_paper.html', items = papers)
    if field == 'Full-Text':
        papers = fulltextsearch(text)
        return  render_template('fulltextsearch.html', items = papers)
    # if field == 'Venues':
    #     confs = conf_es(text)
    #     l = set()
    #     for conf in confs:
    #         for p in conf[0]:
    #             if text in p.lower():
    #                 l.add((p, conf[1]))
    #     return render_template('search_conf.html', items = list(l))

    # if field == 'URL Domain':
    #
    #     df = pd.read_csv('app/[IMP]for_url.csv')
    #     df_1 = df['Domain'].drop_duplicates()
    #
    #     domains = df_1.str.find(text)
    #     df_df_1 = pd.concat([domains, df_1],axis=1)
    #
    #     df_df_1.columns = ['Marker', 'Domain']
    #     domains = list(df_df_1[df_df_1['Marker'] != -1]['Domain'].dropna())
    #
    #     return  render_template('url_search.html', items = domains)
    #
    # if field == 'Field of Study':
    #
    #     df = pd.read_csv('app/for_fos.csv')
    #     df_1 = df['Topics'].drop_duplicates()
    #
    #     domains = df_1.str.find(text)
    #     df_df_1 = pd.concat([domains, df_1],axis=1)
    #
    #     df_df_1.columns = ['Marker', 'Domain']
    #     domains = list(df_df_1[df_df_1['Marker'] != -1]['Domain'].dropna())
    #
    #     new = df[df['Topics'].isin(domains)]
    #
    #     items = []
    #     for a,b in zip(new['Topics'], new['Category']):
    #         items.append((a.title(),b,'_'.join(a.split(' '))))
    #
    #     return  render_template('fos_search.html', items = items)
    #
    # if field == 'All':
    #     auth_items = []
    #     authors = author_es(text)
    #     for t in authors:
    #         temp = {"title" : t[1], "id" : t[0]}
    #         auth_items.append(temp)
    #     paper_items = paper_es(text)
    #     confs = conf_es(text)
    #     l = set()
    #     for conf in confs:
    #         for p in conf[0]:
    #             if text in p:
    #                 l.add((p, conf[1]))
    #     if list(l) == []:
    #         for conf in confs:
    #             for p in conf[0]:
    #                 if text.lower() in p.lower():
    #                     l.add((p, conf[1]))
##########################
#         df = pd.read_csv('app/[IMP]for_url.csv')
#         df_1 = df['Domain'].drop_duplicates()
#
#         domains = df_1.str.find(text)
#         df_df_1 = pd.concat([domains, df_1],axis=1)
#
#         df_df_1.columns = ['Marker', 'Domain']
#         domain_items = list(df_df_1[df_df_1['Marker'] != -1]['Domain'].dropna())
# ########################
#         df = pd.read_csv('app/for_fos.csv')
#         df_1 = df['Topics'].drop_duplicates()
#
#         domains = df_1.str.find(text)
#         df_df_1 = pd.concat([domains, df_1],axis=1)
#
#         df_df_1.columns = ['Marker', 'Domain']
#         domains = list(df_df_1[df_df_1['Marker'] != -1]['Domain'].dropna())
#
#         new = df[df['Topics'].isin(domains)]
#
#         fos = []
#         for a,b in zip(new['Topics'], new['Category']):
#             fos.append((a.title(),b,'_'.join(a.split(' '))))
# #######################
#         papers = fulltextsearch(text)
#
#     return render_template('search_all.html',
#                 auth_items = auth_items[:10],
#                 paper_items = paper_items[:10],
#                 conf_items = list(l)[:10],
#                 domain_items = domain_items[:10],
#                 fos_items = fos[:10],
#                 full_items = papers[:10])
