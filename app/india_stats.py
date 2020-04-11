from flask import Flask,render_template,request
import plotly 
import plotly.graph_objs as go
import pandas as pd
import json
import requests
import lxml.html as lh
import pandas as pd
import csv
import pandas as pd
import time
from datetime import datetime  
from datetime import timedelta  
global last_updated
app=Flask(__name__)

def df1():
    url='https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vSc_2y5N0I67wDU38DjDh35IZSIS30rQf7_NYZhtYYGU1jJYT6_kDx4YpF-qw0LSlGsBYP8pqM_a1Pd/pubhtml#'
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    # tr_elements = doc.xpath('//tr')
    col=[]
    i=0
    for t in tr_elements[1]:
        i+=1
        name=t.text_content()
        col.append((name,[]))

    for j in range(3,len(tr_elements)):
        T=tr_elements[j]
        if len(T)!=len(tr_elements[0]):
            continue
        i=0
        for t in T.iterchildren():
            data=t.text_content() 
            if i>0:
                try:
                    data=int(data)
                except:
                    pass
            col[i][1].append(data)
            i+=1
    Dict={title:column for (title,column) in col}
    df=pd.DataFrame(Dict)
    df.to_csv(r'states.csv', index = False)
    last_updated=datetime.now()
    return 
def df2():
    url="https://www.mohfw.gov.in/"
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    # tr_elements = doc.xpath('//tr')
    col=[]
    i=0
    for t in tr_elements[0]:
        i+=1
        name=t.text_content()
        col.append((name,[]))
    for j in range(1,len(tr_elements)):
        T=tr_elements[j]
        if len(T)!=5:
            continue
        i=0
        for t in T.iterchildren():
            data=t.text_content() 
            if i>0:
                try:
                    data=int(data)
                except:
                    pass
            col[i][1].append(data)
            i+=1
    Dict={title:column for (title,column) in col}
    df=pd.DataFrame(Dict)
    df.to_csv(r'india.csv', index = False)
    last_updated=datetime.now()
    return 

def show_tables():
    df = pd.read_csv('india.csv')
    x=list(df['Death'])
    y=list(df['Cured/Discharged/Migrated'])
    data = df
    data.set_index(['S. No.'], inplace=True)
    data.index.name=None
    return data.to_html(classes='female'),sum(x),sum(y)
    
def india(df):
    df = df[df['Detected State'].notna()]
    mp=[]
    total_count=[]
    count=0
    number=[]
    for i in range(len(df['Date Announced'])):
        if df['Detected State'][i]!='':
            count+=1
            mp.append(df['Date Announced'][i])
            number.append(count)
    dic=dict()
    for i in mp:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    day_count=list(dic.values())
    day=list(dic.keys())
    newday=[]
    for i in range(len(day)):
        newday.append(day[i][0:5])
    for i in range(len(day_count)):
        if i==0:
            total_count.append(day_count[i]+0)
        else:
            total_count.append(day_count[i]+total_count[i-1])
    data=[go.Scatter(x=newday, y=total_count,
                    mode='lines',
                    name='lineplot')]
    graphJSON=json.dumps(data,cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON,total_count[-1],day_count[-1]

def generate_graph(df,state):
    mp=[]
    total_count=[]
    count=0
    number=[]
    # state="Madhya Pradesh"
    for i in range(len(df['Detected State'])):
        if df['Detected State'][i]==state:
            count+=1
            mp.append(df['Date Announced'][i])
            number.append(count)
    dic=dict()
    for i in mp:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    day_count=list(dic.values())
    day=list(dic.keys())
    newday=[]
    for i in range(len(day)):
        newday.append(day[i][0:5])
    for i in range(len(day_count)):
        if i==0:
            total_count.append(day_count[i]+0)
        else:
            total_count.append(day_count[i]+total_count[i-1])
    data=[go.Scatter(x=newday, y=total_count,
                    mode='lines',
                    name='lineplot')]
    graphJSON=json.dumps(data,cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/stats', methods=['POST', 'GET'])
def indiastats():
    file1 = open("last_updated.txt","r")
    last_updated=file1.read()
    last_updated= datetime.strptime(last_updated, '%Y-%m-%d %H:%M:%S.%f')
    file1.close()
    if datetime.now()>last_updated + timedelta(days=0,minutes=60):
        df1()
        df2()
        file1 = open("last_updated.txt","w")
        file1.truncate(0)
        l=datetime.now()
        file1.write(str(l))
        file1.close()
    df = pd.read_csv('states.csv') 
    temp=india(df)
    total=temp[1]
    last_day=temp[2]
    temp2=show_tables()
    tab=temp2[0]
    deaths=temp2[1]
    rec=temp2[2]
    line=temp[0]
    line2=generate_graph(df,'Andhra Pradesh')
    line5=generate_graph(df,'Bihar')
    line9=generate_graph(df,'Delhi')
    line11=generate_graph(df,'Gujarat')
    line12=generate_graph(df,'Haryana')
    line14=generate_graph(df,'Jammu and Kashmir')
    line16=generate_graph(df,'Karnataka')
    line17=generate_graph(df,'Kerala')
    line20=generate_graph(df,'Madhya Pradesh') 
    line21=generate_graph(df,'Maharashtra') 
    line27=generate_graph(df,'Punjab') 
    line28=generate_graph(df,'Rajasthan')
    line29=generate_graph(df,'Tamil Nadu')
    line30=generate_graph(df,'Telangana')
    line32=generate_graph(df,'Uttar Pradesh')
    line34=generate_graph(df,'West Bengal')
    return render_template('indiacovid.html',last=last_day,plot=line,plot2=line2,plot5=line5,
                            plot9=line9,plot11=line11,plot12=line12,plot14=line14,plot16=line16,plot17=line17,
                            plot20=line20,plot21=line21,plot27=line27,plot28=line28,plot29=line29,plot30=line30,plot32=line32,
                            plot34=line34,totals=total,tables=tab,dead=deaths,recover=rec)


