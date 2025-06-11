### BINDING ###
### cuando hacemos ctrl c y control v
"""
Este scrpit de Python crea una interfaz en la cual se muestran los ejemplos de como usar binds en tkinter
"""
import tkinter as tk
from tkinter import messagebox
from botoncito import Botoncito

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__() #con super() heredo todas las caracteristicas del construnctor tkinter
        #Creamos las funciones
        self.window_parameters()
        self.window_settings()

        self.widgets_create()
        self.widgets_layout()

        self.widgets_binds()
        return

    def window_parameters(self): #aqui van todas las variables que se van a necesitar para ejecutar esta interfaz
        self.WIDTH = 800 # En mayusculas se escriben los valores que no van a cambiar nunca (siempre seran constantes)
        self.HEIGHT = 600
        self.circle_color = 'white' 
        self.COLORS = ['red', 'blue', 'green', 'white', 'black', 'yellow','chocolate', 'salmon']
        return
    

    def window_settings(self):
        """
        Esta funcion cambia la configuracion de la ventana
        """
        self.title("Clase 20 - Binding")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        return
    

    def widgets_create(self):
        self.label_title = tk.Label(self, text = "Binding", font = ('Arial', 30, 'bold'))

        self.frame_entrada = tk.Frame(self)
        self.entry_color = tk.Entry(self.frame_entrada, width = 15)
        self.button_color = Botoncito(self.frame_entrada, text = '→', command = None, c_borde = '#e1b12c', c_relleno = '#fbc531', borde = 4)

        self.canvas_draw = tk.Canvas(self, width = 500, height = 400, bg = 'black')
        return
    
        


    def widgets_layout(self):
        self.label_title.pack(pady = 15)

        self.frame_entrada.pack()
        self.entry_color.grid(row = 0, column = 0)
        self.button_color.grid(row = 0, column = 1)
        self.canvas_draw.pack(pady = 15)
        return
    

    def widgets_binds(self):
        self.entry_color.bind('<Return>', self.function_button)
        self.canvas_draw.bind('<Button-1>', self.create_circle)
        
        return

    def create_circle(self, event):
        x,y = event.x, event.y
        size = 50

        self.canvas_draw.create_oval(
            x - size / 2,
            y - size / 2,
            x + size / 2,
            y + size / 2,
            fill = self.circle_color
        )
        return

    def function_button(self, event = None):
        color = self.entry_color.get()

        if color not in self.COLORS:
            messagebox.showerror("Error", "No existe ese color.")
        else:
            self.circle_color = color
            self.entry_color.delete(0, tk.END)
        
        
        return

if __name__=='__main__':
    root = MainWindow()
    root.mainloop()
