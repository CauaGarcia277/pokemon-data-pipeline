from extraindo import tipo, pokemon_id, pokemon, pokemon_tipo, stats
from tratamento import df_tipo, df_pokemon_tipo, df_stats, df_pokemon
from db import insert_pkm, insert_stats, insert_tipo, insert_pkm_tipo


id = [7, 8, 9, 10, 11, 12, 13, 14, 15]
insert_pkm(df_pokemon(pokemon(pokemon_id(id))))
insert_stats(df_stats(stats(pokemon_id(id))))
insert_tipo(df_tipo(tipo))
insert_pkm_tipo(df_pokemon_tipo(pokemon_tipo(pokemon_id(id))))