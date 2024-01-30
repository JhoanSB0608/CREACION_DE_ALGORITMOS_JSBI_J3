def es_palindromo (texto):
    texto = texto.replace (" ", " ").lower()
    return texto == texto [::-1]

entrada = input ("Ingrese palabra u oracion: ")

if es_palindromo (entrada):
    print ("Es palindromo")
else: 
    print ("No es palindromo")