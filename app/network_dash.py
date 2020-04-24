# urls : graphs/network/entity={{ent_name}}&ent_type={{ent_type}}
from app import app
import networkx as nx
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import urllib
import math
from .networks import create_network
from .config import DASHURL


url_base = DASHURL+'network/'

graph = dash.Dash(
    __name__,
    server=app,
    routes_pathname_prefix=url_base,
)

graph.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    #html.Div([html.H1("People")], className="row", style={'textAlign': "center"}),
    html.Div([dcc.Graph(id="my-graph", )]),], className="container")


@graph.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input('url', 'pathname')])
def update_graph(url):

    config = dict(urllib.parse.parse_qsl(url.strip('/')))
    gene = config['graphs/network/entity']
    ent_type = config['ent_type']
    G = create_network(gene, ent_type)
    pos = nx.spring_layout(G, k=3 / math.sqrt(len(G.nodes())), seed=3)

    # Add edges as disconnected lines in a single trace
    edge_trace = go.Scatter(x=[], y=[], line={'width': 1, 'color': '#888'}, hoverinfo='none', mode='lines')
    list_edge_trace_x = list(edge_trace['x'])
    list_edge_trace_y = list(edge_trace['y'])
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        list_edge_trace_x.extend(tuple([x0, x1, None]))
        list_edge_trace_y.extend(tuple([y0, y1, None]))

    edge_trace['x'] = tuple(list_edge_trace_x)
    edge_trace['y'] = tuple(list_edge_trace_y)
    # Add nodes as a scatter trace
    node_trace = go.Scatter(x=[], y=[], text=[], mode='markers', hoverinfo='text',
                            marker={'showscale': True, 'colorscale': 'Jet', 'reversescale': True, 'color': [],'size':20,
                                    'colorbar': {'thickness': 10, 'title': 'Paper', 'xanchor': 'left',
                                                 'titleside': 'right'},
                                    'line': {'width': 2}})
    list_node_trace_x = list(node_trace['x'])
    list_node_trace_y = list(node_trace['y'])
    for node in G.nodes():
        x, y = pos[node]
        list_node_trace_x.extend(tuple([x]))
        list_node_trace_y.extend(tuple([y]))

    node_trace['x'] = tuple(list_node_trace_x)
    node_trace['y'] = tuple(list_node_trace_y)

    # add color by community and size by degree.
    communities = nx.get_node_attributes(G, 'community')
    for node in G.nodes():
        node_trace['text'] += tuple([node])
        node_trace['marker']['color'] += tuple([communities[node]])

    figure = {"data": [edge_trace, node_trace],
              "layout": go.Layout(title='Co-mentions for %s by paper' %gene, showlegend=False, hovermode='closest',
                                  margin={'b': 20, 'l': 5, 'r': 5, 't': 40},
                                  xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                                  yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False})}
    return figure

