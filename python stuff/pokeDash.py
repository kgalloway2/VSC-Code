# add selector for displaying info on selected pokemon (a dropdown or maybe selected point)
# custom filter for data
# use border in to see layout better
# trendlines


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

poke_df = pd.read_csv("test.csv")

poke_dicts = [{'label': poke_df.at[i-1, "Pokemon.Name"], 'value': i-1} for i in poke_df["DFID"]]

stat_dicts = [{'label': "DFID", 'value': "DFID"},
            {'label': "Pokemon.Id", 'value': "Pokemon.Id"},
            {'label': "Pokedex.Number", 'value': "Pokedex.Number"},
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
        dcc.Checklist(
            id='legend-filter',
            options = [
                {'label': 'Legendary', 'value': '\"Legendary\"'},
                {'label': 'Sub-Legendary', 'value': '\"Sub-Legendary\"'},
                {'label': 'Mythical', 'value': '\"Mythical\"'},
                {'label': 'Non-Legendary', 'value': '\"Non-Legendary\"'}
            ],
            value=['\"Legendary\"', '\"Sub-Legendary\"', '\"Mythical\"', '\"Non-Legendary\"']
        )
    ], style={'width': '20%', 'display': 'inline-block'}),
    
    html.Div([
        html.Label("Only Fully-Evolved?"),
        dcc.Slider(
            id='evolved-filter',
            min=0,
            max=1,
            marks={0: "No", 1: "Yes"}
        )
    ], style={'width': '150px', 'display': 'inline-block'}
    ),

    html.Div([
        dcc.Checklist(
            id='generation-filter',
            options = [{'label': i, 'value': i} for i in range(1, 9)],
            value=[1, 2, 3, 4, 5, 6, 7, 8]
        )
    ], style={'width': '10%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='type-filter',
            options=[{'label': i, 'value': i} for i in poke_df['Primary.Type'].unique()],
            multi=True,
            value=[i for i in poke_df['Primary.Type'].unique()]
        )
    ], style={'width': '25%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='data-selector',
            options=[{'label': i, 'value': i} for i in poke_df.columns],
            multi=True,
            value=["Generation"]
        )
    ], style={'width': '25%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='stat-graph')
    ])
])

@app.callback(
    Output('stat-graph', 'figure'),
    Input('xstat-selector', 'value'),
    Input('ystat-selector', 'value'),
    Input('legend-filter', 'value'),
    Input('evolved-filter', 'value'),
    Input('generation-filter', 'value'),
    Input('type-filter', 'value'),
    Input('data-selector', 'value')
)
def update_stat_graph(xstat, ystat, legend_filter, evolved_filter, gen_filter, type_filter, data_list):
    current_df = poke_df[poke_df['Legendary.Type'].isin(legend_filter)]
    
    if evolved_filter:
        current_df = current_df[current_df['Fully.Evolved']]

    current_df = current_df[current_df['Generation'].isin(gen_filter)]

    prim_type = current_df[current_df['Primary.Type'].isin(type_filter)]
    sec_type = current_df[current_df['Secondary.Type'].isin(type_filter)]
    current_df = pd.concat([prim_type, sec_type])
        

    fig = px.scatter(current_df, x=xstat, y=ystat, hover_name=current_df['Pokemon.Name'], hover_data = [xstat, ystat] + data_list)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)