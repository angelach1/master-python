from tkinter import *

ventana = Tk()
#ventana.geometry("1000x1000")

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.config(
    fg = "white",
    bg = "#000000",
    padx = 50,
    pady = 20,
    font=("Consolas", 30),
    cursor="spider"
)
texto.pack(side=TOP)

texto = Label(ventana, text = "Soy Ángel Alhambra")
texto.config(
    height = 3,
    bg = "orange",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="circle"
)    
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text = "Básico 1")
texto.config(
    height=3,
    fg = "yellow",
    bg = "green",
    padx = 10,
    pady = 20,
    font=("Consolas", 18),
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text = "Básico 2 ")
texto.config(
    height=3,
    fg = "yellow",
    bg = "red",
    padx = 10,
    pady = 20,
    font=("Consolas", 18),
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text = "Básico 3")
texto.config(
    height=3,
    fg = "yellow",
    bg = "blue",
    padx = 10,
    pady = 20,
    font=("Consolas", 18),
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)



ventana.mainloop()
