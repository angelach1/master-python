"""
Ejercicio 2.
Escribir un programa que ñada valores auna lista mientras que su longitud sea
menor a 120 y luego mostrar la lista.
Plus: Usar los bucles while y for
"""
"""
# Usando el bucle for

# Creamos una lista vacía
colección = []

for contador in range(0, 120):
    colección.append(f"Elemento-{contador}")
    print("Mostrando el: " + colección[contador])

print(colección)
"""
# Usando el bucle While

# Creamos una lista vacía
colección = []
x = 0

while x < 120:
    colección.append(f"Elemento-{x}")
    print("Mostrando el: " + colección[x])
    x += 1

print(colección)
