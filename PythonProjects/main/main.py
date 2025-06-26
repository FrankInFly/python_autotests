import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN_ID = 'fad310bf7bd094f9dd72411ace62f284'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN_ID}
TRAINER_ID = '36553'

body_create = {
    "name": "Hoshi",
    "photo_id": 68
} 


# создание покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text)

response_data = response_create.json()
POKEMON_ID = response_data['id']


# смена имени покемона
body_change_name = {
    "pokemon_id": POKEMON_ID,
    "name": "Vernon"
}

'''response_change_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)'''

 
# поймать покемона в покебол
body_pokeball = {
    "pokemon_id": POKEMON_ID
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball )
print(response_pokeball.text)

