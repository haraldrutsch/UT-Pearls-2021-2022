import dash
# Using deprecated dash imports as they seem to work better
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
from local_json_parser import *
from counter import *
import multiprocessing as mp
import plotly.express as px

# <--- Global variables --->
# The dictionary used to store all the data used for the line chart
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

# This variable is used to store the next time frame index to look at
last_time_frame_index = 0

# The url where we retrieve our twitter data from
data_url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"

# The time interval at which the data is displayed, this is in seconds
time_interval = 60

# The labels for our graphs / all the sports keywords that were listed
labels = ['Baseball', 'Basketball', 'Voleyball', 'Tennis', 'Cricket', 'Soccer', 'Football', 'Rugby']

# Different colours for all the keywords that were listed
colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)', 'rgb(255,192,203)',
          'rgb(255,0,0)', 'rgb(255, 165,0)', 'rgb(0,128,0)']

# The width of the lines on the line chart
line_size = [2, 2, 2, 2, 2, 2, 2, 2]

# The time in seconds when the line chart is refreshed, among other function that are called
data_refresh_delay = 7

# The pie chart values are stored here
pie_values = []
# <--- Global variables --->

# An external style sheet is used
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# This declares the dash app and how it looks like. Using html code that is in python.
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        # Live analytics top text
        html.H4(children='LiveAnalytics', style={
            'textAlign': 'center',
            'color': '#000000',
            'font': 'Times New Roman'
        }),
        # Used for the refresh of the graphs
        html.Div(id='hacking-update-line'),
        # Declarations for the line chart
        dcc.Graph(id='live-update-graph'),
        # Used for the input of the threshold
        dcc.Input(id="threshold_input", type="number", placeholder="Write threshold percentage here", debounce=True,
                  style={
                      'textAlign': 'center',
                      'color': '#000000',
                      'font': 'Times New Roman'
                  }),
        # Used as the output for the text that is generated from the threshold input
        html.Div(id='threshold-output', style={
            'textAlign': 'center',
            'color': '#000000',
            'font': 'Times New Roman'
        }),
        # Declaration for the pie chart
        dcc.Graph(id='live-update-pie'),
        # This calls functions through app.callback if input is dcc.Interval
        # Calls the function every data_refresh_delay * 1000 milliseconds
        dcc.Interval(
            id='interval-component',
            interval=data_refresh_delay * 1000,  # in milliseconds
            n_intervals=0
        )
    ])
)


# This function is used to calculate the sports that have passed the threshold
@app.callback(Output("threshold-output", "children"), Input("threshold_input", "value"))
def update_threshold(n):
    # Declares the global values that are going to be used
    global pie_values
    global labels

    # Calculates the total number of tweets of sports in the current time frame
    pie_value_total = sum(pie_values)

    # Describes the style of the html.span below
    style = {'padding': '5px', 'fontSize': '16px'}

    sports_passing_threshold = ""
    x = 0

    # If the pie_values are empty we do not try to do the calculations as that results in an error
    if pie_values == []:
        return [
            html.Span('No values in pie chart yet', style=style),
        ]

    # Here we check which sports have passed the percentage threshold of amount of tweets from all tweets
    # We add them to a string and then we format that string into an html.span to be displayed
    for label in labels:
        if pie_values[x] / pie_value_total > n / 100:
            sports_passing_threshold = sports_passing_threshold + ", " + label
        x += 1

    return [
        html.Span('Sports that have reached threshold of {1}%: {0}'.format(sports_passing_threshold, n), style=style),
    ]


# This function is used to update the values used in the line and pie chart
@app.callback(Output('hacking-update-line', 'children'), Input('interval-component', 'n_intervals'))
def update_line_chart_back_end(n):
    # Declarations of all global variables in use
    global line_chart_data
    global last_time_frame_index
    global data_url
    global time_interval
    global pie_values

    # This is an implementation of multithreading that sometimes brakes
    # It does not have any real limits so don't use it
    # pool = mp.Pool(mp.cpu_count() - 1)
    # temp = pool.apply(counter_for_graph, (parser(data_url, time_interval, last_time_frame_index), time_interval - 1))
    # pool.close()

    # This gets the data we need and then advances the next time frame that we look at
    temp = counter_for_graph(parser(data_url, time_interval, last_time_frame_index), time_interval - 1)
    last_time_frame_index += 1

    # All the values for the line chart are appended
    line_chart_data['time'].append(convert_unix_to_time_date(temp[0][0]))
    line_chart_data['baseball'].append(temp[1][0])
    line_chart_data['basketball'].append(temp[2][0])
    line_chart_data['volleyball'].append(temp[3][0])
    line_chart_data['tennis'].append(temp[4][0])
    line_chart_data['cricket'].append(temp[5][0])
    line_chart_data['soccer'].append(temp[6][0])
    line_chart_data['football'].append(temp[7][0])
    line_chart_data['rugby'].append(temp[8][0])

    # All the pie chart values are appended
    pie_values = []
    pie_values.append(temp[1][0])
    pie_values.append(temp[2][0])
    pie_values.append(temp[3][0])
    pie_values.append(temp[4][0])
    pie_values.append(temp[5][0])
    pie_values.append(temp[6][0])
    pie_values.append(temp[7][0])
    pie_values.append(temp[8][0])


# This function is used to just refresh the pie chart using the current data in the global var pie_values
@app.callback(Output('live-update-pie', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_pie_live(n):
    # Declarations of all global variables in use
    global pie_values
    global labels

    # This describes the layout of the pie chart as a subplot
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.1)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    # If there are no values to plot then it defaults back to some default values until we get actual data
    if pie_values == []:
        fig = px.pie(values=[100, 100], names=['test', 'test1'])
    else:
        fig = px.pie(values=pie_values, names=labels)
    return fig


# This function is used to refresh the line chart
@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    # Declaration of global variables in use
    global line_chart_data

    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.1)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    # Adds traces for all the data that comes in
    # Traces need to be all on a new line and separate so that they are adding to the correct sport
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


# This starts the server in non-debug mode
# The regular address of the web server should be: http://127.0.0.1:8050/
if __name__ == '__main__':
    app.run_server(debug=False)
