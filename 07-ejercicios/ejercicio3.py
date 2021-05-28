"""
Ejercicio 3
Escribir un programa que muestre los cuadrados de los 
60 primeros números naturales.
Resolverlo con for y while
"""

print("******************* Ejemplo con while ********************")
contador = 0

while contador <= 60:
    print(f"El cuadrado de {contador} es: {str(contador ** 2)}")
    contador += 1

print("******************* Ejemplo con for ********************")

contador = 0 #esto no es necesario, ya que la variable se inicializa en el bucle for
for contador in range(61):
    print(f"El cuadrado de {contador} es: {str(contador ** 2)}")
