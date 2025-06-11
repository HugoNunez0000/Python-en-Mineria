# Practica 05-23 Viernes

# Back end = logica del sistema
# Front end = parte visual

# # VEREMOS LA INTERFAZ GRAFICA LA PARTE GRAFICA

# #PAQUETE PARA CONSTRUIR INTERFACE GRAFICA:
# from tkinter import *

# crear la ventana principal:

root = Tk()  # ESTA ES LA VENTANA PRINCIPAL QUE EN SU INTERIOR TIENE BOTONES, ETIQUETAS, ESTA VENTANA PRINCIPAL SE LLAMA MASTER O PARENT(PADRE), A LO QUE ESTA DENTRO SE LLAMA CHILD(HIJO)


# configurar la ventana principal

root.title('Mi aplicacion')
root.geometry('800x700')

# para iconos debe estar en formato ico la imagen


# crear y colocar una etiqueta(ELEMENTO GRAFICO)
# label_1 = Label(root, text = 'Esto es una etiqueta')
# # label_1.pack(side = 'left') # Esta funcion "pack" es para mostrar los elementos
# # label_1.pack(pady=30) #pad y es en el eje y, 30 son los pixeles
# label_1.grid(row=4, column=7) #pad y es en el eje y, 30 son los pixeles


# label_2 = Label(root, text = 'Esto es otra etiqueta')
# # label_2.pack(side = 'right')
# label_2.grid(row=2, column=3)


# #DEFINIR UNA FUNCION PARA EL BOTON
def click():
    name = entry.get()
    if name == '':
        messagebox.showerror)

            return

            # CREAR UN BOTON
            button = Button(root, text='ingresar nombre', command=click)
            button.pack()



            # ¿como se coloca algo en pantalla?
            # pack
            # grid


            # Ciclo de refresco La ventana:
            root.mainloop()

            # #RECUPERAR TEXTO:
            # name=entry.get()

            # if name  =='':
            #     text == 'ingrese su nombre...'

            # else:
            #     text=f'hola,{name}!'

            # label = Label

            # #crear una entrada de texto

            # entry = Entry(root)
            # entry.pack()

            # import tkinter as tk

            # root = tk.Tk()
            # root.geometry('400x400')

            # #crear una ventana nuevade
            # def window():

            # #crear una nueva ventana:::

            #     top = tk.Toplevel(root)
            #     top.title('ventana secundaria')
            #     top.geometry('200x200')


            # #añadir boton
            # button = tk.Button(root, text='Nueva ventana', command=window)
            # button.pack(padx=20, pady=10)


            # #Ciclo de refresco La ventana:
            # root.mainloop()
