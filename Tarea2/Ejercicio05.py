#seudocodigo
#pedir un mumero al usuario
#con el numero ingresado calcular la suma de los numeros del 1 al numero ingresado usando un ciclo for
#inicio
numero = int(input("Ingrese un numero entero: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(f"La suma de los numeros del 1 al {numero} es: {suma}")
#Manuel Oswaldo Trabanino Barreda
#04/03/2026
