'''
Ejercicio 1. Hacer un  programa que tenga una lista de 9 números enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer una función que recorra listas de números y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algún elemento que el usuario pida por teclado
'''
def saca_lista(lista):
    resultado = ""
    for elemento in lista:
            resultado += "Elemento: " + str(elemento) + "\n" 
    return(resultado)

cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesisas']
numeros = [1, 2, 5, 8, 3, 4]

print("************* Imprime la lista **************")
print(saca_lista(numeros))

print("************* Ordena la lista **************")
numeros.sort()
print(saca_lista(numeros))
print(saca_lista(cantantes))

print("************* Imprime la longitud de la lista **************")
print(len(numeros))

cantante = input("Introduce un grupo o cantante: ")
print(cantante in cantantes)

