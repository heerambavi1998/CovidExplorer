from allennlp.predictors import Predictor
from datetime import datetime
import csv
import numpy as np
import sys

METADATAPATH = "/home/covid19/web-dir/data/metadata.csv"

#different tags: 
#DNA, RNA, protein, cell_line, cell_type
#B-begin, I-inside, L-last, U-unit

if sys.argv[1] == 'JNLPBA':
    MODELPATH = "/home/covid19/web-dir/system/scibert_ner_model_JNLPBA/model.tar.gz"
    FILEPATH = "/home/covid19/web-dir/ent_from_scibert_JNLPBA.csv"
    all_ents = ["DNA", "RNA", "protein", "cell_line", "cell_type"]
elif sys.argv[1] == 'NCBI':
    MODELPATH = "/home/covid19/web-dir/system/scibert_ner_model_NCBI-disease/model.tar.gz"
    FILEPATH = "/home/covid19/web-dir/ent_from_scibert_NCBI-disease.csv"
    all_ents = ["Disease"]
else:
    print("Error in argument")

#Load the NER model
predictor = Predictor.from_path(MODELPATH)

#Function to format cells with multiple paper IDs
def _format_pid(pid):
  l = pid.split(';')
  l_1 = [i.strip() for i in l]
  return l_1

def list2text(list_ent):
    ents = list(set(list_ent))
    if len(ents) == 0: #empty list
        return ""
    t = ";".join(ents)
    return t

with open(METADATAPATH, newline="") as read_file:
    f = csv.DictReader(read_file)
    with open(FILEPATH, mode='w') as write_file:
        writer = csv.writer(write_file)
        print("Extraction start...")
        time_list = []
        j=0
        for row in f:
            j+=1
#             print("on doc "+str(j))
            start = datetime.now()

            #check fulltext validity
            if row['pdf_json_files'] != '':
                pids = row['sha']
            elif row['pmc_json_files'] != '':
                pids = row['pmcid']
            else:
                continue

            #Extract entities
            try:
                res = predictor.predict(sentence=row['abstract'])
                ents = {}
                for ent in all_ents:
                    ents[ent] = []
                words = res["words"]
                tags = res["tags"]
                i = 0
                while i < len(tags):
                    if tags[i] == "O":
                        i += 1
                        continue
                    if tags[i][0] == "U":
                        ents[tags[i][2:]].append(words[i])
                        i += 1
                        continue
                    if tags[i][0] == "B":
                        ent = words[i]
                        while (tags[i][0] != "L"):
                            i += 1
                            ent+=" " + words[i]
                        ents[tags[i][2:]].append(ent)
                        i += 1
                        continue
                ent_texts = [list2text(ents[t]) for t in all_ents]
            except:
                ent_texts = ["" for t in all_ents]
                print("Error in doc "+str(j)+" of "+str(pids))

            #write to csv
            for pid in _format_pid(pids):
                row = [pid] + ent_texts
                writer.writerow(row)

        end = datetime.now()
        time_taken = end-start
#             print("Time: "+str(time_taken))
        time_list.append(time_taken)

    print("Extraction Complete...")
    print("Average time per doc: "+str(np.mean(time_list)))
                
