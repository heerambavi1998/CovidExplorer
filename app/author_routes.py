from flask import render_template, request, redirect, session, jsonify
from app import app
# import pickle
# import datetime
# import json

# current_year = int(datetime.datetime.now().year)
# number_of_years = 20

from .elasticSearch import author_es, author_findpapers, paper_namefromid
# from pymongo import MongoClient
# mongoClient = MongoClient('localhost', 20000)
# author_db = mongoClient.author
# authorCollection = author_db["author"]

# db = mongoClient.new_papers

# subscriptionCollection = db['subscriptions']
# papers = db['new_papers']


# import datetime
# now = datetime.datetime.now()

# subtopics= {'linguistic':['Discourse','Pragmatics','Lexical Semantics','Distributional Semantics',"Embeddings",'Formal Semantics',
#             'Propositional Semantics','Event Semantics', 
#             'Grounded Semantics','Ontologies','Syntax',
#             'Morphology','Phonology','Phonetics','Prosody','Gesture','Code Mixing','Code Switching','Multilingualism','Sociolinguistic Variation',
#             'Language Change','Typology','Neurolinguistics','Cognitive Linguistics','Psycholinguistics'],
           
#             'approach':['Multilingual Resources','Modeling Linguistic Knowledge ','Algorithm Development ','Data Analysis ',
#             'User Evaluation','Crowd Sourcing','Human Computation','Topic Modeling','Deep Learning','Bayesian Model','Kernel Method',
#             'Structured Prediction','Generative Model','Discriminative Model','Graphical Model','Representation Learning','Semi-supervised Learning',
#             'Unsupervised Learning'],

#             'task':['Language Understanding','Corpus Development','Corpus Annotation','Language Identification','Morphological Analysis',
#             'Tagging','Chunking','Syntactic Parsing','Semantic Parsing','Discourse Parsing','Word Sense Disambiguation','Named Entity Recognition',
#             'Textual Entailment','Semantic Similarity','Information Extraction','Information Retrieval','Relation Extraction','Sentiment Analysis',
#             'Emotion Detection','Event Detection','Time Normalization','Question Answering','Knowledge Acquisition','Coreference Resolution',
#             'Dialog Structure','Conversation Analysis','Language Generation','Summarization','Machine Translation','Paraphrasing',
#             'Text Simplification','Determining Discourse Relations','Text Organization','Argumentation Mining','Dialogue and Interactive Systems',
#             'Image Description Generation','Video Description Generation','Belief Analysis','Factuality Analysis','Modality Analysis',
#             'Irrealis Analysis','ASR','Spoken Language Processing','OCR','Word Segmentation','Text Categorization','Spelling Correction',
#             'Text Quality Prediction','Style Analysis','Predicting Speaker Characteristics','Authorship Attribution','Native Language Identification',
#             'Lexicon and Paraphrase Induction','Mathematical Models','Biomedical','Social Science','Ethics','Multimodal Systems',
#             'Modeling Human Language Processing','Computational Psycholinguistics','Modeling Human Language Acquisition'],

#             'language':['Multilingual','Chinese','English','Malay', 'Hindi', 'Tamil', 'Urdu', 'Sanskrit', 'Japanese', 'Korean','Spanish', 'French', 'Portugese','Arabic','Hebrew','Semitic','Low-Resource Languages','Signed Languages','Child Language'],
#             'dataset_type':['Scientific Literature','Literary Text','News','Encyclopedia','Biographies','Written Dialog',
#             'Chat','Social Media','Non-private Unedited Text ','Twitter','Blogs','Spoken Dialog','Child-directed Speech','Child Language',
#             'Other Spoken Genres','Human-Computer Interaction ','Query Logs','Biomedical Texts','Non-biomedical Scholarly Texts','Legal Documents ',
#             'Legal Opinions','Clinical Notes','Web Crawl']}



# with open('app/for_similar_authors.json', encoding="utf-8") as data_file:
# 	author_dict = json.load(data_file)


# @app.route('/get_data/author_citation_distribution', methods=["GET", "POST"])
# def citation_data():
# 	author_id = request.json["author_id"]
# 	data_citation = list(authorCollection.find({"_id":author_id},{"citation_last_n_years": 1, "citation_distribution": 1}))[0]

# 	author_citation = { }
# 	author_citation["citation_last_n_years"] = data_citation["citation_last_n_years"]
# 	author_citation["last_n_years"] = list(range(current_year, current_year-number_of_years, -1))

# 	yearwise_citation = []
# 	for y in range(current_year, current_year-number_of_years, -1):
# 		yearwise_citation.append(data_citation["citation_distribution"][str(y)])

# 	author_citation["citation_distribution"] = yearwise_citation

# 	resp = jsonify(author_citation)
# 	return resp


# @app.route('/author_search', methods=["GET", "POST"])
# def author_suggestions():
# 	content = request.form.get("author")
# 	p = []
# 	authors = author_es(content)
# 	for t in authors:
# 		temp = {"title" : t[1], "id" : t[0]}
# 		p.append(temp)
# 	return  render_template('search_author.html', items = p)



@app.route('/author/<author_name>', methods = ['GET'])
def get_author_page_new(author_name):
	#must return author individual page

	# author_name = ' '.join(author_id.split('-')).title()
	# print(author_name)
	paper_data = list(author_findpapers(author_name))
	paper_names=[]
	for pid in paper_data:
		paper_names.append(paper_namefromid(pid))
	return  render_template('author_pg.html', items = paper_names, keyword=author_name)

	# data = {}
	# # confs = set()
	# # conf_names = set()
	# for paper in paper_data:
	# 	l = {}
	# 	l["title"] = paper["paper_title"]
	# 	l["authors"] = paper["acl_author_name"]
	# 	l["authors_id"] = paper["acl_author_id"]
	# 	l["id"] = paper["_id"]
	# 	l["venue"] = paper["venue_name"]
	# 	l["year"] = paper["year"]
	# 	for venue in paper["venue_name"]:
	# 		confs.add((venue, paper["year"]))
	# 		conf_names.add(venue)
	# 	try:
	# 		data[int(paper["year"])].append(l)
	# 	except:
	# 		data[int(paper["year"])] = [l]

	# author_paper_year = []
	# for key in list(data.keys()):
	# 	l  = {"year" : key , "count" : len(data[key])}
	# 	author_paper_year.append(l)
	# data = sorted(data.items(), reverse=True)

	# auth_data = list(authorCollection.find({"_id" : author_id}))[0]
	# auth_paper_count = len(auth_data['all_papers_written'])
	# auth_coauthors = auth_data['all_coauthors']
	# for i in auth_coauthors:
	# 	if author_id == i:
	# 		auth_coauthors.remove(author_id)

	# auth_citations = auth_data["total_citations"]
	# auth_confs = list(confs)
	# auth_conf_names = list(conf_names)
	# first_acl_paper = auth_data["first_paper"]
	# last_acl_paper = auth_data["latest_paper"]
	# coauth_names = []
	# for authorID in auth_coauthors:
	# 	coauth_names.append(' '.join(authorID.split('-')).title())
	
	# try:
	# 	similar_authors = {}
	# 	similar_authors['author_name'] = []
	# 	similar_authors['author_id'] = []

	# 	for j in author_dict[author_id]:
	# 		if author_id != j:
	# 			temp = ' '.join(j.split('-')).title()
	# 			similar_authors['author_name'].append(temp) 
	# 			similar_authors['author_id'].append(j) 

	# 	auths_simi = []
	# 	for author, _id in zip(similar_authors["author_name"], similar_authors["author_id"]):
	# 		auths_simi.append((_id, author))

	# 		# auth_auths = []
	# 		# for author, _id in zip(temp["acl_author_name"], temp["acl_author_id"]):
	# 		# 	paper_auths.append((_id,author))

	# 		# paper_data['similar_papers'][j]['Author'] = paper_auths
	# except:
	# 	auths_simi = []
	# 	# pass



	# # print(type(auth_coauthors))
	# return render_template('new_auth_temp.html',
	# 	author = author_name,
	# 	auth_paper_data = data,
	# 	author_paper_year = author_paper_year,
	# 	author_id = author_id,
	# 	auth_paper_count = auth_paper_count,
	# 	auth_coauthors = auth_coauthors[:5],
	# 	auth_citations = auth_citations,
	# 	auth_confs = auth_confs,
	# 	auth_conf_names = auth_conf_names,
	# 	coauth_names = coauth_names,
	# 	first_acl_paper = first_acl_paper,
	# 	last_acl_paper = last_acl_paper,
	# 	similar_authors = auths_simi,
	# 	count_author_linguistic = len(auth_data["linguistic"]),
	# 	count_author_task = len(auth_data["task"]),
	# 	count_author_approach = len(auth_data["approach"]),
	# 	count_author_language = len(auth_data["language"]),
	# 	count_author_dataset_type = len(auth_data["dataset_type"])
	# 	)



# @app.route('/get_data/author', methods=["GET", "POST"])
# def graph_data():
# 	author_id = request.json["author_id"]
# 	author_name = ' '.join(author_id.split('-')).title()
# 	author_data = list(authorCollection.find({"_id":author_id}))[0]
	
# 	author_data_final = {}
# 	author_data_final["citation_last_n_years"] = author_data["citation_last_n_years"]

# 	yearwise_citation = []
# 	for y in range(current_year, current_year-number_of_years, -1):
# 		try:
# 			yearwise_citation.append(author_data["citation_distribution"][str(y)])
# 		except:
# 			yearwise_citation.append(0)

# 	yearwise_papers = []
# 	for y in range(current_year, current_year-number_of_years, -1):
# 		try:
# 			yearwise_papers.append(author_data["paper_distribution"][str(y)])
# 		except:
# 			yearwise_papers.append(0)
			
			
# 	author_data_final["citation_distribution"] = yearwise_citation
# 	author_data_final["paper_distribution"] = yearwise_papers
# 	author_data_final["last_n_years"] = list(range(current_year, current_year-number_of_years, -1))
			

# 	for topic_distribution in ['linguistic', 'task', 'approach', 'language', 'dataset_type']:
# 		if topic_distribution in author_data.keys():
# 			author_data_final[topic_distribution] = {"count": [], "label": []}
# 			total_topic_count = sum(author_data[topic_distribution].values())
# 			subtopic_list=subtopics[topic_distribution]
# 			other_count = 0
# 			for topic, count in author_data[topic_distribution].items():
# 				subtopic_name = topic
# 				for name in subtopic_list:
# 					name_id=''.join(name.split(' ')).lower()
# 					if subtopic_name == name_id:
# 						subtopic_name = name
# 				if count < 0.05*total_topic_count:
# 					other_count += count
# 				else:	
# 					author_data_final[topic_distribution]["label"].append(subtopic_name)
# 					author_data_final[topic_distribution]["count"].append(count)
# 			if other_count>0:
# 				author_data_final[topic_distribution]["label"].append("Other")
# 				author_data_final[topic_distribution]["count"].append(other_count)
# 	print(author_data_final)
# 	resp = jsonify(author_data_final)
# 	return resp




# @app.route('/author_all', methods = ['GET'])
# def get_all_authors():
# 	# Get new authors in last 2 years, sorted by citation count
# 	new_authors_cit = list(authorCollection.find({"first_paper":str(current_year-1)},{"total_citations":1}).sort([("total_citations",-1)]).limit(10))
# 	for a in new_authors_cit:
# 		a["name"] = ' '.join(a["_id"].split('-')).title()

# 	# Get new authors in last 2 years, sorted by citation count
# 	new_authors_paperc = list(authorCollection.find({"first_paper":str(current_year-1)},{"total_papers":1}).sort([("total_papers",-1)]).limit(10))
# 	for a in new_authors_paperc:
# 		a["name"] = ' '.join(a["_id"].split('-')).title()

# 	# get new author distribution
# 	# new_author_count = []
# 	# new_author_year = []
# 	# for i in range(20):
# 	#   no_new_author = authorCollection.find({"first_paper":str(current_year-i)}).count()
# 	#   new_author_count.append(no_new_author)
# 	#   new_author_year.append(current_year-i)

# 	# most cited authors
# 	most_cited_authors = list(authorCollection.find({},{"total_citations":1}).sort([("total_citations",-1)]).limit(10))
# 	for a in most_cited_authors:
# 		a["name"] = ' '.join(a["_id"].split('-')).title()

# 	# most cited authors - last 5 years
# 	most_cited_authors_5 = list(authorCollection.find({},{"citation_last_n_years":1}).sort([("citation_last_n_years.5",-1)]).limit(10))
# 	for a in most_cited_authors_5:
# 		a["name"] = ' '.join(a["_id"].split('-')).title()

# 	# most cited authors - last 1 year
# 	most_cited_authors_1 = list(authorCollection.find({},{"citation_last_n_years":1}).sort([("citation_last_n_years.1",-1)]).limit(10))
# 	for a in most_cited_authors_1:
# 		a["name"] = ' '.join(a["_id"].split('-')).title()


# 	# author with most papers
# 	most_papers_authors = list(authorCollection.find({},{"total_papers":1}).sort([("total_papers",-1)]).limit(10))
# 	for a in most_papers_authors:
# 		a["name"] = ' '.join(a["_id"].split('-')).title()

# 	most_diverse_authors = [[u'iryna-gurevych', u'Iryna Gurevych'],
# 							 [u'noah-a-smith', u'Noah A Smith'],
# 							 [u'timothy-baldwin', u'Timothy Baldwin'],
# 							 [u'eduard-hovy', u'Eduard Hovy'],
# 							 [u'hinrich-schutze', u'Hinrich Schutze'],
# 							 [u'dan-jurafsky', u'Dan Jurafsky'],
# 							 [u'walter-daelemans', u'Walter Daelemans'],
# 							 [u'heng-ji', u'Heng Ji'],
# 							 [u'anna-korhonen', u'Anna Korhonen'],
# 							 [u'yuji-matsumoto', u'Yuji Matsumoto']]
# 	# print(most_diverse_authors)

# 	return render_template('authorsAll.html',
# 		new_authors = new_authors_cit,
# 		new_authors_paper_count = new_authors_paperc,
# 		most_papers_authors = most_papers_authors,
# 		most_cited_authors = most_cited_authors,
# 		most_cited_authors_5 = most_cited_authors_5,
# 		most_cited_authors_1 = most_cited_authors_1,
# 		most_diverse_authors = most_diverse_authors)
# 		# new_author_count = new_author_count,
# 		# new_author_year = new_author_year)
