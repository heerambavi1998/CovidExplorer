import os
import subprocess
from datetime import datetime

def add_cronjob():
    # add cronjob
    cmd = '''touch /var/spool/cron/covid19;
/usr/bin/crontab /var/spool/cron/covid19;
echo "0 5 * * mon ~/web-dir/system/cronscript.sh" > /var/spool/cron/covid19'''
    os.system(cmd)

    #check using crontab -u covid19 -l
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

    _, err = run('unzip -oq CORD-19-research-challenge.zip -d ~/web-dir/data')
    if err != '':
        print('Error in unzipping dataset: %s' %err)
        
    _, err = run('python3 ~/web-dir/system/run_scibertNER.py')
    if err != '':
        print('Error in extracting entities: %s' %err)
        
    _, err = run('python3 ~/web-dir/app/merge_ner_csv.py')
    if err != '':
        print('Error in merging entity files: %s' %err)
    
    currtime = datetime.now()
    _, err = run('touch ~/web-dir/system/time.txt; echo "%s" >> ~/web-dir/system/time.txt' %currtime)
