"""
Ejercicio 9.
Hacer un programa que pida números al usuario indefinidamente
hasta meter el número 111
"""
numero = 0
while numero != 111:
    numero = int(input("introduce el número a mostrar. Para salir del programa introduce '111' "))
    print("Has introducido el número ", numero)
    
    print("\n************** FIN DEL PROGRAMA ***************")
