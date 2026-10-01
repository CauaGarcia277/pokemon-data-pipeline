import pandas as pd

def df_tipo(tipo):


    tipo_list = tipo()
    tipo_df = pd.DataFrame(tipo_list, columns=['tipo'])

    ##Verificando valores nulos
    tipo_df.isnull().sum()

    ##Verificando o tipo da coluna
    tipo_df.dtypes


    ##Verificando valores duplicados
    tipo_df.duplicated().sum()

    return tipo_df


def df_stats(stats_list):
    stats_df = pd.DataFrame(stats_list, columns=
                            ['id', 
                             'hp', 
                             'ataque', 
                             'defesa', 
                             'ataque_especial', 
                             'defesa_especial', 
                             'velocidade'])


    stats_df.isnull().sum()

    stats_df.dtypes

    ##Verificando valores duplicados
    stats_df.duplicated().sum()

    return stats_df


def df_pokemon(pokemon_list):

    pokemon_df = pd.DataFrame(pokemon_list, columns= [
        'id_pokemon',
        'nome',
        'descricao',
        'altura',
        'peso',
        'experiencia_base',
        'geracao',
        'image_url'])

    pokemon_df.isnull().sum()
    ##Revizando os tipos em cada coluna
    pokemon_df.dtypes
    ##Modificando os tipos da coluna
    pokemon_df['altura'] = pokemon_df['altura'].astype('double')
    pokemon_df['peso'] = pokemon_df['peso'].astype('double')

    pokemon_df.duplicated().sum()

    return pokemon_df



def df_pokemon_tipo(poke_list):
    df_pk = pd.DataFrame(poke_list, columns = [
        'id_pokemon',
        'nome'])

    df_pk.isnull().sum()

    df_pk.dtypes

    df_pk.duplicated().sum()

    return df_pk



id = [1, 2, 3, 4, 5, 6]
#insert_stats(df_stats(stats(pokemon_id(id))))