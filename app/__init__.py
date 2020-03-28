from flask import Flask
from elasticsearch import Elasticsearch
from app import fulltextsearch
from .config import *


app = Flask(__name__)

app.config['SECRET_KEY'] = "96e16ccf34694cc691a8c284919ab2e7d3daafbdb9407c90"


# ES indexing
ES_CLIENT = Elasticsearch([{'host':'localhost','port':ES_PORT}])


if not ES_CLIENT.indices.exists(index='test'):
    fulltextsearch.index_fulltext_search(ES_CLIENT, DATAPATH, 'test')

from app import routes