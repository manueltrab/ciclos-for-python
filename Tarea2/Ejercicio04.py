#seudocodigo
#pedir un numero entero al usuario 
#con el numero ingresado mostrar la tabla de multiplicar del 1 al 10 usando
#un ciclo for
#inicio
numero = int(input("Ingrese un numero entero: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}") 