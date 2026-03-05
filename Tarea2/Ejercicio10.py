#seudocodigo
#pedir un mumero de articulos al usuario
#luego pedir el precio de cada articulo usando un ciclo for
#calcular el total a pagar por los articulos usando un ciclo for    
#inicio
num_articulos = int(input("Ingrese el numero de articulos: "))
total = 0
for i in range(num_articulos):
    precio = float(input(f"Ingrese el precio del articulo {i + 1}: "))
    total += precio
print(f"El total a pagar es: {total}")
#Manuel Oswaldo Trabanino Barreda
#04/03/2026