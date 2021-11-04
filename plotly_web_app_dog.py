import datetime

import dash
from dash import html
from dash import dcc
import plotly
from dash.dependencies import Input, Output
from parserUT import *
import pandas
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Global variables
line_chart_data = {
    'time': [],
    'baseball': [],
    'basketball': [],
    'volleyball': [],
    'tennis': [],
    'cricket': [],
    'soccer': [],
    'football': [],
    'rugby': []
}

last_time_frame_index = 0
data_url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"
time_interval = 10 * 60
labels = ['Baseball', 'Basketball', 'Voleyball', 'Tennis', 'Cricket', 'Soccer', 'Football', 'Rugby']
colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)', 'rgb(255,192,203)',
          'rgb(255,0,0)', 'rgb(255, 165,0)', 'rgb(0,128,0)']
mode_size = [8, 8, 8, 8, 8, 8, 8, 8]
line_size = [2, 2, 2, 2, 2, 2, 2, 2]
# Global variables


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(style={
        'backgroundColor': '#FFFFFF'},
        children=[
            html.H1(
                children='Twente Analytica',
                style={
                    'textAlign': 'center',
                    'color': '#000000'}),
            html.Div([
                html.H3(
                    children='Line Chart',
                    style={
                        'textAlign': 'center',
                        'color': '#000000',
                        'font': 'Times New Roman'}),
                dcc.Graph(
                    id='line_chart_main',
                    figure=fig,
                    style={
                        'height': 500,
                        'width': 750,
                        "display": "inline-block",
                        "margin-top": "auto",
                        "margin-left": "",
                        "margin-right": ""
                    }),
                dcc.Interval(
                    id='interval_line_chart_main',
                    interval=1 * 1000,  # in milliseconds
                    n_intervals=0
                ),
            ], className="seven columns"),
            '''
            html.Div([
                html.H3(
                    children='Popularity',
                    style={
                        'textAlign': 'center',
                        'color': '#000000'}),
                dcc.Graph(
                    id='pie_chart_main',
                    figure=fig1,
                    style={
                        'height': 500,
                        'width': 600,
                        "display": "",
                        "margin-left": "",
                        "margin-right": ""
                    }, ),
                dcc.Interval(
                    id='interval_pie_chart_main',
                    interval=1 * 1000,  # in milliseconds
                    n_intervals=0
                ),
            ], className="seven columns"),
            '''
        ], className="container")
])


# Multiple components can update everytime interval gets fired.
@app.callback(Output('line_chart_main', 'figure'),
              Input('interval_line_chart_main', 'n_intervals'))
def update_graph_live(n):
    global line_chart_data
    global last_time_frame_index
    global data_url
    global time_interval
    global labels
    global colors
    global mode_size
    global line_size

    # Collect some data
    temp = parser(data_url, time_interval, last_time_frame_index)
    last_time_frame_index += 1

    line_chart_data['time'].append(temp[0][0])
    line_chart_data['baseball'].append(temp[1][0])
    line_chart_data['basketball'].append(temp[2][0])
    line_chart_data['volleyball'].append(temp[3][0])
    line_chart_data['tennis'].append(temp[4][0])
    line_chart_data['cricket'].append(temp[5][0])
    line_chart_data['soccer'].append(temp[6][0])
    line_chart_data['football'].append(temp[7][0])
    line_chart_data['rugby'].append(temp[8][0])

    # Create the graph with subplots
    #fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    #fig['layout']['margin'] = {
    #    'l': 30, 'r': 10, 'b': 30, 't': 10
    #}
    #fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    for n in range(1, 8):
        fig.append_trace(go.Scatter(x=line_chart_data['time'][last_time_frame_index],
                                    y=line_chart_data[n][last_time_frame_index],
                                    mode='lines',
                                    line=dict(color=colors[n], width=line_size[n]),
                                    connectgaps=True))

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
            showgrid=False,
            zeroline=False,
            showline=True,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)', )

        ), )

    fig.update_layout(annotations=annotations)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
