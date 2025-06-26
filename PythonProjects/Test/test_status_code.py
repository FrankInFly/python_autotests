import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN_ID = 'fad310bf7bd094f9dd72411ace62f284'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN_ID}
TRAINER_ID = '36553'


## запрос GET /trainers приходит с кодом 200
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200


## в ответе приходит строчка с именем твоего тренера
def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    data = response.json()
    assert data['data'][0]['trainer_name'] == "FrankInFly"