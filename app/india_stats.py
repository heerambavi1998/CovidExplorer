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
import math
from app import app
import plotly.express as px
import os
import zipfile
def df1():
#     os.system('cmd /c "kaggle datasets download -d sudalairajkumar/covid19-in-india"')
#     with zipfile.ZipFile('covid19-in-india.zip', 'r') as zip_ref:
#         zip_ref.extractall('statistics')
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
    df.to_csv(r'statistics/india.csv', index = False)
    last_updated=datetime.now()
    return 

def show_tables():
    df = pd.read_csv('statistics/india.csv')
    x=0
    
    for i in range(len(df['Deaths ( more than 70% cases due to comorbidities )'])):
        try :
            x+=int(df['Deaths ( more than 70% cases due to comorbidities )'][i])
        except:
            pass
    # x=list(df['Death'])
    y=list(df['Cured/Discharged/Migrated'])
    data = df
    data.set_index(['S. No.'], inplace=True)
    data.index.name=None
    return data.to_html(classes='female'),x,sum(y)
    
def india(df):
    df = df[df['State/UnionTerritory'].notna()]
    mp=[]
    total_count=[]
    count=0
    number=[]

    dic=dict()
    for i in range(len(df['Confirmed'])):
        if df['Date'][i] not in dic:
            dic[df['Date'][i]]=df['Confirmed'][i]
        else:
            dic[df['Date'][i]]+=df['Confirmed'][i]
    total_count=list(dic.values())
    day=list(dic.keys())
    newday=[]
    for i in range(len(day)):
        newday.append(day[i][0:5])
    day_count=[]
    day_count.append(total_count[0])
    for i in range(1,len(total_count)):
        day_count.append(total_count[i]-total_count[i-1])
    # print(day_count,total_count)
            
    data=[go.Scatter(x=newday, y=total_count,fill='tozeroy',
                    mode='lines+ markers',
                    name='lineplot',
                    line=dict(color='royalblue', width=3))]
    df1 = pd.DataFrame(list(zip(newday, day_count)), 
                columns =['Day', 'Daily_count'])
    fig = px.bar(df1, x='Day', y='Daily_count',
                color='Daily_count',
                labels={'Daily Cases in India'}, height=450)
    graphJSON1=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)                   
    graphJSON=json.dumps(data,cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON,total_count[-1],day_count[-1],graphJSON1

def india_deaths(df):
    df = df[df['State/UnionTerritory'].notna()]
    total_count=[]
    dic=dict()
    try:
        for i in range(len(df['Deaths'])):
            if df['Date'][i] not in dic:
                dic[df['Date'][i]]=int(df['Deaths'][i])
            else:
                dic[df['Date'][i]]+=int(df['Deaths'][i])
    except:
        pass
    total_count=list(dic.values())
    day=list(dic.keys())
    newday=[]
    for i in range(len(day)):
        newday.append(day[i][0:5])
#     print(total_count)
    day_count=[]
    day_count.append(total_count[0])
    for i in range(1,len(total_count)-1):
        day_count.append(total_count[i]-total_count[i-1])
#     print(day_count,total_count)
    data=[go.Scatter(x=newday, y=total_count,fill='tozeroy',
                    mode='lines+ markers',
                    name='lineplot',
                    line=dict(color='red', width=3))]
    df1 = pd.DataFrame(list(zip(newday, day_count)), 
                columns =['Day', 'Daily_count'])
    fig = px.bar(df1, x='Day', y='Daily_count',
                color='Daily_count',
                labels={'Daily Cases in India'}, height=450)
    graphJSON1=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)                   
    graphJSON=json.dumps(data,cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON,graphJSON1

def generate_graph(df,state):
    df = df[df['State/UnionTerritory'].notna()]
    mp=[]
    total_count=[]
    count=0
    number=[]

    dic=dict()
    for i in range(len(df['Confirmed'])):
        if df['State/UnionTerritory'][i]==state:
            if df['Date'][i] not in dic:
                dic[df['Date'][i]]=df['Confirmed'][i]
            else:
                dic[df['Date'][i]]+=df['Confirmed'][i]
    total_count=list(dic.values())
    day=list(dic.keys())
    newday=[]
    for i in range(len(day)):
        newday.append(day[i][0:5])
    day_count=[]
    day_count.append(total_count[0])
    for i in range(1,len(total_count)):
        day_count.append(total_count[i]-total_count[i-1])
    # print(day_count,total_count)
    data=[go.Scatter(x=newday, y=total_count,fill='tozeroy',
                    mode='lines+markers',
                    name='lineplot',
                    line=dict(color='royalblue', width=3))]

    graphJSON=json.dumps(data,cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/stats', methods=['POST', 'GET'])
def indiastats():
    file1 = open("statistics/last_updated.txt","r")
    last_updated=file1.read()
    last_updated= datetime.strptime(last_updated, '%Y-%m-%d %H:%M:%S.%f')
    file1.close()
    if datetime.now()>last_updated + timedelta(days=0,minutes=720):
        df1()
        df2()
        file1 = open("statistics/last_updated.txt","w")
        file1.truncate(0)
        l=datetime.now()
        file1.write(str(l))
        file1.close()
    df = pd.read_csv('statistics/covid_19_india.csv')
    
    temp5=india_deaths(df)
    tot_death_graph=temp5[0]
    daily_death_graphs=temp5[1]
    
    temp=india(df)
    line=temp[0]
    total=temp[1]
    last_day=temp[2]
    daily_c=temp[3]
    temp2=show_tables()
    tab=temp2[0]
    deaths=temp2[1]
    rec=temp2[2]
    acti=total-deaths-rec
    closed=rec+deaths
    recper=math.ceil(rec/closed*100)
    deadper=100-recper
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
    line30=generate_graph(df,'Telengana')
    line32=generate_graph(df,'Uttar Pradesh')
    line34=generate_graph(df,'West Bengal')
    return render_template('indiacovid.html',plot41=tot_death_graph,plot40=daily_death_graphs,daily=daily_c,last=last_day,plot=line,plot2=line2,plot5=line5,
                            plot9=line9,plot11=line11,plot12=line12,plot14=line14,plot16=line16,plot17=line17,
                            plot20=line20,plot21=line21,plot27=line27,plot28=line28,plot29=line29,plot30=line30,plot32=line32,
                            plot34=line34,totals=total,tables=tab,dead=deaths,recover=rec,active=acti,close=closed,recper=recper,
                            deadper=deadper)


