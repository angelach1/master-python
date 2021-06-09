"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar uin índice numérico.
"""

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
# Para definir una lista con list, a list hay que pasarle una tupla, por eso los dobles paréntesis
cantantes = list (('2pac', 'Drake', 'Jenifer Lopez'))
years = list(range(2020, 2050))
variada = ["Ángel", 30, 20.8, True]


print(peliculas)
print(cantantes)
print(years)
print(variada)

# Índices (siempre empiezan por el número 0)
peliculas[1] = "Gran Torino"
peliculas[0] = "El Hobbit"
print(peliculas)
print(peliculas[0])
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])


