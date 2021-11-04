import plotly.graph_objects as go
import numpy as np
import dash
from dash import html
from dash import dcc
import pandas
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets) 
labels = ['Baseball', 'Basketball', 'Voleyball', 'Tennis', 'Cricket', 'Soccer', 'Football', 'Rugby']
values = [4500, 2500, 1053, 500, 200, 300, 150, 2000]

title = 'Twente Analytica'
labels = ['Baseball', 'Basketball', 'Voleyball', 'Tennis', 'Cricket', 'Soccer', 'Football', 'Rugby']
colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)', 'rgb(255,192,203)', 'rgb(255,0,0)', 'rgb(255, 165,0)', 'rgb(0,128,0)']

mode_size = [8, 8, 8, 8, 8, 8, 8, 8]
line_size = [2, 2, 2, 2, 2, 2, 2, 2]

x_data = np.vstack((np.arange(2001, 2014),)*8)

y_data = np.array([
    [74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 100],
    [45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28],
    [13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
    [18, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 40],
    [50, 31, 27, 76, 30, 10, 62, 55, 40, 22, 12, 80],
    [25, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 55],
    [37, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 45],
    [10, 19, 20, 21, 16, 14, 11, 18, 17, 20, 39, 25],
])

#Pie chart
fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                             insidetextorientation='radial'
                            )])
#Line chart
fig = go.Figure()
for i in range(0, 8):
    fig.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
        name=labels[i],
        line=dict(color=colors[i], width=line_size[i]),
        connectgaps=True,
    ))
    # endpoints
    #fig.add_trace(go.Scatter(
    #    x=[x_data[i][0], x_data[i][-1]],
    #    y=[y_data[i][0], y_data[i][-1]],
    #    mode='markers',
    #    marker=dict(color=colors[i], size=mode_size[i])
    #))

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid= False,
        zeroline=False,
        showline=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',)

    ),)
    #autosize=False,
    #margin=dict(
    #    autoexpand=True
    #    l=100,
    #    r=20,
    #    t=110,
    #),
    #showlegend=True,
    #plot_bgcolor='white'
#)

annotations = []

# Adding labels
#for y_trace, label, color in zip(y_data, labels, colors):
    # labeling the left_side of the plot
#    annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
#                                  xanchor='right', yanchor='middle',
#                                  showarrow=True))
    # labeling the right_side of the plot

fig.update_layout(annotations=annotations)

app.layout =html.Div([
    html.Div(style = {
    'backgroundColor': '#FFFFFF'}, 
    children = [
        html.H1(
        children = 'Twente Analytica',
        style = {
        'textAlign': 'center',
        'color': '#000000'}),
    html.Div([
        html.H3(
        children = 'Line Chart',
        style = {
        'textAlign': 'center',
        'color': '#000000',
        'font': 'Times New Roman'}),
            dcc.Graph(
                id = 'example-graph-2',
                figure = fig,
                style = {
                'height': 500,
                'width': 750,
                "display": "inline-block",
                "margin-top": "auto",
                "margin-left": "",
                "margin-right": ""
                }),
    ], className= "seven columns"),
    html.Div([
        html.H3(
        children = 'Popularity',
        style = {
        'textAlign': 'center',
        'color': '#000000'}),
            dcc.Graph(
                id='pie1',
                figure= fig1,
                style = {
                'height': 500,
                'width': 600,
                "display": "",
                "margin-left": "",
                "margin-right": ""
                },),
        ], className= "seven columns"),
    ], className= "container")
])
if __name__ == '__main__':
  app.run_server(debug = True)
fig.show()
fig1.show()
