"""
Ejercicio 4.
Crear un script que tenga 4 variables: una lista, un string, un enter y un booleano,
y que imprima eun mensaje según eltipo de dato de cada variable.
Usar funciones.
"""

def traducirTipo(tipo):
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NÚMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"
    else:
        result = "NO COINCIDE CON NINGÚN TIPO DEL SUPUESTO"
    
    return result


def comprobaTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    
    if test:
        result =f"Este dato es del tipo {traducirTipo(type(dato))}"
    else:
        result = "El tipo de dato no es correcto"
    
    return result

mi_lista = ["Hola mundo", 77]
titulo = "Master en Python"
numero = 100
verdadero = True

print(comprobaTipado(mi_lista, list))
print(comprobaTipado(titulo, list))
print(comprobaTipado(numero, list))
print(comprobaTipado(verdadero, list))

print(comprobaTipado(titulo, str))
print(comprobaTipado(numero, int))
print(comprobaTipado(verdadero, bool))
