from app import app

from pymongo import MongoClient
mongoClient = MongoClient('localhost', 20000)
author_db = mongoClient.author
authorCollection = author_db["author"]

db = mongoClient.new_papers

subscriptionCollection = db['subscriptions']
papers = db['new_papers']

import datetime, json
from nltk.probability import FreqDist

current_year = int(datetime.datetime.now().year)
number_of_years = 20


from flask import Flask, Blueprint, jsonify
from flask_restplus import Api, Resource, fields, Namespace
import pandas as pd
import wikipediaapi
from .elasticSearch import conf_es, author_es, paper_es, fulltextsearch

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, version='1.0.0', title='NLPExplorer API',
    description="The following consists of APIs which the website uses to fetch data from the database.\n The API is open source under Apache License 2.0.")

app.register_blueprint(blueprint)

ns1 = Namespace('author', description="All APIs related to author data")
ns2 = Namespace('paper', description="All APIs related to paper data")
ns3 = Namespace('conference', description="All APIs related to conference data")
ns4 = Namespace('url', description="All APIs related to URLs data")
ns5 = Namespace('fos', description="All APIs related to the field of study data")
ns6 = Namespace('search', description="API for searching in our database")

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
api.add_namespace(ns4)
api.add_namespace(ns5)
api.add_namespace(ns6)

@ns1.route('/get-data/<author_id>')
class Author_Data(Resource):
    @ns1.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self, author_id):
        author_name = ' '.join(author_id.split('-')).title()
        paper_data = list(papers.find({"acl_author_id": author_id}))

        data = {}
        confs = set()
        conf_names = set()
        for paper in paper_data:
            l = {}
            l["title"] = paper["paper_title"]
            l["authors"] = paper["acl_author_name"]
            l["authors_id"] = paper["acl_author_id"]
            l["id"] = paper["_id"]
            l["venue"] = paper["venue_name"]
            l["year"] = paper["year"]
            for venue in paper["venue_name"]:
                confs.add((venue, paper["year"]))
                conf_names.add(venue)
            try:
                data[int(paper["year"])].append(l)
            except:
                data[int(paper["year"])] = [l]

        author_paper_year = []
        for key in list(data.keys()):
            l  = {"year" : key , "count" : len(data[key])}
            author_paper_year.append(l)
        data = sorted(data.items(), reverse=True)

        try:   
            auth_data = list(authorCollection.find({"_id" : author_id}))[0]
        except:
            return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500
        auth_paper_count = len(auth_data['all_papers_written'])
        auth_coauthors = auth_data['all_coauthors']
        for i in auth_coauthors:
            if author_id == i:
                auth_coauthors.remove(author_id)

        auth_citations = auth_data["total_citations"]
        auth_confs = list(confs)
        auth_conf_names = list(conf_names)
        first_acl_paper = auth_data["first_paper"]
        last_acl_paper = auth_data["latest_paper"]
        coauth_names = []
        for authorID in auth_coauthors:
            coauth_names.append(' '.join(authorID.split('-')).title())
        
        try:
            similar_authors = {}
            similar_authors['author_name'] = []
            similar_authors['author_id'] = []

            for j in author_dict[author_id]:
                if author_id != j:
                    temp = ' '.join(j.split('-')).title()
                    similar_authors['author_name'].append(temp) 
                    similar_authors['author_id'].append(j) 

            auths_simi = []
            for author, _id in zip(similar_authors["author_name"], similar_authors["author_id"]):
                auths_simi.append((_id, author))

                # auth_auths = []
                # for author, _id in zip(temp["acl_author_name"], temp["acl_author_id"]):
                # 	paper_auths.append((_id,author))

                # paper_data['similar_papers'][j]['Author'] = paper_auths
        except:
            auths_simi = []
            # pass

        resp = { "author" : author_name, "paper_data" : data, "co-authors" : coauth_names, "conferences" : auth_confs,
                "total-citations" : auth_citations, "total-papers" : auth_paper_count}
        return resp

@ns1.route('/get-citation-data/<author_id>')
class Author_Data(Resource):
    @ns1.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self, author_id):
        try:
            data_citation = list(authorCollection.find({"_id":author_id},{"citation_last_n_years": 1, "citation_distribution": 1}))[0]
        except:
            return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500
        author_citation = { }
        author_citation["citation_last_n_years"] = data_citation["citation_last_n_years"]
        author_citation["last_n_years"] = list(range(current_year, current_year-number_of_years, -1))

        yearwise_citation = []
        for y in range(current_year, current_year-number_of_years, -1):
            yearwise_citation.append(data_citation["citation_distribution"][str(y)])

        author_citation["citation_distribution"] = yearwise_citation

        resp = jsonify(author_citation)
        return resp

@ns1.route('/most_cited')
class Author_Data(Resource):
    @ns1.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def get(self):
        most_cited_authors = list(authorCollection.find({},{"total_citations":1}).sort([("total_citations",-1)]).limit(10))
        for a in most_cited_authors:
            a["name"] = ' '.join(a["_id"].split('-')).title()
        return most_cited_authors

@ns1.route('/most_papers')
class Author_Data(Resource):
    @ns1.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def get(self):
        most_papers_authors = list(authorCollection.find({},{"total_papers":1}).sort([("total_papers",-1)]).limit(10))
        for a in most_papers_authors:
            a["name"] = ' '.join(a["_id"].split('-')).title()
        return most_papers_authors
        
@ns1.errorhandler(Exception)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns1.errorhandler(KeyError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns1.errorhandler(IndexError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

"""
"""

@ns2.route('/get-data/<paper_id>')
class Paper_Data(Resource):
    @ns2.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self, paper_id):
        try:
            paper = list(papers.find({"_id": paper_id}, {"paper_title":1,"acl_author_name" : 1,"acl_author_id" :1}))[0]
        except:
            return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500
        paper_data = {}
        paper_data['id'] = paper_id
        try:
            paper_data['title'] = paper['paper_title']
        except:
            pass
        
        try:
            paper_auths = []
            for author, _id in zip(paper["acl_author_name"], paper["acl_author_id"]):
                paper_auths.append((_id,author))
            paper_data['authors'] = paper_auths
        except:
            pass

        return paper_data

@ns2.route('/get-data/citations/<paper_id>')
class Paper_Data(Resource):
    @ns2.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self, paper_id):
        cited_paper_year_list = list(papers.find({"ref_ACLcode":request.json["paper_id"]},{"_id":0,"year":1}))
        yearwise_citation = {}
        for year in cited_paper_year_list:
            try:
                yearwise_citation[int(year['year'])] += 1
            except KeyError:
                yearwise_citation[int(year['year'])] = 1

        final_citation_dict = {"year":[],"citation_count":[]}
        for key in yearwise_citation:
            final_citation_dict["year"].append(key)
            final_citation_dict["citation_count"].append(yearwise_citation[key])
        
        resp = jsonify(final_citation_dict)

        return resp

@ns2.errorhandler(Exception)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns2.errorhandler(KeyError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns2.errorhandler(IndexError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

"""
"""

@ns3.route('/get-data/<conference_id>')
class Conference_Data(Resource):
    @ns3.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self, conference_id):
        conf_title, year = conf_id.split("-")
        conf_data = list(papers.find({"venue_name" : conf_title, "year" : year}).sort([("total_citations",-1)]))
        data = {}
        for paper in conf_data:
            try:
                l = {}
                l["title"] = paper["paper_title"]
                l["authors"] = paper["acl_author_name"]
                l["authors_id"] = paper["acl_author_id"]
                l["id"] = paper["_id"]
                try:
                    data[int(paper["year"])].append(l)
                except:
                    data[int(paper["year"])] = [l]
            except:
                None
        data = sorted(data.items(), reverse=True)

        resp = {"title" : conf_title, "year" : year, "data" : data}

@ns3.errorhandler(Exception)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns3.errorhandler(KeyError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns3.errorhandler(IndexError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500


"""
"""
df = pd.read_csv('app/[IMP]for_url.csv')
df_grp = df.groupby('Domain')

wiki_wiki = wikipediaapi.Wikipedia('en')

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


@ns4.route('/get-data/<url_id>')
class Url_Data(Resource):
    @ns4.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self, url_id):
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

        return { "url_id" : url_id, "summary" : summary, "wiki_link" : wiki_link, "more_info" : more_info,
                        "link_dict": link_dict, "link_list" : link_list, "max_year": max_year, "min_year": min_year}

@ns4.errorhandler(Exception)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns4.errorhandler(KeyError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns4.errorhandler(IndexError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500


"""
"""

subtopics= [['Discourse','Pragmatics','Lexical Semantics','Distributional Semantics',"Embeddings",'Formal Semantics',
            'Propositional Semantics','Event Semantics',
            #'Extra-propositional Semantics',
            'Grounded Semantics','Ontologies','Syntax',
            'Morphology','Phonology','Phonetics','Prosody','Gesture','Code Mixing','Code Switching','Multilingualism','Sociolinguistic Variation',
            'Language Change','Typology','Neurolinguistics','Cognitive Linguistics','Psycholinguistics'],
           
            ['Multilingual Resources','Modeling Linguistic Knowledge ','Algorithm Development ','Data Analysis ',
            'User Evaluation','Crowd Sourcing','Human Computation','Topic Modeling','Deep Learning','Bayesian Model','Kernel Method',
            'Structured Prediction','Generative Model','Discriminative Model','Graphical Model','Representation Learning','Semi-supervised Learning',
            'Unsupervised Learning'],

            ['Language Understanding','Corpus Development','Corpus Annotation','Language Identification','Morphological Analysis',
            'Tagging','Chunking','Syntactic Parsing','Semantic Parsing','Discourse Parsing','Word Sense Disambiguation','Named Entity Recognition',
            'Textual Entailment','Semantic Similarity','Information Extraction','Information Retrieval','Relation Extraction','Sentiment Analysis',
            'Emotion Detection','Event Detection','Time Normalization','Question Answering','Knowledge Acquisition','Coreference Resolution',
            'Dialog Structure','Conversation Analysis','Language Generation','Summarization','Machine Translation','Paraphrasing',
            'Text Simplification','Determining Discourse Relations','Text Organization','Argumentation Mining','Dialogue and Interactive Systems',
            'Image Description Generation','Video Description Generation','Belief Analysis','Factuality Analysis','Modality Analysis',
            'Irrealis Analysis','ASR','Spoken Language Processing','OCR','Word Segmentation','Text Categorization','Spelling Correction',
            'Text Quality Prediction','Style Analysis','Predicting Speaker Characteristics','Authorship Attribution','Native Language Identification',
            'Lexicon and Paraphrase Induction','Mathematical Models','Biomedical','Social Science','Ethics','Multimodal Systems',
            'Modeling Human Language Processing','Computational Psycholinguistics','Modeling Human Language Acquisition'],

            ['Multilingual','Chinese','English','Malay', 'Hindi', 'Tamil', 'Urdu', 'Sanskrit', 'Japanese', 'Korean','Spanish', 'French', 'Portugese','Arabic','Hebrew','Semitic','Low-Resource Languages','Signed Languages','Child Language'],
            ['Scientific Literature','Literary Text','News','Encyclopedia','Biographies','Written Dialog',
            'Chat','Social Media','Non-private Unedited Text ','Twitter','Blogs','Spoken Dialog','Child-directed Speech','Child Language',
            'Other Spoken Genres','Human-Computer Interaction ','Query Logs','Biomedical Texts','Non-biomedical Scholarly Texts','Legal Documents ',
            'Legal Opinions','Clinical Notes','Web Crawl']]


@ns5.route('/get-data/<fos_link>')
class FOS_Data(Resource):
    @ns5.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self, fos_link):

        global subtopics

        if(fos_link=="linguistic"):
            fos_subtopics = subtopics[0]
            fos_heading = "Linguistic Target"
            search_name="linguistic"

        elif(fos_link=="approach"):
            fos_subtopics = subtopics[1]
            fos_heading = "Approach"
            search_name="approach"

        elif(fos_link=="task"):
            fos_subtopics = subtopics[2]
            fos_heading = "Task"
            search_name="task"

        elif(fos_link=="language"):
            fos_subtopics = subtopics[3]
            fos_heading = "Language"
            search_name="languages"

        elif(fos_link=="dataset"):
            fos_subtopics = subtopics[4]
            fos_heading = "Dataset"
            search_name="dataset_type"

        else:
            return {}
        data1 = list(papers.aggregate([{"$match":{"$nor":[{search_name:{"$exists":False}},{search_name:{"$size":0}}]}},{"$group":{"_id":"$year", "count":{"$sum":1}}}]))
        data2=list(papers.aggregate([{"$unwind":"$acl_author_name"},{"$match":{"$nor":[{search_name:{"$exists":False}},{search_name:{"$size":0}}]}},{"$group":{"_id":"$year","author_names":{"$addToSet":"$acl_author_name"}}},{"$project":{"_id":1,"author_count":{"$size":"$author_names"}}}]))
        data3=list(papers.aggregate([{"$match":{"$nor":[{search_name:{"$exists":False}},{search_name:{"$size":0}}]}},{"$group":{"_id":"$year", "count":{"$sum":"$total_citations"}}}]))
        data4 = list(papers.aggregate([{"$unwind":"$venue_name"},{"$match":{"$nor":[{search_name:{"$exists":False}},{search_name:{"$size":0}}]}},{"$group":{"_id":"$venue_name", "count":{"$sum":1}}},{"$sort":{"count":-1}}]))

        fos_ids=[]
        for fos in fos_subtopics:
            fos_id= '_'.join(fos.split(' ')).lower()
            fos_ids.append(fos_id)

        paper_distri = {"year":[], "paper_count":[]}
        author_distri = {"year":[], "author_count":[]}
        citation_distri = {"year":[], "citation_count":[]}
        conference_distri = {"conference":[],"topic_count":[]}


        for paper in data1: 
            try :
                paper_distri["year"].append(int(paper["_id"]))      
            except:
                paper_distri["year"].append("unknown")  
            paper_distri["paper_count"].append(int(paper["count"]))
        
        for author in data2:
            try:
                author_distri["year"].append(int(author["_id"]))
            except:
                author_distri["year"].append("unknown")

            author_distri["author_count"].append(int(author["author_count"]))

        for citation in data3:
            try:
                citation_distri["year"].append(int(citation["_id"]))
            except:
                citation_distri["year"].append("unknown")
            citation_distri["citation_count"].append(int(citation["count"]))


        for conference in data4:
            if(int(conference["count"])>30):
                try:
                    conference_distri["conference"].append(conference["_id"])
                except:
                    conference_distri["conference"].append("unknown")
                conference_distri["topic_count"].append(int(conference["count"]))

        return {"fos_link":fos_link,"fos_heading":fos_heading,"fos_ids":fos_ids,"fos_subtopics": fos_subtopics, "paper_distribution":paper_distri,"author_distribution":author_distri,"citation_distribution":citation_distri,
                "conference_distribution":conference_distri}

@ns5.route('/get-data/<fos_link>/<fos_ids>')
class FOS_Data(Resource):
    @ns5.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self, fos_link, fos_ids):
        if(fos_link=='linguistic'):
            fos_heading = "Linguistic Target"
            fos_link="linguistic"
            search_name="linguistic"
            field_name="$linguistic"
        elif(fos_link=='approach'):
            fos_heading = "Approach"
            fos_link="approach"
            search_name="approach"
            field_name="$approach"
        elif(fos_link=='task'):
            fos_heading = "Task"
            fos_link="task"
            search_name="task"
            field_name="$task"
        elif(fos_link=='language'):
            fos_heading = "Language"
            fos_link="language"
            search_name="languages"
            field_name="$languages"
        elif(fos_link=='dataset'):
            fos_heading = "Dataset"
            fos_link="dataset"
            search_name="dataset_type"
            field_name="$dataset_type"
        else:
            return {}
        
        send_fos_subtopic=''.join(fos_ids.split('_')).lower()
        fos_subtopics=' '.join(fos_ids.split('_')).title()
        tab_names = ["Authors","Papers","Conferences"]
    

        total_paper_mentions = list(papers.aggregate([{"$match":{search_name:send_fos_subtopic}},{"$count":"count"}]))
        min_year = list(papers.aggregate([{"$match":{search_name:send_fos_subtopic}},{"$group":{"_id":"null","minq":{"$min":"$year"}}}]))
        max_year=list(papers.aggregate([{"$match":{search_name:send_fos_subtopic}},{"$group":{"_id":"null","maxq":{"$max":"$year"}}}]))
        
        total_paper_mentions = total_paper_mentions[0]["count"]
        min_year=min_year[0]["minq"]
        max_year=max_year[0]["maxq"]

        graph_data = list(papers.aggregate([{"$match":{search_name:send_fos_subtopic}},{"$group":{"_id":"$year","count":{"$sum":1}}}]))
        data1 = list(papers.aggregate([{"$unwind":"$acl_author_name"},{"$unwind":field_name},{"$match":{search_name:send_fos_subtopic}},{"$group":{"_id":"$acl_author_name","count":{"$push":field_name}}},{"$project":{"_id":1,"freq":{"$sum":{"$size":"$count"}}}},{"$sort":{"freq":-1}},{"$limit":100}]))
        data2=list(papers.aggregate([{"$match":{search_name:send_fos_subtopic}},{"$project":{"year":1,"_id":1, "venue_name":1,"paper_title":1,"acl_author_name":1}},{"$sort":{"year":-1}},{"$limit":100}]))
        data3=list(papers.aggregate([{"$unwind":"$venue_name"},{"$unwind":field_name},{"$match":{search_name:send_fos_subtopic}},{"$group":{"_id":"$venue_name","count":{"$push":field_name}}},{"$project":{"_id":1,"freq":{"$sum":{"$size":"$count"}}}},{"$sort":{"freq":-1}},{"$limit":100}]))
        

        paper_mentions = {"year":[],"count":[]}
        author_list={"author_id":[],"author_names":[],"freq":[]}
        paper_list={'author_ids':[],'paper_id':[],'paper_title':[],'author_names':[],"year":[],"venue":[]}
        conference_list={"conference_name":[],"freq":[]}    
        for point in graph_data:
            try: 
                paper_mentions["year"].append(int(point["_id"]))    
            except:
                paper_mentions["year"].append("unknown")
            paper_mentions["count"].append(int(point["count"]))

        for author in data1:
            author_list["author_names"].append(author["_id"])
            author_list["freq"].append(author["freq"])
            author_list["author_id"].append(('-'.join(author["_id"].split(' ')).lower()))

        for paper in data2:
            paper_list['paper_id'].append(paper["_id"])
            try:
                paper_list['paper_title'].append(paper["paper_title"]) 
                paper_list["author_names"].append(paper["acl_author_name"])
                paper_list["year"].append(paper["year"])
                paper_list["venue"].append(paper["venue_name"])
                l=[]
                for author in paper["acl_author_name"]:
                    l.append('-'.join(author.split(' ')).lower())
                paper_list['author_ids'].append(l)
            except:
                pass

        for conference in data3:
            conference_list["conference_name"].append(conference["_id"])
            conference_list["freq"].append(conference["freq"])

        return {"fos_subtopics":fos_subtopics,
                "fos_heading":fos_heading,
                "tab_names":tab_names,
                "author_list":author_list,
                "paper_list":paper_list,
                "conference_list":conference_list,
                "paper_mentions":paper_mentions,
                "total_paper_mentions":total_paper_mentions,
                "min_year":min_year,
                "max_year":max_year,
                "fos_link":fos_link,
                "fos_ids":fos_ids}

@ns5.errorhandler(Exception)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database. Fos links can only be linguistic, approach, task, language, dataset"}, 500


@ns5.errorhandler(KeyError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database. Fos links can only be linguistic, approach, task, language, dataset"}, 500

@ns5.errorhandler(IndexError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500


"""
"""

@ns6.route('/get-search/<query>/<limit>')
class Search(Resource):
    @ns5.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self, query, limit):
        limit = int(limit)
        auth_items = []
        authors = author_es(query)
        for t in authors:
            temp = {"title" : t[1], "id" : t[0]}
            auth_items.append(temp)
        paper_items = paper_es(query)
        confs = conf_es(query)
        l = set()
        for conf in confs:
            for p in conf[0]:
                if query in p:
                    l.add((p, conf[1]))
        if list(l) == []:
            for conf in confs:
                for p in conf[0]:
                    if query.lower() in p.lower():
                        l.add((p, conf[1]))
        df = pd.read_csv('app/[IMP]for_url.csv')
        df_1 = df['Domain'].drop_duplicates()

        domains = df_1.str.find(query)
        df_df_1 = pd.concat([domains, df_1],axis=1)

        df_df_1.columns = ['Marker', 'Domain']
        domain_items = list(df_df_1[df_df_1['Marker'] != -1]['Domain'].dropna())
        df = pd.read_csv('app/for_fos.csv')
        df_1 = df['Topics'].drop_duplicates()

        domains = df_1.str.find(query)
        df_df_1 = pd.concat([domains, df_1],axis=1)

        df_df_1.columns = ['Marker', 'Domain']
        domains = list(df_df_1[df_df_1['Marker'] != -1]['Domain'].dropna())

        new = df[df['Topics'].isin(domains)]

        fos = []
        for a,b in zip(new['Topics'], new['Category']):
            fos.append((a.title(),b,'_'.join(a.split(' '))))
        papers = fulltextsearch(query)

        return {"authors": auth_items[:limit],
                "paper" : paper_items[:limit],
                "conferences" : list(l)[:limit],
                "domains" :  domain_items[:limit],
                "full_text" : papers[:limit]}

@ns6.errorhandler(Exception)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns6.errorhandler(KeyError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500

@ns6.errorhandler(IndexError)
def execption_handled(error):
    return {'message': "Internal Server Error: The following is most likely the result of incorrect paramters, or parameters which do not exist in the database"}, 500
