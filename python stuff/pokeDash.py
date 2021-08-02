# add filters for graph like fully-evolved, legendary, generation, etc.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

poke_df = pd.read_csv("PokemonDataCleaned.csv")

poke_dicts = [{'label': poke_df.at[i-1, "Pokemon.Name"], 'value': i-1} for i in poke_df["DFID"]]

stat_dicts = [{'label': "DFID", 'value': "DFID"},
            {'label': "Pokemon.Height", 'value': "Pokemon.Height"},
            {'label': "Pokemon.Weight", 'value': "Pokemon.Weight"},
            {'label': "Male.Ratio", 'value': "Male.Ratio"},
            {'label': "Female.Ratio", 'value': "Female.Ratio"},
            {'label': "Base.Happiness", 'value': "Base.Happiness"},
            {'label': "Health.Stat", 'value': "Health.Stat"},
            {'label': "Attack.Stat", 'value': "Attack.Stat"},
            {'label': "Defense.Stat", 'value': "Defense.Stat"},
            {'label': "Special.Attack.Stat", 'value': "Special.Attack.Stat"},
            {'label': "Special.Defense.Stat", 'value': "Special.Defense.Stat"},
            {'label': "Speed.Stat", 'value': "Speed.Stat"},
            {'label': "Base.Stat.Total", 'value': "Base.Stat.Total"},
            {'label': "Catch.Rate", 'value': "Catch.Rate"},
            {'label': "Experience.Growth.Total", 'value': "Experience.Growth.Total"},
            {'label': "Experience.Yield", 'value': "Experience.Yield"},
            {'label': "Generation", 'value': "Generation"}
            ]          

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xstat-selector',
        options=stat_dicts,
        value="DFID")
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(id='ystat-selector',
        options=stat_dicts,
        value="Pokemon.Height"
        )
    ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='stat-graph')
    ])
])

@app.callback(
    Output('stat-graph', 'figure'),
    Input('xstat-selector', 'value'),
    Input('ystat-selector', 'value')
)
def update_stat_graph(xstat, ystat):
    fig = px.scatter(poke_df, x=poke_df[xstat], y=poke_df[ystat], hover_name=poke_df['Pokemon.Name'])

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)