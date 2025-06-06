'''VEREMOS DOCSTRINGS QUE ES PARA COMUNICARSE CON EL USUARIO'''

# def myfun(nombre: str, num1: int, num2: float):

#     # if type(nombre) !=str:
#     #     raise ValueError:
#     print(f"Te llamas {nombre} y nel resultado es {num1+num2}")
#     return


# myfun()


# #TRABAJO CON 4
# #FRAMES##########
# #################

import tkinter as tk
from tkinter.ttk import Treeview
from Teoria.Teoria06_04 import RockDatabase


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_parameters()
        self.window_settings()
        
        self.widgets_create()
        self.widgets_layouts()

    
    def window_parameters(self):
        self.WIDGHT = 300
        self.HEIGHT = 300
        return
    
    def window_settings(self):
        self.title("Ventana Principal")
        self.geometry(f"{self.WIDGHT}x{self.HEIGHT}")
        self.resizable(False,False)
        return
    
    def widgets_create(self):
        self.label_title = tk.Label(self,text = "Base de datos", font = ('Times New Roman', 25, 'bold'))

        self.frame_buttons = tk.Frame(self)
        self.button_rock = tk.Button(self.frame_buttons, text = 'Roca', font = ('Arial', 15), width=20, command = open)
        self.button_explosive = tk.Button(self.frame_buttons, text = 'Explosivos', font = ('Arial', 15),width=20)
        self.button_teams = tk.Button(self.frame_buttons, text = 'Equipos', font = ('Arial', 15),width=20)
        return
    
    def widgets_layouts(self):
        self.label_title.pack(anchor = 'w')

        self.frame_buttons.pack(pady = 20)
        self.button_rock.pack(pady = 5)
        self.button_explosive.pack(pady = 5)
        self.button_teams.pack(pady = 5)
        return
    
    def open_rock_database(self):
        win = RockDatabase()
        return
    
if __name__ == '__main__': ### el name ==  main hace que cuando le pongamos play haga algo
    app = MainWindow()
    #Ciclo principal:
    app.mainloop()