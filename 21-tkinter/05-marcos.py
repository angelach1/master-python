from cmath import exp
from tkinter import *

ventana = Tk()
ventana.title("Marcos | Máster en Python")
ventana.geometry("1000x1000")

marco_padre = Frame(ventana, width=300, height=300)
marco_padre.config(
    bg="lightblue",
    bd=5,
    relief="ridge"
)

marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=300, height=300)
marco.config(
    bg="red",
    bd=5,
    relief=SOLID
)

marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False) # Esto evita que el marco se contraiga al insertarle un Label

texto = Label(marco, text="Primer marco") 
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    height=10,
    width=10,
    bd=3
)
texto.pack(anchor=CENTER, fill=Y, expand=YES)


marco = Frame(marco_padre, width=300, height=300)
marco.config(
    bg="green",
    bd=5,
    relief="solid"
)

marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=300, height=300)
marco_padre.config(
    bg="lightblue",
    bd=5,
    relief="ridge"
)

marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco = Frame(marco_padre, width=300, height=300)
marco.config(
    bg="blue",
    bd=5,
    relief="solid"
)

marco.pack(side=LEFT)

marco = Frame(marco_padre, width=300, height=300)
marco.config(
    bg="orange",
    bd=5,
    relief="solid"
)

marco.pack(side=RIGHT)

ventana.mainloop()