def es_primo (numero):
    if numero < 2:
        return False
    for i in range (2, int (numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True 

def obtener_primos_hasta_n (n):
    primos = [i for i in range (2, n) if es_primo (i)]
    return primos 

def obtener_factores_primos (numero):
    factores = []
    i = 2
    while i <= numero:
        if (numero % i) == 0:
            factores.append(i)
            numero = numero / i
        else:
            i = i + 1
    return factores

def suma_primos(numero_par):
    primos = obtener_primos_hasta_n(numero_par)
    for i in primos:
        if numero_par - i in primos:
            print(f"{i} + {numero_par - i}")
            break

def primos_terminan_en_7(n):
    primos_7 = [i for i in range (2, n) if es_primo(i) and i % 10 == 7]
    return primos_7

def suma_cuadrados_primos_entre_1_y_1000():
    primos = obtener_primos_hasta_n(1000)
    suma_cuadrados = sum(primo**2 for primos in primos) 
    return suma_cuadrados

def producto_primos_con_digitos_7():
    primos_con_7 = [7, 17, 37, 47, 67, 71, 79, 97]
    producto = 1
    for primo in primos_con_7 :
        producto *= primo
    return producto

numero = int(input ("Ingrese un numero: "))
if es_primo(numero):
    print(f"{numero} es primo")
else: 
    print(f"{numero} es compuesto")

n = int(input("Cuantos primos:"))
for primo in obtener_primos_hasta_n(n**2):
    print(primo)
    n -= 1
    if n == 0:
        break

m = int(input("Primos menores que: "))
for i in obtener_primos_hasta_n(m):
    print(i)

m = int(input("Contar primos menores que: "))
contador_primos = sum(1 for i in range(2, m) if es_primo(i))
print (f"Hay {contador_primos} primos menores que {m}")

numero = int(input("Ingrese numero: "))
for factor in obtener_factores_primos(numero):
    print(factor)

numero_par = int(input("Ingrese numero par: "))
if numero_par % 2 == 0:
    suma_primos(numero_par)
else:
    print("El numero ingresado no es par.")

print(f"Cantidad de primos menores que 10000 y terminan en 7: {len(primos_terminan_en_7(10000))}")
print(f"Suma de cuadrados de primos entre 1 y 1000: {suma_cuadrados_primos_entre_1_y_1000()}")
print(f"Producto de primos menores que 100 con digito 7: {producto_primos_con_digitos_7()}")





