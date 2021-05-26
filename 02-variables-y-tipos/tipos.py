nada = None
cadena = "Hola soy Victor Robles WEB"
entero = 99
decimal = 8.5
booleano = True
lista = [10, 20, 30, 100, 200]
listaVariada = [10, "veinte", 30.5, None]
tupla = (10, 15, "hola", None) #como una lista, pero los valores no cambian
diccionario = {     #Conjunto de claves-valores
    "Nombre": "Victor",
    "Apellido": "Robles",
    "Curso": "Master en Python"
}
rango = range(9)
dato_byte = b"tipo de datos byte"

#imprime la variable
print('1-', nada)
print('2-', cadena)
print('3-', entero)
print('4-', decimal)
print('5-', booleano)
print('6-', lista)
print('7-', listaVariada)
print('7[0]-', listaVariada[0])
print('7[1]-', listaVariada[1])
print('7[2]-', listaVariada[2])
print('7[3]-', listaVariada[3])
print('8-', tupla)
print('9-', diccionario)
print('10-', rango)
print('11-', dato_byte)

#imprime el tipo
print('1-', type(nada))
print('2-', type(cadena))
print('3-', type(entero))
print('4-', type(decimal)) #float
print('5-', type(booleano))
print('6-', type(lista))
print('7-', type(listaVariada))
print('7[0]-', type(listaVariada[0]))
print('7[1]-', type(listaVariada[1]))
print('7[2]-', type(listaVariada[2]))
print('7[3]-', type(listaVariada[3]))
print('8-', type(tupla))
print('9-', type(diccionario))
print('10-', type(rango))
print('11-', type(dato_byte))


#conversión de tipos
print("************************************************************************")

texto = "Hola, soy un texto"
numero = 99

# Lo siguiente da error TypeError: can only concatenate str (not "int") to str
# No se pueden encadenar variables de distinto tipo
#print(texto + ' ' + numero) 

#cambiando el tipo del entero a cadena se corrige
numero = str(numero)
print(texto + ' ' + numero)

print(type(numero))

numero = int(numero)
print(numero)
print(type(numero))

numero = float(numero)
print(numero)
print(type(numero))

numero = bool(numero)
print(numero)
print(type(numero))