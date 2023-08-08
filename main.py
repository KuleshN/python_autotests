import requests
token = '1c0524caf4fb562ada0fc2277aa974dc'
host = 'https://api.pokemonbattle.me:9104'

# 1.зарегили тренера путь trainers/reg 1.
# 2. Далее активировали отправив только токен в боди и по другому пути trainers/confirm_email  2.

 #"trainer_token" : token,
 # "email": "rarog@dolnikov.ru",
 #"password": "Iloveqa1"                             
                           

# создаём покемона
response = requests.post(f'{host}/pokemons', 
 json = {
                                
   "name": "Вульвазавр",
   "photo": "https://dolnikov.ru/pokemons/albums/111.png"
},
headers= {"Content_type" : "application/json",
        "trainer_token" : token}

)
print(response.text)
# меняем имя покемону

change_name = requests.put(f'{host}/pokemons',
json = {
    "pokemon_id": "5814",
    "name": "NewВульвазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/111.png"
},
headers= {"Content_type" : "application/json",
        "trainer_token" : token}

)
print(change_name.text)


#ловим покемона
catch_pok = requests.post(f'{host}/trainers/add_pokeball',
json = {
    "pokemon_id": "6007",
   

    
},
headers= {"Content_type" : "application/json",
        "trainer_token" : token}

)
print(catch_pok.text)