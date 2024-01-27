def media_armonica (secuencia):
    n = len(secuencia)
    suma_inversos = sum (1/x for x in secuencia)
    media_armonica = n / suma_inversos
    return media_armonica

def main ():
    try:
        cantidad_numeros = int(input ("Cuantos numero vas a ingresar: "))
        if cantidad_numeros <= 0:
            print("Por favor, ingrese un numero entero positivo.")
            return
        numeros = [int(input(f'n{i + 1} = "'))for i in range (cantidad_numeros)]
        resultado = media_armonica(numeros)

        print (f'La media armonica de esta secuencia es: H = {resultado}')
    except ValueError:
        print("Por favor, ingrese un numero valido.")
if __name__ == "__main__":
    main ()