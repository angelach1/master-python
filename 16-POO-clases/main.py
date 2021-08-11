# Programación orientada a objetos (POO o OOP)

# Definir una clase (molde apra crear más objetos de ese tipo)

class Coche:

    # Atributos o propiedades (variables)
    # Características del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos, son acciones que hace le objeto (coche) (funciones)

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# Fin definición clase

#Crear objetos / Instaciar la clase

coche = Coche()
print(coche)
print(coche.marca, coche.color)
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Velocidad actual: ", coche.velocidad)

coche.frenar()

print("Velocidad actual: ", coche.velocidad)
