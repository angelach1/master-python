"""
# Bucle FOR

for variable in elemento_iterable (lista, rango, etc...)
    BLOQUE DE INSTRUCCIONES
"""

contador = 0
resultado = 0

for contador in range(0, 10):
    print("voya por el  " + str(contador))
    # resultado = resultado + contador
    resultado += contador

print(f"El resultado es: {resultado}")
