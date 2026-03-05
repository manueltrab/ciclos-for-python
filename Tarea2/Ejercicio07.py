#seudocodigo
#pedir al usuario 5 notas diferentes con numeros enteros
#calcular el promedio de las notas usando un ciclo for
#inicio
notas = []
for i in range(5):
    nota = int(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio}")