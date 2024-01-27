def es_palindromo(numero):
    str_numero = str(numero)
    return str_numero == str_numero[::-1]

def main():
    try:
        numero = int (input("Ingrese un numero: "))
        if numero < 0:
            print("Por favor, ingrese un numero natural: ")
        elif es_palindromo(numero):
            print(f'{numero} es un palindromo')
        else: 
            print(f'{numero} no es un palindromo')
    except ValueError:
        print("Por favor, ingrese un numero entero")
        
if __name__ == "__main__":
    main() 