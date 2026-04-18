import requests

# Consumir la URL con el límite de 20
url = "https://pokeapi.co/api/v2/pokemon?limit=20"

try:
    respuesta = requests.get(url)

    # Validar si la petición fue exitosa (status 200)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        lista_pokemon = datos['results']

        for pokemon in lista_pokemon:
            nombre = pokemon['name']
            
            # Lógica y condicional para la letra 'b'
            if nombre.lower().startswith('b'):
                print(f"[ESPECIAL] {nombre}")
            else:
                print(f"Nombre: {nombre}")
    else:
        print(f"Error: Código de estado {respuesta.status_code}")

except Exception as e:
    print(f"Ocurrió un error en la conexión: {e}")


