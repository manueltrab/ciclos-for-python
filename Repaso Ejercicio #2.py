
import requests

url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)

if response.status_code == 200:
    datos = response.json()
    for pokemon in datos['results']:
        print(pokemon['name'].capitalize())
else:
    print(f"Error: {response.status_code}")
