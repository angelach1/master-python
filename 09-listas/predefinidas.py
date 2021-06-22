cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesisas']
numeros = [1, 2, 5, 8, 3, 4 ]

#Ordenar
print("*********ORDENAR**********")
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
print("*********AÑADIR**********")
cantantes.append("Natos y Waor")
cantantes.insert(1, "David Bisbal")
print(cantantes)

# Eliminar elementos
print("*********ELIMINAR**********")
cantantes.pop(1)
cantantes.remove('Bad Bunny')
print(cantantes)

# Dar la vuelta
print("*********INVERTIR**********")
print(numeros)
numeros.reverse()
print(numeros)

# Comprobar si existe dentro de una lista
print("*********COMPROBAR SI EXISTE**********")
print('Drake' in cantantes)

# Contar elementos
print("*********CONTAR ELEMENTOS**********")
print(cantantes)
print(len(cantantes))

# cuantas veces aparece un elemento
print("*********CUANTAS VECES APARECE UN ELEMENTO**********")
numeros.append(8)
print(numeros.count(8))

# Conseguir el índice
print("*********CONSEGUIR EL ÍNDICE**********")
print(cantantes.index(("Drake")))

# Unir listas
print("*********UNIR**********")
cantantes.extend(numeros)
print(cantantes)
