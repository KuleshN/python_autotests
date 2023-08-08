import requests
import pytest
host = 'https://api.pokemonbattle.me:9104'
token = '1c0524caf4fb562ada0fc2277aa974dc'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id' : 1905})
    assert response.status_code == 200
    
def test_coach_name():
    response = requests.get(f'{host}/trainers', params={'trainer_id' : 1905})
    assert response.json()['trainer_name']=='NIKO123'