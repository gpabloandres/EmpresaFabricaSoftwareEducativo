from tkinter import *

# Crear la Ventana de la calculadora
ventana = Tk()
ventana.title("Calculadora")

# Visualizar del texto en el display
display = Entry(ventana, font= ("Calibri 20"))
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Definir los botones de números
boton1 = Button(ventana, text="1", width=5, height=2)
boton2 = Button(ventana, text="2", width=5, height=2)
boton3 = Button(ventana, text="3", width=5, height=2)
boton4 = Button(ventana, text="4", width=5, height=2)
boton5 = Button(ventana, text="5", width=5, height=2)
boton6 = Button(ventana, text="6", width=5, height=2)
boton7 = Button(ventana, text="7", width=5, height=2)
boton8 = Button(ventana, text="8", width=5, height=2)
boton9 = Button(ventana, text="9", width=5, height=2)
boton0 = Button(ventana, text="0", width=5, height=2)

# Definir los botones de expresiones
boton_borrar = Button(ventana, text="AC", width=5, height=2)
boton_parentesis_abre = Button(ventana, text="(", width=5, height=2)
boton_parentesis_cierra = Button(ventana, text=")", width=5, height=2)
boton_punto = Button(ventana, text=".", width=5, height=2)

# Definir los botones de las operaciones
boton_dividir = Button(ventana, text="/", width=5, height=2)
boton_multiplicar = Button(ventana, text="x", width=5, height=2)
boton_sumar = Button(ventana, text="+", width=5, height=2)
boton_restar = Button(ventana, text="-", width=5, height=2)
boton_igual = Button(ventana, text="=", width=5, height=2)

# Agregar y ordenar en la ventana los botones definidos. 
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis_abre.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis_cierra.grid(row=1, column=2, padx=5, pady=5)
boton_dividir.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_multiplicar.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sumar.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_restar.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()