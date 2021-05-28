"""
# Bucle FOR

for variable in elemento_iterable (lista, rango, etc...)
    BLOQUE DE INSTRUCCIONES
"""

contador = 0
resultado = 0

for contador in range(1, 11):
    print("voya por el  " + str(contador))
    # resultado = resultado + contador
    resultado += contador

print(f"El resultado es: {resultado}")

# Ejemplo tablas de multiplicar
print("\n#################### EJEMPLO ###################")

numero_usuario = int(input("¿De qé número quieres la tabla de multiplicar?: "))
print(f"\n### Tabla de multiplicar del número {numero_usuario} ####")

for numero_tabla in range(0, 10):
    if numero_usuario < 1 or numero_usuario > 9:
        print("No se pueden mostrar números prohibidos")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada")
