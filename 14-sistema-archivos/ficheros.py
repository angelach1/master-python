from io import open
import pathlib
import shutil

# Abrir archivo
# Para abrir el archivo desde el directorio de la aplicación, sin que haya problemas, se 
# puede utilizar la siguiente línea de código
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
# archivo = open("fichero_texto.txt", "a+")
archivo = open(ruta, "a+")

# Escribir
archivo.write("**************Soy un texto metido desde Pythoon*******************\n")

# Cerrar el archivo
archivo.close()

# Leer contenido de archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

contenido = archivo_lectura.read()
print(contenido)

# Leer contenido y guardarlo en una lista
archivo_lectura = open(ruta, "r")
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    print("- ", frase.upper())
archivo_lectura.close()

"""
# Copiar 
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)


# Mover
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)


# Eliminar
import os

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""

# Comprobar si existe un fichero
import os.path

#print(os.path.abspath("./"))
ruta_comprobar = os.path.abspath(("./") + "/fichero_texto.txt")
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("el archivo no existe")

