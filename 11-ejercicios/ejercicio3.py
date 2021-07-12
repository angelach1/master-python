"""
Ejercicio 3.
Programa que compruebe siuna variable está vacía, y si está vacía rellenarla con texto en
minúsuclas y mostrarlo en mayúsculas.
"""

texto = "    "

if len(texto.strip()) <= 0:
    texto = "Hola, soy un texto en minúsuculas"
    print(texto.upper())
else:
    print(f"La variable tiene contendio: {texto}")