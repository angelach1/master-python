import imp
from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("700x400")
ventana.config(bd=70)

# Además de showinfo, están showwarning y showerror
def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola, soy Ángel")
    return True

Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutando la aplicación?")
    if resultado != "yes":
        MessageBox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Ángel Alhambra")).pack()



ventana.mainloop()