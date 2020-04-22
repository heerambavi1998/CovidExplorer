# This file contains script to merge and filter NEs obtained through different NER systems
# such as SciBert, Saber.
# Redundant entities are filtered out

import csv

def _format_ne(ne):
    l = ne.split(';')
    l_1 = [i.strip() for i in l if len(i)>1]
    return l_1

# removing Capitalised entities for multiple occuring entities
entities = {}

with open('ent_from_scibert_JNLPBA.csv', newline='') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        for i in range(1,6):
            nes = _format_ne(row[i])
            for ne in nes:
                if ne.lower() in entities:
                    entities[ne.lower()].append(ne)
                else:
                    entities[ne.lower()] = [ne]

ched_sha_ent = {}
with open('ched_from_abs_comb.csv', newline='') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        ched_sha_ent[row[0]] = row[1]
        nes = _format_ne(row[1])
        for ne in nes:
            if ne.lower() in entities:
                entities[ne.lower()].append(ne)
            else:
                entities[ne.lower()] = [ne]

for ent in entities:
    mode = max(entities[ent], key=entities[ent].count)
    entities[ent] = mode

# writing these entities to a new csv
f2 = open('ners.csv','w')
writer = csv.writer(f2)
with open('ent_from_scibert_JNLPBA.csv', newline='') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        l = [row[0]]
        for i in range(1,6):
            nes = _format_ne(row[i])
            new_nes = ''
            for ne in nes:
                new_nes += entities[ne.lower()]
                new_nes += ';'
            l.append(new_nes)
        if row[0] in ched_sha_ent:
            nes = _format_ne(ched_sha_ent[row[0]])
            new_nes = ''
            for ne in nes:
                new_nes += entities[ne.lower()]
                new_nes += ';'
            l.append(new_nes)
        else:
            l.append('')
        writer.writerow(l)
