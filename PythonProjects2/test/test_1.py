import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='45dc8143ed56c213330c240f847ed862'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN }
TRAINER_ID = '28914'
TRAINER_NAME = 'Hellboy'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers',params = {'trainer_id':TRAINER_ID,})
    assert response_get.json()["data"][0]['trainer_name'] == 'Hellboy'
