"""
- Es aconsejable definir todas las funciones al principio del fichero
- Es aconsejable que la función devuelva un valor en vez de hacer un print dentro.
- Si se quiere acceder a una variable global desde dentro de una función, se puede hacer, siempre y
  cuando la variable esté definida antes de llamar a la función donde se va a usar.
"""

def mi_funcion():
    return "Hola que tal " + nombre

def mi_funcion2():
    return "Hola que tal 2 " + apellidos


nombre = "Ángel"
apellidos = "Alhambra"

# Si las dos líneas siguientes estuvieran antes de la declaración de las variables nombre y apellidos
# el programa fallaría diciendo que no están definidas las variables.
print(mi_funcion())
print(mi_funcion2())