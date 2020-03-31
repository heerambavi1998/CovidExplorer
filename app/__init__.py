from flask import Flask
from elasticsearch import Elasticsearch
from app import index_data
from .config import *


app = Flask(__name__)

app.config['SECRET_KEY'] = "96e16ccf34694cc691a8c284919ab2e7d3daafbdb9407c90"


# ES indexing
ES_CLIENT = Elasticsearch([{'host':'localhost','port':ES_PORT}])


if not ES_CLIENT.indices.exists(index='covid19_fulltext'):
    index_data.index_fulltext(ES_CLIENT, METADATAPATH, DATAPATHS, 'covid19_fulltext')

if not ES_CLIENT.indices.exists(index='covid19_authors'):
    index_data.index_authorsfromMD(ES_CLIENT, METADATAPATH, 'covid19_authors')

from app import routes, author_routes