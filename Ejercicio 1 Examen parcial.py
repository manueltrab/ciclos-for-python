def calcular_precio_final():
    print("="*50)
    print("SISTEMA DE DESCUENTOS AUTOMÁTICO - TIENDA DE VIDEOJUEGOS")
    print("="*50)
    try:
        precio = float(input("Ingrese el precio del videojuego (Q): "))
        vip = input("¿El cliente es miembro VIP? (Sí/No): ").strip().lower()

        if precio >= 500:
            precio_con_descuento = precio * 0.90  # Aplica descuento del 10%
        else:
            precio_con_descuento = precio

        if vip == 's':
            precio_final = precio_con_descuento * 0.85  # Aplica descuento adicional del 15%
        else:
            precio_final = precio_con_descuento

        print(f"\nEl precio final a pagar es: Q{precio_final:.2f}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el precio.")
calcular_precio_final()
