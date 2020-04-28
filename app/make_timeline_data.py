import json
import csv
import re
from datetime import datetime
from .elasticSearch import paper_namefromid
from .index_data import _ner_filter
from .config import COLOR_MAP as color_map

def top_entities():
    # function to create json file with top 10 entities for each entity type
    print("Finding top entities...")
    d = {'ner_ched':[],
        'ner_dna':[],
        'ner_rna':[],
        'ner_protein':[],
        'ner_cell_line':[],
        'ner_cell_type':[]}
    named_ent_dict, _ = _ner_filter()
    for item in named_ent_dict:
        freq= len(named_ent_dict[item]['pids'])
        type = named_ent_dict[item]['type']
        d[type].append((freq,item))

    for type in d:
        d[type].sort(reverse=True)
        d[type] = d[type][:10]

    json.dump(d, open('top_entities.json','w'))

    return

def make_timeline_data_json():
    print("Making data for timelines...")
    ent_to_sha, _ = _ner_filter()
    timeline_ents = {}
    first_men = {}
    # first_men_mon = {}
    ent_type = {}
    # journal = {}
    # title = {}

    for item in ent_to_sha:
        #to remove noisy case
        if len(ent_to_sha[item]['pids']) < 10:
            continue

        y_min = datetime.now().date()
        for pid in ent_to_sha[item]['pids']:
            p = paper_namefromid(pid)
            try:
                y = datetime.strptime(p['ptime'][:7], '%Y-%m').date()
            except:
                try:
                    y = datetime.strptime(p['ptime'], '%Y').date()
                except:
                    continue
            if y <= y_min:
                y_min = y
                # first_paper = p['title']
                # journ = p['journ']
        first_men[item] = y_min.year
        # first_men_mon[item] = y_min
        ent_type[item] = ent_to_sha[item]['type']
        # title[item] = first_paper
        # journal[item] = journ

    print("No. of entities after removing noisy cases: "+str(len(first_men.keys())))

    for item in first_men:
        if first_men[item] in timeline_ents:
            timeline_ents[first_men[item]][ent_type[item]].append(item)
        else:
            timeline_ents[first_men[item]] = {'ner_ched':[],
                                            'ner_dna':[],
                                            'ner_rna':[],
                                            'ner_protein':[],
                                            'ner_cell_line':[],
                                            'ner_cell_type':[]}
            timeline_ents[first_men[item]][ent_type[item]].append(item)
        
    all_yrs = timeline_ents.keys()
    all_yrs = sorted(all_yrs)
    tl_dict = {}
    # tl_dict["title"] = {
    #     "heading" : "Explore when the entities were first discovered..."
    # }
    tl_dict["events"] = []

    types = {'ner_ched':'Chemical Entity', 
                'ner_dna':'DNA', 
                'ner_rna':'RNA',
                'ner_protein':'Protein', 
                'ner_cell_line':'Cell Line', 
                'ner_cell_type':'Cell Type'}

    
    for dt in all_yrs:

        d = {}
        d["start_date"] = {"year":str(dt)}
        
        html_mk = "<ul>"
        
        for t in types:
            if len(timeline_ents[dt][t])!=0:
                html_mk += "<li>"
                html_mk += "<h4>"+str(types[t])+"</h4>"
                html_mk += "<p>"
                
                for ent in timeline_ents[dt][t]:
                    html_mk += r"<a type=\"button\" style=\"margin-top:5px;margin-left:10px;color:"+color_map[t]+r" !important;\" class=\"btn btn-light\" href=\"/entity/"+str(ent_type[ent])+"/"+str(ent)+r"\">"+str(ent)+"</a></div>"

                html_mk += "</p>"
                html_mk += "</li>"

        html_mk += "</ul>"

        d["text"] = {
            "headline":str(dt),
            "text":html_mk
        }

        # d["background"] = {"url": r"\{\{url_for(\"static/images\", filename=\"virtual_bg.jpg\")\}\}"}

        tl_dict["events"].append(d)



    # # MAKING DATA FOR SEPARATE ENTITY TYPES
    # tl_types_dict = {}

    # for t in types:
    #     tl_types_dict[t] = {}
    #     tl_types_dict[t]["events"] = []

    # for ent in first_men_mon:
    #     d = {}
    #     d["start_date"] = {"year": str(first_men_mon[ent].year), "month": str(first_men_mon[ent].month)}
    #     html_mk = ""
    #     # html_mk += "Entity Type :" + str(types[ent_type[ent]]) 
    #     html_mk += r"<br><a type=\"button\" style=\"margin-top:5px;margin-left:10px;color:"+color_map[ent_type[ent]]+r" !important;\" class=\"btn btn-light\" href=\"/entity/"+str(ent_type[ent])+"/"+str(ent)+r"\">Click here for more info on this entity</a>"
    #     t = str(title[ent]).replace("'",r"\'")        
    #     t = t.replace('"',r'\"')
    #     html_mk += r"<h6>Published In \:</h6>" + t
    #     j = str(journal[ent]).replace("'",r"\'")
    #     j = j.replace('"',r'\"')
    #     html_mk += r"<h6>Journal \:</h6>" + j

    #     d["text"] = {
    #         "headline":str(ent),
    #         "text":html_mk
    #     }

        
        
    #     tl_types_dict[ent_type[ent]]["events"].append(d)



    #WRITE TO FILES

    json_obj_all = json.dumps(tl_dict, indent = 4)
    json_obj_all = re.sub(r'\n+', '', json_obj_all)

    # json_obj_types = {}
    # for t in types:
    #     temp = json.dumps(tl_types_dict[t], indent=4)
    #     json_obj_types[t] = re.sub(r'\n+', '', temp)
    #     temp = None

    with open("app/static/timeline-data-final.js",'w') as outfile:
        outfile.write("data_all = '"+ json_obj_all+"';\n")
    #     for t in types:
    #         outfile.write("data_"+str(t)+" = '"+ json_obj_types[t]+"';\n")

    return

