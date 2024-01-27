import os
os.system ('clear')
print ( """
    +++++++++++++++++++++++++++++++++++++++++++++
    +   ECUACION DE PRIMER GRADO (ax + b = 0)   +
    +++++++++++++++++++++++++++++++++++++++++++++
    """)

a = int(input("Ingrese el valor para el coeficiente a: "))
b = int(input("Ingrese el valor para el coeficiente b: "))

if (a == 0 and b == 0):
    print ("No hay solucion unica")

elif (a == 0 and b != 0):
    print ("Sin solucion")

elif (a != 0 and b != 0):
    x = -b/a
    print (f'La solucon es {x}')
