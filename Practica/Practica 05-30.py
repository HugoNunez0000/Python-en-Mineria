
# import tkinter as tk

# class MainWindow(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.window_variables()
#         self.window_settings()
        
#         self.widgets_create()
#         self.widgets_layout()


#     def window_variables(self):
#         self.WIN_WIDTH = 800
#         self.WIN_HEIGHT = 600

#         self.var_radios = tk.StringVar(value = "Cielo")
#         return
    
#     def window_settings(self):
#         self.title("Clase 8 - Radiobuttons")
#         self.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
#         self.resizable(False, False)
#         return
    
#     def widgets_create(self):
#         self.label_title = tk.Label(self, text = "Radiobuttons", font = ('Arial', 20, 'bold'))



#         self.frame_radios = tk.Frame(self)
#         self.radio_cielo = tk.Radiobutton(self.frame_radios, text = "Cielo abierto", value = "Cielo", variable = self.var_radios, command = self.selected_radio)
#         self.radio_subte = tk.Radiobutton(self.frame_radios, text = "Subterrànea", value = "Subte", variable = self.var_radios, command = self.selected_radio)

#         self.label_resultado = tk.Label(self, text = "")
#         return
    
#     def widgets_layout(self):
#         self.label_title.pack(pady = 15)

#         self.frame_radios.pack()
#         self.radio_cielo.pack()
#         self.radio_subte.pack()
        
#         self.label_resultado.pack(pady = 10)
#         return
    
#     def selected_radio(self):  #"Cielo" o "Subte"
#         click = self.var_radios.get()
#         if click == "Cielo":
#             self.label_resultado.config(text = "Haz seleccionado Cielo")
#         elif click == "Subte":
#             self.label_resultado.config(text = "Haz seleccionado Subterrànea")
#         return
# ##AQUI FALTA EL LOOP Y LLAMAR A LA CLASE

# if __name__ == "__main__": #ESTO EJECUTA EL ARCHIVO SOLO SI LO ESTOY LLAMANDO
#     win = MainWindow()
#     win.mainloop()



######## AHORA VEREMOS CHECKBOX #######


import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_variables()
        self.window_settings()
        self.widgets_create()
        self.widgets_layout()
        return

    def window_variables(self):
         self.WIN_WIDTH = 800
         self.WIN_HEIGHT = 600

         self.var_camion = tk.IntVar()
         self.var_pala = tk.IntVar()
         self.var_dozer = tk.IntVar()

         return

    def window_settings(self):
        self.title("Clase 8 - Checkbuttons.")
        self.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        self.resizable(False,False)
        return
    
    def widgets_create(self):
        self.label_title = tk.Label(self, text = "Clase 8.2 - Checkbuttons", font = ('Arial', 20, 'bold') )

        self.frame_check = tk.Frame(self)
        self.check_camion = tk.Checkbutton(self.frame_check, text = 'Camion', variable = self.var_camion)
        self.check_pala = tk.Checkbutton(self.frame_check, text = 'Pala', variable = self.var_pala)
        self.check_dozer = tk.Checkbutton(self.frame_check, text = 'Buldozer', variable = self.var_dozer)

        self.button_text = tk.Button(self, text = "Siguiente", command = self.selected_check)

        return

    def widgets_layout(self):
        self.label_title.pack(pady = 15)

        self.frame_check.pack()
        self.check_camion.pack()
        self.check_pala.pack()
        self.check_dozer.pack()

        self.button_text.pack(pady = 10)
        return
    
    def selected_check(self):
        selected = []

        if self.var_camion.get():
            selected.append("Camion")
        if self.var_pala.get():
            selected.append("Pala")
        if self.var_dozer.get():
            selected.append("Buldozer")

        print(selected)

        return



if __name__ == "__main__": #ESTO EJECUTA EL ARCHIVO SOLO SI LO ESTOY LLAMANDO
    app = App()
    app.mainloop()
