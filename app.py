import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, page_registry, page_container
from dash.dependencies import Input, Output
from datetime import date

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)


sidebar = html.Div(
    [
        html.H5("Astronomical ephemerides for the ancient world"),
        html.Hr(),
            dbc.Nav(
            [
                dbc.NavLink(page['name'], href=page['path']) 
                for page in page_registry.values()
        ],
        vertical=True,
        pills=True,
        )
    ]
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Montu App",
                         style={'fontSize':50, 'textAlign':'center', 'background-color': '#DED18D', 'font-weight': 'bold'}))
    ]),
    html.Hr(style={'background-color': '#DED18D'}),
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)

"""
https://github.com/fnneves/callbacks-tutorial/blob/main/Callbacks_Tutorial.ipynb
https://www.youtube.com/watch?v=uzosQuETMKo
https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Bootstrap/Side-Bar/side_bar.py
https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Dash_More_Advanced_Stuff/Intro%20to%20Python%20multipage/App-B/app.py

"""

if __name__=='__main__':
    app.run_server(debug=True, port=3000)