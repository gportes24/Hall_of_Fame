import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Baseball Stats from the 1980s"
mytitle = "Batting Averages for 4 Hall of Famers"
x_values = ['1984', '1985', '1986', '1987', '1988', '1989']
y1_values = [293, 314, 263, 291, 305, 274]
y2_values = [325, 368, 357, 363, 366, 330]
y3_values = [296, 288, 328, 332, 356, 339]
y4_values = [351, 317, 329, 370, 313, 336]
color1 = '#189716'
color2 = '#EF0C29'
color3 = '0C94EF'
color4 = '#544338'
name1 = 'Rickey Henderson'
name2 = 'Wade Boggs'
name3 = 'Kirby Puckett'
name4 = 'Tony Gwinn'
tabtitle = 'baseball'
sourceurl = 'https://www.baseball-reference.com'
githublink = 'https://github.com/austinlasseter/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
    
trace3 = go.Scatter(
    x = x_values,
    y = y4_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name4
)

# assign traces to data
data = [trace0, trace1, trace2, trace3]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
