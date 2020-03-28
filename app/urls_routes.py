from flask import render_template, request, redirect, session
import json
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')

from app import app
import pandas as pd 
import pickle
import os
import json
from nltk.probability import FreqDist
import datetime

df = pd.read_csv('app/[IMP]for_url.csv')
df["Domain_lowercase"] = df["Domain"].map(lambda x: x if type(x)!=str else x.lower())
df_grp = df.groupby('Domain')


with open('app/for_url.json', encoding="utf-8") as data_file:
	url_dict = json.load(data_file)

def get_year(code):
	try: 
		code_ = int(code[1:3])
		if code_ > 21:
			year = 1900 + code_
		else:
			year = 2000 + code_
		return year
	except:
		return None

@app.route('/url_search', methods=["GET", "POST"])
def url_suggestions():
	content = request.form.get("url").lower()
	df_1 = df['Domain_lowercase'].drop_duplicates()

	domains = df_1.str.find(content)
	df_df_1 = pd.concat([domains, df_1],axis=1)

	df_df_1.columns = ['Marker', 'Domain_lowercase']
	domains = list(df_df_1[df_df_1['Marker'] != -1]['Domain_lowercase'].dropna())

	return  render_template('url_search.html', items = domains)


@app.route('/urls_all', methods = ['GET'])
def get_all_urls():

	domains = [{'name': 'Github', 'count': '9977'},{'name': 'Aclweb', 'count': '4979'}, {'name': 'DOI', 'count': '4683'}, {'name': 'Google', 'count': '3144'},  {'name': 'Stanford', 'count': '3144'}]
	corporate = [{'name': 'Github', 'count': '9977'}, {'name': 'Google', 'count': '3144'}, {'name': 'Sourceforge', 'count': '1948'}, {'name': 'Wikipedia', 'count': '1748'},  {'name': 'NIST', 'count': '1527'}]
	affiliations = [{'name': 'Stanford', 'count': '3144'},{'name': 'Upenn', 'count': '1790'}, {'name': 'CMU', 'count': '945'}, {'name': 'NTU', 'count': '620'}, {'name': 'Princeton', 'count': '593'} ]
	digital = [{'name': 'Aclweb', 'count': '4979'}, {'name': 'DOI', 'count': '4683'},{'name': 'Wikipedia', 'count': '1748'}, {'name': 'Arxiv', 'count': '1507'}, {'name': 'ACM', 'count': '668'} ]


	domain_dict = {1995: 12, 1996: 33,1997: 47,1998: 134,1999: 101,2000: 288,2001: 206,2002: 496,2003: 373,2004: 788,2005: 470,2006: 989,2007: 582,2008: 1098,2009: 1020,2010: 1537,2011: 1139,2012: 1921,2013: 1480,2014: 2375,2015: 1483,2016: 2411,2017: 1878,2018: 2315,2019: 1396}

	new_domain_year = list(domain_dict.keys())
	new_domain_count = list(domain_dict.values())

	link_dict = {1995: 13,	1996: 38,1997: 65, 1998: 214,1999: 148,2000: 617,2001: 413,2002: 1097,2003: 736,2004: 1915,2005: 1037,2006: 2453,2007: 1318,2008: 2772,2009: 2311,2010: 3976,2011: 2675,2012: 5213,2013: 3987,2014: 6842,2015: 4292,2016: 8034,2017: 10705,2018: 10499,2019: 5061}

	new_link_year = list(link_dict.keys())
	new_link_count = list(link_dict.values())

	return render_template('url_all.html', domains = domains, corporate = corporate, affiliations = affiliations, digital = digital, new_domain_year= new_domain_year, new_domain_count = new_domain_count, new_link_year =new_link_year, new_link_count = new_link_count)

# Individual paper page
@app.route('/url/<url_id>', methods = ['GET'])
def IndividualPage(url_id):
	try:
		page_py = wiki_wiki.page(url_id)
		wiki_link = page_py.fullurl
		summary = page_py.summary[0:500] + '... '
		more_info = 'For More Info'

		if ("refer to:" in summary) or ("stand for" in summary):
			wiki_link = 'http://www.google.com/search?q=%s'%('+'.join(url_id.split(' ')))
			more_info = "About"
			summary = ''

	except:
		summary = ''
		wiki_link = 'http://www.google.com/search?q=%s'%('+'.join(url_id.split(' ')))
		more_info = 'About'

	print(df_grp.head())

	code_list = list(set(df_grp.get_group(url_id)['Code']))
	code_list = [get_year(i) for i in code_list]

	max_year = max(code_list)
	min_year = min(code_list)

	year_dict = dict(FreqDist(code_list))
	year_dict_key = list(year_dict.keys())
	year_dict_value = list(year_dict.values())

	len_code_list = len(code_list)

	link_dict = dict(url_dict[url_id])
	link_list = list(link_dict.keys())
	len_link_list = len(link_list)

	return render_template('new_url_temp.html', url_id = url_id, summary= summary, wiki_link = wiki_link, more_info = more_info, link_dict = link_dict, link_list = link_list, len_link_list=len_link_list, len_code_list= len_code_list, max_year=max_year, min_year= min_year, year_dict_key=year_dict_key, year_dict_value=year_dict_value)
