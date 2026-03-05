#seudocodigo
#pedir un numero al usuario
#que el programa dibuje una escalera con * hasta llegar a los * dependiendo del numero ingresado usando un ciclo for
#inicio
numero = int(input("Ingrese un numero entero: "))
for i in range(1, numero + 1):
    print("*" * i)