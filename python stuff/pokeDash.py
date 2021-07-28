import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)
server = app.server


global poke_df 
poke_df = pd.read_csv("C:/Users/kgtrm/Documents/VSC Code/R stuff/Pokemon Project/PokemonDataCleaned.csv", encoding="ISO-8859-1")

global names 
names = poke_df['Pokemon.Name'].tolist()
global ids 
ids = poke_df['ï..Pokemon.Id'].tolist()

global poke_dict_list
poke_dict_list = []
for i in range(len(names)):
    poke_dict_list.append({'label': names[i], 'value': ids[i]})

app.layout = html.Div([
    html.Div([
        html.H1('Pokemon Dashboard'),
        html.H2('Choose a Pokemon'),
        dcc.Dropdown(
            id='pokemon-dropdown',
            options=poke_dict_list,
            multi=True,
            clearable=True,
            value=[i for i in range(1, 11)]
        ),
        dcc.Graph(
            id='pokemon-bst-bar',
            figure={'data': [
                {'x': poke_df['Pokemon.Name'].isin('pokemon-dropdown'),
                 'y': poke_df['Base.Stat.Total'], 
                 'type': 'bar'},
            ],
            'layout': {
                'title': 'Bas State Totals'
                }
            }
        )
    ], style={'width': '40%', 'display': 'inline-block'}),
    html.Div([
        html.H2('Current Pokemon info'),
        html.Table(id='my-table'),
        html.P(''),
    ], style={'width': '55%', 'float': 'right', 'display': 'inline-block'}),
    html.Div([
        html.H2('stats graph'),
        dcc.Graph(id='stats-graph'),
        html.P('')
    ], style={'width': '100%', 'display': 'inline-block'})
    ])

@app.callback(Output('my-table', 'children'), [Input('pokemon-dropdown', 'value')])

def generate_table(selected_dropdown_value, max_rows=20):
    pokemon_df_filter = poke_df[(poke_df['ï..Pokemon.Id'].isin(selected_dropdown_value))]

    pokemon_df_filter = pokemon_df_filter.sort_values(['ï..Pokemon.Id'], ascending=True)
    colsList = [1, 2, 3, 5, 10, 11, 25, 26, 27, 28, 29, 30, 49]

    return [html.Tr([html.Th(col) for col in pokemon_df_filter.columns[colsList]])] + [html.Tr([html.Td(pokemon_df_filter.iloc[i][col]) for col in pokemon_df_filter.columns[colsList]]) for i in range(min(len(pokemon_df_filter), max_rows))]


if __name__ == '__main__':
    app.run_server(debug=True)