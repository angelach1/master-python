"""
FUNCIONES
Una función es un conjunto de instrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocando a la función tantas veces
como sea necesario.

Declaración:

def nombreDeMiFuncion(parametros):
    #BLOQUE / CONJUNTO DE INSTRUCCIONES

Uso:

nombreDeMiFuncion(mi_parametro, ...)
"""

"""
#Ejemplo 1
print ("######## EJEMPLO1 #######")

# Definición de la función
def muestraNombre():
    print("Ángel")
    print("Pepe")
    print("Indalecio")
    print("Loli")
    print("\n")

#Invocar a la fución
muestraNombre()
muestraNombre()

# Ejemplo 2. Parámetros
print("############# EJEMPLO 2 ################")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("introduce tu edad: "))
mostrarTuNombre(nombre, edad)

# Ejemplo 3
print("############# EJEMPLO 3 ################")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")
    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")
    print("\n")

for numero_tabla in range(1,11):
    tabla(numero_tabla)

# Ejemplo 4
print("############# EJEMPLO 4 ################")

# Parámetros opcionales
def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Angel Alhambra")
getEmpleado("Angelote", "51373451")

# Ejemplo 5: return o devolver datos
print("############# EJEMPLO 5 ################")
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("Angel"))


# Ejemplo 6: return o devolver datos
print("############# EJEMPLO 6 ################")

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas == True:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print(calculadora(5, 10, True))
print(calculadora(5, 10, False))
print(calculadora(5, 10))

"""
# Ejemplo 7: Funciones anidadas
print("############# EJEMPLO 7 ################")
def getNombre(nombre):
     texto = f"El nombre es: {nombre}"
     return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Angel", "Alhambra Chaparro"))

