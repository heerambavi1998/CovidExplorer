from flask import Flask
from elasticsearch import Elasticsearch
from app import index_data
from .config import *


app = Flask(__name__)

app.config['SECRET_KEY'] = "96e16ccf34694cc691a8c284919ab2e7d3daafbdb9407c90"


# ES indexing
ES_CLIENT = Elasticsearch([{'host':'localhost','port':ES_PORT}])


if not ES_CLIENT.indices.exists(index='covid19_fulltext'):
    for path in DATAPATHS:
        index_data.index_fulltext(ES_CLIENT, path, 'covid19_fulltext')

if not ES_CLIENT.indices.exists(index='covid19_authorz'):
    index_data.index_authors(ES_CLIENT, DATAPATHS, 'covid19_authorz')

from app import routes, author_routes