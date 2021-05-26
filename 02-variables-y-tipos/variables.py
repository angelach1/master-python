'''
Una variable es un contenedro de información
que dentro guardará un dato, se pueden crear 
muchas variables y que cada una tenga un dato
'''


# Crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "con Virctor Robles"
numero = 45
decimal =6.5

# Mostrar el valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print( "------------------------------")

# Sustituir el valor de algunas variables / reasignar valores
numero = 77
decimal = 9.22

print(numero)
print(decimal)

print( "------------------------------")

# concatenación
nombre = "Victor"
apellidos = "Robles"
web = "victorroblesweb.es"

print('1 - ' + nombre + " " + apellidos + ' - ' + web)
print(f"2 - {nombre} {apellidos} - {web}")
cadena = f"3 - {nombre} {apellidos} - {web}"
print(cadena)
print("4 - Hola, me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))
print ("5 - ", nombre, apellidos, web)
