'''
Diccionario:
Tipo de dato que almacena un conjunto de datos en formato clave > valor.
Es parecido a un array asociativo o un objeto json.
'''

persona = {
    'nombre': 'Ángel',
    'apellidos': 'Alhambra',
    'web': 'angelach.hopto.org'
}

print(persona)
print(type(persona))
print(persona['nombre'])
print(persona['apellidos'])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antinio@antonio.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

print(contactos)
print(contactos[0]['nombre'])
contactos[0]['nombre'] = 'Antoñito'
print(contactos[0]['nombre'])

print('\nListado de contactos\n')
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"eMail del contacto: {contacto['email']}\n")
