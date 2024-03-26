import pandas as pd

pokemon_df = pd.read_csv("pokemon.csv")
anime_df = pd.read_csv("myanimelist.csv")

# Creating a list of lists from pokemon_df:
poke_column_names = pokemon_df.columns.tolist()
pokemon_list = pokemon_df.values.tolist()
pokemon_list.insert(0, poke_column_names)

# Creating a list of lists from anime_df:
anime_columns = anime_df.columns.tolist()
anime_list = anime_df.values.tolist()
anime_list.insert(0, anime_columns)

# Creating a list of dictionaries from pokemon_df:
pokemon_dict_list = pokemon_df.to_dict(orient='records')

# Creating a list of dictionaries from anime_df:
anime_dict_list = anime_df.to_dict(orient='records')

# Creating a list of tuples from pokemon_df:
pokemon_tuple_list = [tuple(poke_column_names)]
for row in pokemon_df.values:
    pokemon_tuple_list.append(tuple(row))

# Creating a list of tuples from anime_df:
anime_tuple_list = [tuple(anime_columns)]
for row in anime_df.values:
    anime_tuple_list.append(tuple(row))
