"""
Ejercicio 2.
Escribir un script que nos muestre por pantalla todos los números pares del 1 al 120
"""

print("****************** Ejemplo con bucle for ***********************")
numero = 1
cadena = str(0)

for numero in range (1, 121):
    if numero % 2 == 0:
        cadena = cadena + "," + str(numero)

print(cadena)

print("****************** Ejemplo con bucle for con salto ***********************")
numero = 1
cadena = str(0)

for numero in range(0, 121, 2):
    #if numero % 2 == 0:
        cadena = cadena + "," + str(numero)

print(cadena)


print("****************** Ejemplo con bucle while ***********************") 
numero = 1
cadena = str(0)

while numero < 121:
    if numero % 2 == 0:
        cadena = cadena + "," + str(numero)

    numero += 1

print(cadena)
