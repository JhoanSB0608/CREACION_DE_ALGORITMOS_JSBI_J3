def mayor_alza_precio(dias, precios):
    mayor_alza = 0

    for i in range(1, dias):
        alza_diaria = precios[i] - precios[i - 1]

        if alza_diaria > mayor_alza:
            mayor_alza = alza_diaria

    return mayor_alza

def main():
    dias = int(input("¿Cuántos días? "))

    precios = []

    for i in range(1, dias + 1):
        precio = float(input(f"Día {i}: "))
        precios.append(precio)

    alza_maxima = mayor_alza_precio(dias, precios)

    if alza_maxima > 0:
        print(f"La mayor alza fue de {alza_maxima:.2f} pesos.")
    else:
        print("No hubo alzas.")

if __name__ == "__main__":
    main()
