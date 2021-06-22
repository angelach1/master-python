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

# Añadir elementos a lista
cantantes.append("Madonna")
cantantes.append("Siniestro Total")
print(cantantes)

# Recorrer una lista
nuevo_cantante = ""
while nuevo_cantante != "salir":
    nuevo_cantante = input("Introduce un nuevo cantante o grupo musical: ")
    if nuevo_cantante != "salir":
        cantantes.append(nuevo_cantante)

        

print("\n************* LISTADO DE CANTANTES ************")
for cantante in cantantes:
    print(f"{cantantes.index(cantante) + 1} --- {cantante}")


# Listas multidimensionales
print("\n************* LISTADO DE CONTACTOS ************")
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

print(contactos)
print(contactos[0][1])
print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: "  + elemento)
        else:
            print("eMail: " + elemento)
    print("\n")