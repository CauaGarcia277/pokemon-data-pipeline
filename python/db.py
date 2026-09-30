import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ca272525#',
    database = 'pokemon_bd'
)

cursor = conexao.cursor()

def insert_pkm(df_pokemon):
    comando = '''INSERT INTO pokemon(id_pokemon, nome, descricao, altura, peso, experiencia_base, geracao, image_url) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

    for pkm in df_pokemon.itertuples(index = False):
        cursor.execute(comando, pkm)
    conexao.commit()

def insert_stats(df_stats):
    comando = '''INSERT INTO pokemon_stat(id_pokemon, hp, ataque, defesa, ataque_especial, defesa_especial, velocidade)
    VALUES (%s, %s, %s, %s, %s, %s, %s)'''

    for stats in df_stats.itertuples(index = False):
        cursor.execute(comando, stats)
    conexao.commit()

