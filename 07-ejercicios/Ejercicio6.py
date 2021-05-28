"""
Ejercicio 6
Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrar el título de la tabla y luego las multiplicaciones.
"""

for contador in range(1,11):
    print(f"\nTabla de multiplicar del nº {contador}")
    for numero in range (1, 11):
        print(f"{contador} x {numero} = {contador * numero}")
