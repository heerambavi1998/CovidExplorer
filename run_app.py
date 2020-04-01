from app import app
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

app=Flask(__name__)

def generate_graph():
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
        if len(T)!=26:
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
    mp=[]
    total_count=[]
    count=0
    number=[]
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
    for i in range(len(day_count)):
        if i==0:
            total_count.append(day_count[i]+0)
        else:
            total_count.append(day_count[i]+total_count[i-1])
    # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    data=[go.Scatter(x=day, y=day_count,
                    mode='lines',
                    name='lineplot')]
    graphJSON=json.dumps(data,cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON 


@app.route('/',methods=['POST','GET'])
def index():
    line=generate_graph()
    return render_template('index.html',plot=line)




if __name__=='__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)
