#seudocodigo   
#pedir 10 numeros direfentes al usuario
#contar cuantos numeros fueron positivos
#contar cuantos numeros fueron negativos
#cuantos numeros fueron ceros
#inicio
numeros = []
for i in range(10):
    numero = int(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)

positivos = 0
negativos = 0
ceros = 0

for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")
print(f"Numeros ceros: {ceros}")
