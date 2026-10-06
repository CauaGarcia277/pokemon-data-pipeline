import pandas as pd

def df_tipo(tipo):


    tipo_list = tipo()
    tipo_df = pd.DataFrame(tipo_list, columns=['tipo'])

    ##Verificando valores nulos
    if tipo_df.isnull().sum() > 0:
        tipo_df = tipo_df.fillna('Não informado')


    ##Verificando valores duplicados
    if tipo_df.duplicated().sum() > 0:
        tipo_df = tipo_df.drop_duplicates()

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

    # Verificando valores nulos
    if stats_df.isnull().sum().sum() > 0:
        for coluna in stats_df.columns:
            if stats_df[coluna].isnull().sum() > 0:
                stats_df[coluna] = stats_df[coluna].fillna(0)
            else:
                continue

    # Verificando valores duplicados
    if stats_df.duplicated().sum() > 0:
        stats_df = stats_df.drop_duplicates()

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

    colunas_numericas = ['id_pokemon', 'altura', 'peso', 'experiencia_base']
    colunas_texto = ['nome', 'descricao', 'geracao', 'image_url']

    for coluna in colunas_numericas:
        if pokemon_df[coluna].isnull().sum() >0:
            pokemon_df[coluna] = pokemon_df[coluna].fillna(0)

    for coluna in colunas_texto:
        if pokemon_df[coluna].isnull().sum() > 0:
            pokemon_df[coluna] = pokemon_df[coluna].fillna('Não informado')
    
    ##Modificando os tipos da coluna
    pokemon_df['altura'] = pokemon_df['altura'].astype('double')
    pokemon_df['peso'] = pokemon_df['peso'].astype('double')

    if pokemon_df.duplicated().sum() > 0:
        pokemon_df = pokemon_df.drop_duplicates()

    return pokemon_df



def df_pokemon_tipo(poke_list):
    df_pk = pd.DataFrame(poke_list, columns = [
        'id_pokemon',
        'nome'])

    if df_pk['id_pokemon'].isnull().sum() > 0:
        df_pk['id_pokemon'] = df_pk['id_pokemon'].fillna(0)

    if df_pk['nome'].isnull().sum() > 0:
        df_pk['nome'] = df_pk['nome'].fillna('Não informado')

    if df_pk.duplicated().sum() > 0:
        df_pk = df_pk.drop_duplicates()

    return df_pk



id = [1, 2, 3, 4, 5, 6]
#insert_stats(df_stats(stats(pokemon_id(id))))