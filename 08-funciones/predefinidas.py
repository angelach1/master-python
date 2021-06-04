nombre = "Ángel Alhambra"

# funciones generales
print(nombre)
print(type(nombre))

# Detectar el tipo
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("La variable no es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un número con decimales")

# Limpiar espacios en una cadena
frase = "   mi contenido    "
print(frase)
print(frase.strip())

# Eliminar variables
year = 2022
print(year)
del year
#Lo siguiente daría error, ya que la variable vuelve a no estar definida
#print(year)

# Comprobar variable vacía
texto = "  ff  "

if len(texto) <= 0:
    print("La variable está vacía.")
else:
    print("La variable tiene contenido: ", len(texto))

# Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayúsculas y minúsculas
print(nueva_frase.upper())
print(nueva_frase.lower())

