"""
Ejercicio 10
El programa tiene que pedir la nota de un numero de alumnos y sacar por pantalla
cuantos han aprobado y cuantos han suspendido
"""

alumnos = int(input("Introduce el número de alumnos a contabilizar: "))
contador = 1
aprobados = 0
suspendidos = 0



while contador <= alumnos:
    nota = float(input(f"Introduce la nota del alumno nº {contador}: "))
    if nota < 0 or nota > 10:
        print(f"La nota del alumno nº {contador} no está en el rango de 0 a 10.")
    else:
        if nota < 5:
            print(f"El alumno nº {contador} ha suspendido.\n")
            suspendidos +=1
        else:
            print(f"El alumno nº {contador} ha aprobado.\n")
            aprobados +=1
        contador += 1
    
print("El resultado total es el siguiente:\n")
print(f"Número de alumnos aprobados: {aprobados}.\n")
print(f"Número de alumnos suspendidos: {suspendidos}.\n")
