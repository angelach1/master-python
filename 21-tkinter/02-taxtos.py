from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.config(
    fg = "white",
    bg = "#000000",
    padx = 50,
    pady = 20,
    font=("Consolas", 30),
    cursor="spider"
)
texto.pack()

texto = Label(ventana, text = "Soy Ángel Alhambra")
texto.config(
    height = 3,
    bg = "orange",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="circle"
)    
texto.pack(anchor = SE)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

# En las llamadas a métodos y funciones, si anteponemos el nombre del parámetro al valor,
# los podemos poner en el orden que queramos.
# Esto es muy útil cuando usamos métodos y funciones con muchos parámetros.
texto = Label(ventana, text = pruebas(pais="España", nombre="Ángel", apellidos="Alhambra"))
texto.config(
    height=3,
    fg = "yellow",
    bg = "green",
    padx = 10,
    pady = 20,
    font=("Consolas", 18),
    cursor="spider"
)
texto.pack(anchor = NW)



ventana.mainloop()
