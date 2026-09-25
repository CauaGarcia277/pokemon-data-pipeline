import requests


api_base_url = 'https://pokeapi.co/api/v2'

##Requisitando pokemon
def pokemon_id(id = int):
    id_list = []
    
    try:
        page_url = f'{api_base_url}/pokemon/{id}/'
        response = requests.get(page_url)
        response.raise_for_status()


        id_list.append(response.json())

    except requests.RequestException as error:
        print(f"Erro ao buscar pokemon, id: {id}")
        id_list.append(None)
    return id_list


##Requisitando status
def stats(pokemon_list):
    abili = []
    for abi in pokemon_list:
        abili.append(abi['stats'])
    st = []
    for status in abili:
        for base in status:
            st.append([base['stat']['name'], base['base_stat']])
    return st
    
##Requisitando Imagem, descrição e característica do pokemon
def pokemon(pokemon_list, id):
    ##Imagem
    imagem_list = []
    try:
        page_url = f'{api_base_url}/pokemon/{id}'
        response = requests.get(page_url)
        response.raise_for_status()

        imagem_list.append(response.json())
        for g in imagem_list:
            gif = g['sprites']['versions']['generation-v']['black-white']['animated']['front_default']

    except requests.RequestException as error:
            print(f"Erro ao requisitar a geração do pokemon, id: {id}")


    ##Descrição e geração
    try:
        page_url = f'{api_base_url}/pokemon-species/{id}'
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
        print(f'Erro ao requisitar descrição, id: {id}')
        ## Características
    try:
        for carac in pokemon_list:
            pokemon_data = [carac['id'], 
                            carac['name'],
                            descricao,
                            carac['height'], 
                            carac['weight'], 
                            carac['base_experience'], 
                            gif, geracao]
            
    except KeyError:
        print(f"Erro ao requisitar caracteristicas do pokemon, id: {id}")
            
    return pokemon_data







id = 4
print(pokemon(pokemon_id(id), id))

def tipo():
    page_url = f'{api_base_url}/type'
    response = requests.get(page_url)
    dados = response.json()

    tipo_list = []
    for tipo in dados['results']:
        tipo_list.append(tipo['name'])

    return tipo_list

print(tipo())


