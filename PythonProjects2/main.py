
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='45dc8143ed56c213330c240f847ed862'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN }

body_creat = {
    "name": "Ken",
    "photo_id": 1
}
body_catch = {
    "pokemon_id": "273737"
}
body_changes ={
    "pokemon_id": "273737",
    "name": "Aloha",
    "photo_id": 2
}

response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER, json = body_creat)
print(response_create.text)


response_catch = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_catch)
print(response_catch.text)

response_changes = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_changes)
print(response_changes.text)
