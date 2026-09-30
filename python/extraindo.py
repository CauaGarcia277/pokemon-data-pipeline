import requests


api_base_url = 'https://pokeapi.co/api/v2'
##Requisitando pokemon
def pokemon_id(pokemon_list):


    id_list = []
    for pokemon in pokemon_list:
        try:
            page_url = f'{api_base_url}/pokemon/{pokemon}/'
            response = requests.get(page_url)
            response.raise_for_status()


            id_list.append(response.json())

        except requests.RequestException as error:
            print(f"Erro ao buscar pokemon, id: {pokemon}")
            id_list.append(None)
    return id_list


##Requisitando status
def stats(pokemon_list):
    stats_list = []

    for pokemon in pokemon_list:
        st = []
        st.append(pokemon['id'])

        for status in pokemon['stats']:
            st.append(status['base_stat'])

        stats_list.append(st)

    return stats_list
    
##Requisitando Imagem, descrição e característica do pokemon
def pokemon(pokemon_list):
    ##Imagem
    pokemon_data = []
    for pokemon in pokemon_list:
        imagem_list = []
        try:
            page_url = f'{api_base_url}/pokemon/{pokemon['id']}'
            response = requests.get(page_url)
            response.raise_for_status()

            imagem_list.append(response.json())
            for g in imagem_list:
                gif = g['sprites']['versions']['generation-v']['black-white']['animated']['front_default']

        except requests.RequestException as error:
                print(f"Erro ao requisitar a geração do pokemon, id: {pokemon['id']}")


        ##Descrição e geração
        try:
            page_url = f'{api_base_url}/pokemon-species/{pokemon['id']}'
            response = requests.get(page_url)
            response.raise_for_status()


            geracao_data = response.json()
            geracao = geracao_data['generation']['name']
            
            desc_data = response.json()

            descricao = None
            for desc in desc_data['flavor_text_entries']:
                if desc['language']['name'] == 'en':
                    descricao = desc['flavor_text']
                    break

        except requests.RequestException as error:
            print(f'Erro ao requisitar descrição, id: {pokemon['id']}')
            ## Características
        try:  
            poke = [pokemon['id'], 
                            pokemon['name'],
                            descricao,
                            pokemon['height'], 
                            pokemon['weight'], 
                            pokemon['base_experience'], 
                            geracao, gif]
            pokemon_data.append(poke)
        except KeyError:
            print(f"Erro ao requisitar caracteristicas do pokemon, id: {id}")
                
    return pokemon_data


def tipo():
    page_url = f'{api_base_url}/type'
    response = requests.get(page_url)
    dados = response.json()

    tipo_list = []
    for tipo in dados['results']:
        tipo_list.append(tipo['name'])

    return tipo_list

#print(tipo())




id = [1, 2]
#print(pokemon(pokemon_id(id)))



def pokemon_tipo(pokemon_list):
    tipo_list = []
    for pokemon in pokemon_list:
        for types in pokemon['types']:
            tipo_list.append([pokemon['id'],types['type']['name']])
    return tipo_list

print(stats(pokemon_id(id)))