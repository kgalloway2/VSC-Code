import pandas as pd

global poke_df 
poke_df = pd.read_csv("C:/Users/kgtrm/Documents/VSC Code/R stuff/Pokemon Project/PokemonDataCleaned.csv", encoding="ISO-8859-1")

testList = [2, 3, 4, 5, 8, 9, 12, 22]

for i in range(50):
    print(i, poke_df.columns[i])
# names = poke_df['Pokemon.Name'].tolist()
# ids = poke_df['ï..Pokemon.Id'].tolist()

# poke_dict = {names[i]: ids[i] for i in range(len(names))}
# [1, 2, 3, 5, 10, 11, 25, 26, 27, 28, 29, 30, 49]