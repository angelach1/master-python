'''
SET es un tipo de dato, para tener una colección de valores,
pero no tiene ni índice ni orden.
'''

personas = {
    'Victor',
    'Manolo',
    'Francisco'
}

personas.add('Paco')
print(type(personas))
print(personas)

personas.remove('Francisco')
print(personas)