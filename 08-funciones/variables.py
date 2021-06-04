"""
Variables locales: Se definen dentro de la función y no se puede3 usar fuera 
de ella, sólo están disponibles dentro, al no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una fucnión y están disponibles
dentro y fuera de ellas.
"""

# Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "Hola Mundo!!"
    print(frase)

    year = 2021
    print(year)

    #declaramos la variable website como global y tendremos acceso a ella desde fuera de la función
    global website
    website = "angelach.com"
    print("DENTRO: ", website)

    return "Dato devuelto " + str(year)
    
holaMundo()
print("FUERA: ", website)