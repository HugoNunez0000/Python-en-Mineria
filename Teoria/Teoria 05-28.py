'teoria clase Miercoles Cris'

import tkinter as tk 
from tkinter import ttk
# 'creamos nuestra ventana que se llamara root(raiz en ingles)'

# root = tk.Tk()


# 'Creamos variables globales (es una variable que se utiliza en todo el codigo)'
# contador = 1

# def add_rows():
#     global contador

#     nombre = f"Persona {contador}"
#     edad = str(20 + contador)
#     tree.insert("", "end", values = (nombre, edad))
#     return


# 'parametros de la ventana'
# 'puede ser el titulo, tamaño, etc'
# root.title("Clase 7.1 - Treeviews")
# root.geometry("1000x800")
# root.resizable(False, False)



# 'crear los widgets'
# mi_boton = tk.Button(root, text = 'Presioname')

# #ahora crearemos un frame
# frame_tree = tk.Frame(root)

# scrollbar_tree = ttk.Scrollbar(frame_tree, orient='vertical')
# tree = ttk.Treeview(frame_tree, columns = ("Nombre", "Edad"), show = 'headings', yscrollcommand=scrollbar_tree) #aqui el WIDGET estara dentro del FRAME

# boton_filas = tk.Button(root,text = 'Añadir Filas', command = add_rows) 


# 'colocamos los widgets'
# # mi_boton.pack() #meter el widget en la ventana
# # mi_boton.grid() #divide nuestra ventana en filas y columnas
# # mi_boton.place() #necesita coordenada x,y

# 'colocamos los frames y el widget'
# frame_tree.pack()

# scrollbar_tree.pack(side = 'right', fill = 'y')
# tree.pack(side = 'left', expand = 'True', fill = 'both')
# scrollbar_tree.config(command = tree.yview)




# 'main loop o bucle principal de la ventana'
# root.mainloop()


####
####
####
###OTRO WIDGETS###
###
###
###
import tkinter as tk 
from tkinter import ttk
import pandas as pd # LIBRERIA PARA IMPORTAR ARCHIVOS

from tkinter import ttk, filedialog, messagebox  #filedialog devuelve la ruta del archivo


    #0.VARIABLES GLOBALES   
df = None



'funcion open file'
def open_file():
    global df
    ruta_archivo = filedialog.askopenfilename(title = "Abrir archivo")
    if ruta_archivo:
        df = pd.read_csv(ruta_archivo, sep = ';')
        messagebox.showinfo("Archivo cargado", "Se ha cargado el archivo correctamente")
        print(df)
        after_read()
    return
                                                                                


def after_read():
    global combo_size_x, combo_size_y, combo_size_z

    combo_values = df.columns.tolist()

    combo_size_x['values'] = combo_values
    combo_size_y['values'] = combo_values
    combo_size_z['values'] = combo_values
    

    combo_size_x.config(state = 'readonly')
    combo_size_y.config(state = 'readonly')
    combo_size_z.config(state = 'readonly')
    

    return


#1.CREAR VENTANA
root = tk.Tk()



#2.PARAMETROS DE LA VENTANA
root.title("Clase 7.2 - Combobox")
root.geometry("800x600")
root.resizable(False,False)

#3.CREAR WIDGETS
boton_abrir_archivo = tk.Button(root, text = "Abrir archivo", command = open_file)
'COBOBOX'
frame_combo = tk.Frame(root)
combo_size_x = ttk.Combobox(frame_combo, state = 'disabled')
label_size_x = tk.Label(frame_combo, text = "Tamaño x")
combo_size_y = ttk.Combobox(frame_combo, state = 'disabled')
label_size_y = tk.Label(frame_combo, text = "Tamaño y")
combo_size_z = ttk.Combobox(frame_combo, state = 'disabled')
label_size_z = tk.Label(frame_combo, text = "Tamaño z")


#4.COLOCAR WIDGETS
boton_abrir_archivo.pack(pady = 20) #pady es distancia vertical entre 2 botones


frame_combo.pack(pady = 20)
combo_size_x.grid(row = 0, column = 0, pady = 5)
label_size_x.grid(row = 0, column= 1, pady = 5)
combo_size_y.grid(row = 1, column = 0, pady = 5)
label_size_y.grid(row = 1, column= 1, pady = 5)
combo_size_z.grid(row = 2, column = 0, pady = 5)
label_size_z.grid(row = 2, column= 1, pady = 5)


#5.CREAR BARRA DE MENU
menubar = tk.Menu(root)       #AL PONER tk es la libreria y de esa libreria necesitamos la clase Menu

menubar_file = tk.Menu(menubar, tearoff = 0)
menubar_file.add_command(label = 'Abrir archivo', command = open_file)    

menubar.add_cascade(label = 'Archivo', menu = menubar_file)

root.config(menu = menubar)



#6.MAIN LOOP
root.mainloop()