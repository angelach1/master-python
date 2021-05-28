"""
Ejercicio 8
¿Cuánto es X por ciento de un numero?
"""

numero = int(input("introduce el número para la operacion del porcentaje:"))
porcentaje = int(input("introduce el número que indique el {%} a extraer:"))

resultado = (numero * porcentaje) / 100

print(f"El {porcentaje}% de {numero} es: {resultado}")
