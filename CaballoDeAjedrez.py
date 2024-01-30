def coordenada_valida (fila, columna):
    return 1 <= fila <= 8 and 1 <= columna <= 8

def movimientos_posibles_caballo (fila, columna):
    movimientos = []
    posibles_movimientos = [(-2, -1), (-2, 1), (-1, -2), (1, 2), (2, -1), (2, 1)]

    for mov in posibles_movimientos:
        nueva_fila = fila + mov [0]
        nueva_columna = columna + mov[1]

        if coordenada_valida (nueva_fila, nueva_columna):
            movimientos.append ((nueva_fila, nueva_columna))
    return movimientos

try:
    print ("Ingrese coordenadas del caballo.")
    fila = int (input ("Fila (1-8): "))
    columna = int (input("Columna (1-8): "))

    if coordenada_valida (fila, columna):
        resultados = movimientos_posibles_caballo (fila, columna)
        print (f"EL caballo puede saltar de {fila} {columna} a: {resultados}")

    else: 
        print("Posicion invalida.")
except ValueError:
    print ("Error: Ingrese valores numericos para las coordenadas.")




