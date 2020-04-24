# urls : graphs/sanky/entity={{ent_name}}&ent_type={{ent_type}}
from app import app
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import urllib
from .networks import create_sanky
from .config import DASHURL


url_base = DASHURL+'sanky/'

graph = dash.Dash(
    __name__,
    server=app,
    routes_pathname_prefix=url_base,
)
graph.config.suppress_callback_exceptions = True
graph.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    #html.Div([html.H1("People")], className="row", style={'textAlign': "center"}),
    html.Div([dcc.Graph(id="my-graph", )]),], className="container")

@graph.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input('url', 'pathname')])
def update_sanky(url):

    config = dict(urllib.parse.parse_qsl(url.strip('/')))
    gene = config['graphs/sanky/entity']
    #ent_type = config['ent_type']
    data = create_sanky(gene)
    figure = go.Figure(data=[go.Sankey(
        arrangement="snap",
        orientation='h',
        #valueformat=".0f",
        #valuesuffix="TWh",
        node=dict(
            pad=30,
            thickness=15,
            line=dict(color="black", width=0.5),
            label=data['label']
            #color=data['data'][0]['node']['color']
        ),
        link=dict(
            source=data['source'],
            target=data['target'],
            value=data['value'],
            #label=data['data'][0]['link']['label']
        ))])

    figure.update_layout(
        hovermode='x',
        title="%s" %gene,
        font=dict(size=12, color='white'),
        height=1000,
    )

    return figure
