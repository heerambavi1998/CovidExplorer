import os
import sys
import subprocess
from datetime import datetime
from elasticsearch import Elasticsearch
from app import index_data,make_timeline_data
from app.config import *

def add_cronjob():
    # add cronjob
    cmd = '''touch /var/spool/cron/covid19;
/usr/bin/crontab /var/spool/cron/covid19;
echo "0 5 * * mon ~/web-dir/system/cronscript.sh" > /var/spool/cron/covid19'''
    os.system(cmd)

    #check using crontab -u covid19 -l
    # check /var/mail/covid19
    return

def run(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out.decode('utf-8'), err.decode('utf-8')


if __name__ == '__main__':

    print('Downloading data.......')
    kag_cmd = "kaggle datasets download -d allen-institute-for-ai/CORD-19-research-challenge\n"
    _, err = run(kag_cmd)
    if err != '':
        print('Error in downloading dataset: %s' %err)
        #sys.exit()

    _, err = run('unzip -oq CORD-19-research-challenge.zip -d ~/web-dir/data')
    if err != '':
        print('Error in unzipping dataset: %s' %err)
        #sys.exit()

    currtime = datetime.now()
    run('touch ~/web-dir/system/time.txt; echo "last data dwnld: %s" >> ~/web-dir/system/time.txt' % currtime)

    print('Deleting zip.......')
    run('rm CORD-19-research-challenge.zip')

    #run NER
    print('Running JNLPBA sciBERT NER.......')
    _, err = run('python3 ~/web-dir/system/run_scibertNER.py JNLPBA')
    if err != '':
        print('Error in extracting entities: %s' %err)

        
    print('Running NCBI-disease sciBERT NER.......')
    _, err = run('python3 ~/web-dir/system/run_scibertNER.py NCBI')
    if err != '':
        print('Error in extracting entities: %s' %err)

        
    _, err = run('python3 ~/web-dir/app/merge_ner_csv.py')
    if err != '':
        print('Error in merging entity files: %s' %err)
        #sys.exit()

    # reindex data
    ES_CLIENT = Elasticsearch([{'host': 'localhost', 'port': ES_PORT}])
    print('Deleting current fulltext index.......')
    _, err = run('curl -XDELETE localhost:9210/covid19_fulltext')
    if err != '':
        print('Error in deleting fulltext index: %s' %err)
    print('Adding new fulltext index.......')
    index_data.index_fulltext(ES_CLIENT, METADATAPATH, DATAPATHS, 'covid19_fulltext')

    print('Deleting current authors index.......')
    _, err = run('curl -XDELETE localhost:9210/covid19_authors')
    if err != '':
        print('Error in deleting author index: %s' %err)
    print('Adding new author index.......')
    index_data.index_authorsfromMD(ES_CLIENT, METADATAPATH, 'covid19_authors')

    print('Deleting current ner index.......')
    _, err = run('curl -XDELETE localhost:9210/covid19_ner')
    if err != '':
        print('Error in deleting ner index: %s' %err)
    print('Adding new ner index.......')
    index_data.index_named_entities(ES_CLIENT, 'covid19_ner')

    print('Indexing DONE.......')

    #save last indexed time
    currtime = datetime.now()
    run('touch ~/web-dir/system/time.txt; echo "last indexing: %s" >> ~/web-dir/system/time.txt' % currtime)

    #creating timelines
    print('Creating timelines.......')
    make_timeline_data.make_timeline_data_json()
    print('Writing top_entities.json.......')
    make_timeline_data.top_entities()

    #ADD any additional steps here


    # save last update time
    currtime = datetime.now()
    run('touch ~/web-dir/system/time.txt; echo "last update finished at: %s" >> ~/web-dir/system/time.txt' % currtime)
