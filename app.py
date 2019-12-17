# from flask import Flask
# import os
# app = Flask(__name__)
# port = int(os.environ.get("PORT", 5000))

# @app.route('/')
# def hello_world():
#     return 'Flask Dockerized and deployed to Heroku'

# if __name__ == '__main__':
#     app.run(debug=True,host='0.0.0.0',port=port)

import dash
import dash_core_components as dcc
import dash_html_components as html
import os
port = int(os.environ.get("PORT", 5000))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=port)