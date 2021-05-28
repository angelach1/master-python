"""
Ejercicio 4
Pedir dos números al usuario y hacer todas las operaciones
básicas de una calculadora y mostrarlo por pantalla.
"""

numero1 = int(input("introduce el primer número para las operaciones:"))
numero2 = int(input("introduce el segundo número para las operaciones:"))

suma = str(numero1 + numero2)
resta = str(numero1 - numero2)
multiplicacion = str(numero1 * numero2)
division = str(numero1 / numero2)

print(f"\nLa suma de {numero1} y {numero2} es: {suma}")
print(f"\nLa resta de {numero1} y {numero2} es: {resta}")
print(f"\nLa multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"\nLa división de {numero1} y {numero2} es: {division}")
