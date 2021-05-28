"""
Ejercicio 5
Hacer un programa que muestre todos los números entre dos números
que diga el usuario.
"""

numero1 = int(input("introduce el primer número para las operaciones:"))
numero2 = int(input("introduce el segundo número para las operaciones:"))

if numero1 < numero2:
    print(f"\nLos números entre {numero1} y {numero2} son: \n")
    for i in range(numero1 + 1, numero2):
        print(str(i))
else:
    print("El primer número debe ser menor que el segundo.")
