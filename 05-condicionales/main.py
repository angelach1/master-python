"""
# Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones

# Operadores de comparación
== igual
!= No igual o distinto
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores lógicos
and Y
or O
! Negación
not NO
"""

# Ejemplo 1
print("################### EJEMPLO 1 #################")

color = "rojo"
#color = input("Adivina cuál es mi color favorito: ")

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("El color es incorrecto")

# Ejemplo 2
print("\n################### EJEMPLO 2 #################")

# year = int(input("¿En qué año estamos?: "))
year = 2020

if year >= 2021:
    print("Estamos de 2021 en adelante !!")
else:
    print("Es un año anterior a 2021")

# Ejemplo 3
print("\n################### EJEMPLO 3 #################")
    
nombre = "Ángel Alhambra"
ciudad = "Madrid"
continente = "Europa"
edad = 17
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"Es mayor de edad !!")
    if continente != "Europa":
        print("El usuario NO es Europeo")
    else:
        print(f"Es Europeo y de {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4
print("\n################### EJEMPLO 4 #################")

dia = 5
# (input("Introduce un día de la semana en número:"))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miércoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else :
    print("Es Fin de Semana")

# Ejemplo 5
print("\n################### EJEMPLO 5 #################")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Está en edad de trabajar")
else:
    print("NO esta en edad de trabajar")

# Ejemplo 6
print("\n################### EJEMPLO 6 #################")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana")
else: 
    print(f"{pais} NO es un país de habla hispana")

# El ejemplo siguiente es igual pero con el operador not
if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} Es un país de habla hispana")

# El ejemplo siguiente es igual pero con el operador != (distinto)
if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} Es un país de habla hispana")



