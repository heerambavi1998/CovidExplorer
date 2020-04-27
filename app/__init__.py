from flask import Flask
from .config import * 
import time
from elasticsearch import Elasticsearch
ES_CLIENT = Elasticsearch([{'host':'localhost','port':ES_PORT}]) # ES indexing

from app import index_data, make_timeline_data 
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = "96e16ccf34694cc691a8c284919ab2e7d3daafbdb9407c90"





if not ES_CLIENT.indices.exists(index='covid19_fulltext'):
    index_data.index_fulltext(ES_CLIENT, METADATAPATH, DATAPATHS, 'covid19_fulltext')

if not ES_CLIENT.indices.exists(index='covid19_authors'):
    index_data.index_authorsfromMD(ES_CLIENT, METADATAPATH, 'covid19_authors')

if not ES_CLIENT.indices.exists(index='covid19_ner'): #need fulltext index made before this
    index_data.index_named_entities(ES_CLIENT, 'covid19_ner')

if not os.path.exists('app/static/timeline-data-final.js'):
    make_timeline_data.make_timeline_data_json()

if not os.path.exists('/top_entities.json'):
    make_timeline_data.top_entities()


from app import routes, author_routes,india_stats,network_dash,sanky_dash, entity_routes