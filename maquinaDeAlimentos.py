precio_producto_A = 270
precio_producto_B = 340
precio_producto_C = 390

print(f"Costo del producto A: ${precio_producto_A}")
print(f"Costo del producto B: ${precio_producto_B}")
print(f"Costo del producto C: ${precio_producto_C}")

producto_elegido = input("Elija un producto (A, B o C): ")

if producto_elegido not in ['A', 'B', 'C']:
    print("Producto no válido. Por favor, elija A, B o C.")
else:
    if producto_elegido == 'A':
        precio_producto = precio_producto_A
    elif producto_elegido == 'B':
        precio_producto = precio_producto_B
    else:
        precio_producto = precio_producto_C

    monto_ingresado = 0
    monedas_vuelto = []

    while monto_ingresado < precio_producto:
        moneda = int(input("Ingrese una moneda (10, 50 o 100): "))
        
        if moneda not in [10, 50, 100]:
            print("Moneda no válida. Por favor, ingrese 10, 50 o 100.")
        else:
            monto_ingresado += moneda

    vuelto = monto_ingresado - precio_producto
    print("Su vuelto:")

    while vuelto > 0:
        if vuelto >= 100:
            monedas_vuelto.append(100)
            vuelto -= 100
        elif vuelto >= 50:
            monedas_vuelto.append(50)
            vuelto -= 50
        elif vuelto >= 10:
            monedas_vuelto.append(10)
            vuelto -= 10

    for moneda in monedas_vuelto:
        print(moneda)