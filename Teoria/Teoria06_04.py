import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import ttk


# # root = tk.Tk()

# # combo = Combobox(root, values = ['a', 'b', 'c', 'd', 'e'], state = 'readonly') #state normal. disabled y readonly
# # combo.pack(padx = 20, pady = 20)

# # # combo.set('a')

# # #definir una funcion que depende de un evento:

# # def get_value(event):
# #     print(combo.get()) #funcion get para recuperar algo


# # # combo.bind('<<ComboboxSelected>>', get_value)
# # combo.bind('<Button-1>', get_value)
# # root.mainloop()

# #################
# #################
# #TRABAJO CON 4
# #FRAMES##########
# #################

# import tkinter as tk
# from tkinter.ttk import Treeview

# #Ventana principal:
# root = tk.Tk()


# #Crear una ventana secundaria:
# window = tk.Toplevel(root)


# #Creamos los marcos para colocar elementos:
# frame_1 = tk.Frame(window, bg = 'red', width = 100, height = 100)
# frame_2 = tk.Frame(window, bg = 'blue', width = 100, height = 100)
# frame_3 = tk.Frame(window, bg = 'green', width = 100, height = 100)
# frame_4 = tk.Frame(window, bg = 'magenta', width = 100, height = 100)

# #Colocamos el frame
# frame_1.pack(fill = 'both', side = 'left')
# frame_2.pack(fill = 'both')
# frame_3.pack(fill = 'both')
# frame_4.pack(fill = 'both')

# #Label 1
# label_1 = tk.Label(frame_2, text = 'Nombre de la roca')
# label_1.grid(row = 0, column = 0, sticky = 'w')

# entry_1 = tk.Entry(frame_2)
# entry_1.grid(row = 0, column = 1)

# #Label 2
# label_2 = tk.Label(frame_2, text = 'Densidad de la roca')
# label_2.grid(row = 1, column = 0, sticky = 'w')

# entry_2 = tk.Entry(frame_2)
# entry_2.grid(row = 1, column = 1)

# units_2 = tk.Label(frame_2, text = 'g/cm3')
# units_2.grid(row = 1, column = 2, sticky = 'w')

# #Ciclo principal:
# root.mainloop()

import tkinter as tk

class RockDatabase(tk.Toplevel):
    '''Ventana para base de datos de la roca'''

    def __init__(self, parent):
        super().__init__(parent)

        #configurar la ventana:
        self.title('Base de datos - Roca')

    def create_widgets(self):
        '''Crear los elementos graficos'''
         
         #1. Crear el marco para tabla:
         self.frame_table = tk.Frame(self)
        
        #2. Crear un marco para los parametros:
        self.frame_params = tk.Frame(self)

        self.entry_name



    def widgets_layout(self):
        '''Colocar los elementos graficos'''




root = tk.Tk()
win = RockDatabase(root)
root.mainloop()