import pandas as pd

df = pd.read_csv("PokemonDataCleaned.csv")

def legend(x):
    if x in ['\"Legendary\"', '\"Sub-Legendary\"', '\"Mythical\"']:
        return x
    else:
        return '\"Non-Legendary\"'

df['Legendary.Type'] = df['Legendary.Type'].apply(legend)

df.to_csv("test.csv")