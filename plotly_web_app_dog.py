import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
from parserUT import *
import pandas
import plotly.graph_objects as go
from counter import *

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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H4('LiveAnalytics'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=5*1000, # in milliseconds
            n_intervals=0
        )
    ])
)


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
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
    temp = counter_for_graph(parser(data_url, time_interval, last_time_frame_index), time_interval - 1)
    last_time_frame_index += 1

    line_chart_data['time'].append(convert_unix_to_time_date(temp[0][0]))
    line_chart_data['baseball'].append(temp[1][0])
    line_chart_data['basketball'].append(temp[2][0])
    line_chart_data['volleyball'].append(temp[3][0])
    line_chart_data['tennis'].append(temp[4][0])
    line_chart_data['cricket'].append(temp[5][0])
    line_chart_data['soccer'].append(temp[6][0])
    line_chart_data['football'].append(temp[7][0])
    line_chart_data['rugby'].append(temp[8][0])

    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.1)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace({
        'x': line_chart_data['time'],
        'y': line_chart_data['baseball'],
        'name': 'baseball',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': line_chart_data['time'],
        'y': line_chart_data['basketball'],
        'name': 'basketball',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': line_chart_data['time'],
        'y': line_chart_data['volleyball'],
        'name': 'volleyball',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': line_chart_data['time'],
        'y': line_chart_data['tennis'],
        'name': 'tennis',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': line_chart_data['time'],
        'y': line_chart_data['cricket'],
        'name': 'cricket',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': line_chart_data['time'],
        'y': line_chart_data['soccer'],
        'name': 'soccer',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': line_chart_data['time'],
        'y': line_chart_data['football'],
        'name': 'football',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': line_chart_data['time'],
        'y': line_chart_data['rugby'],
        'name': 'rugby',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
