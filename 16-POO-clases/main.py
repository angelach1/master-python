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

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# Fin definición clase

#Crear objetos / Instaciar la clase

coche = Coche()
coche.setColor("amarillo")
coche.setModelo("Murciélago")

print(coche.marca, coche.getModelo(), coche.getColor())

print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Velocidad actual: ", coche.getVelocidad())

coche.frenar()

print("Velocidad nueva: ", coche.getVelocidad())

print("---------------------")

#Crear más objetos
coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")
print("COCHE 2:")
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))




