"""
Crear un programa que tenga:
(x) Ventana
(x) Tamaño fijo
(x) No redimensionable
(x) Un menu (inicio, Añadir, Información, Salir)
(x) Salir
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
"""

from tkinter import *

# Definir ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter - Máster en Python")
ventana.resizable(0, 0)

# Pantallas
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
    )
    home_label.grid(row=0, column=0)

    # Ocultar las otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
    )
    add_label.grid(row=0, column=0)

    # Ocultar las otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    # Ocultar las otras pantallas
    add_label.grid_remove()
    home_label.grid_remove()

    return True

# Definir campos de pantalla (INICIO)
home_label = Label(ventana, text="Inicio")

# Definir campos de pantalla (AÑADIR)
add_label = Label(ventana, text="Añadir Producto")

# Definir campos de pantalla (INFO)
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Ángel Alhambra - 2022")
# Cargar pantalla incio
home()

# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar menú
ventana.config(menu=menu_superior)



# Cargar ventana
ventana.mainloop()