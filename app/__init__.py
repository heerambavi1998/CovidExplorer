from flask import Flask
from .config import * 

from elasticsearch import Elasticsearch
ES_CLIENT = Elasticsearch([{'host':'localhost','port':ES_PORT}]) # ES indexing

from app import index_data 



app = Flask(__name__)

app.config['SECRET_KEY'] = "96e16ccf34694cc691a8c284919ab2e7d3daafbdb9407c90"





if not ES_CLIENT.indices.exists(index='covid19_fulltext'):
    index_data.index_fulltext(ES_CLIENT, METADATAPATH, DATAPATHS, 'covid19_fulltext')

if not ES_CLIENT.indices.exists(index='covid19_authors'):
    index_data.index_authorsfromMD(ES_CLIENT, METADATAPATH, 'covid19_authors')

if not ES_CLIENT.indices.exists(index='covid19_ner'): #need fulltext index made before this
    index_data.index_named_entities(ES_CLIENT, NERDATAPATH, 'covid19_ner')

if not ES_CLIENT.indices.exists(index='covid19_ched'): #need fulltext index made before this
    index_data.index_named_entities(ES_CLIENT, CHEDDATAPATH, 'covid19_ched')

from app import routes, author_routes,india_stats,network_dash