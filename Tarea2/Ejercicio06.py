#seudocodigo
#pedir al usario que ingrese una palabra
#leer la palabra y contar cuantas vocales tiene usando un ciclo for
#inicio
palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
contador_vocales = 0
for letra in palabra:
    if letra in vocales:
        contador_vocales += 1
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")
