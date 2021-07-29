# Capturar execpciones y manejar errores en código susceptible a fallos/errores

"""
try: #Comienzo de la comprobación de excepciones
    nombre = input("Cuál es tu nombre?: ")
    print(nombre)

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except: # Se ejecuta cuando se produce un error en el apartado try
    print("Ha ocurrido un error, mete bien el nombre.")
else: # Opcional: Se ejecuta si no se prudice un error
    print("Todo ha funcionado correctamente")
finally: # Opcional: Siempre se ejecuta, haya error o no, al final del bloque try
    print("Fin de la ejecución.")
"""

#Múltiples excepciones
"""
try:
    numero = int(input("Número para elevarlo al cuadrado: "))
    #numero = input("Número para elevarlo al cuadrado: ")
    print("El cuadrado de " + str(numero) +  " es: " + str(numero*numero)) 
except TypeError: # Se produce si no usamos la función int para convertir la cadena devuelta por la función input
    print("¡¡Debes convertir tus cadenas a enteros en el código!!")
#except ValueError:
#    print("Introduce un número correcto!!")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)
"""

# Excepciones personalizadas o lanzar una excepción

try:
    nombre = input("introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real.")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo.")
    else:
        print(f"Bienvenido al Master en Python {nombre}!!")
except Exception as e:
    print("existe un error: ", e)


