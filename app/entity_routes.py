from flask import render_template
import json
from app import app
from .config import ENT_TYPES
from.helper import get_ent_type_name


ent_types = {}
for t in ENT_TYPES:
    ent_types[t] = get_ent_type_name(t)
@app.route('/ner_all', methods=["GET", "POST"])
def ne_all():
    return render_template('named_entities_all.html', ent_types=ent_types)

@app.route('/ner_all/<ent_type>', methods=["GET", "POST"])
def ne_type(ent_type):
    with open('top_entities.json') as f:
        ent = json.load(f)
    return render_template('named_entity_type_pg.html', ent_type=ent_types[ent_type],
                           ent_types=ent_types, top_entities=ent[ent_type])