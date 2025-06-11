

import tkinter as tk

class Botoncito(tk.Frame): #Con esto digo que mi clase es un frame
    def __init__(self, parent, text, command, c_borde, c_relleno, borde = 3, *args, **kwargs): # el parent es donde va a ir mi widget
        super().__init__(parent, *args)
        self.parent = parent
        self.text = text
        self.command = command
        self.c_borde = c_borde
        self.c_relleno = c_relleno
        self.borde = borde

        self.config(
            highlightbackground = self.c_borde,
            highlightthickness = self.borde
        )

        button = tk.Button(
            self,
            text = self.text,
            command = self.command,
            bg = self.c_relleno,
            bd = 0,
            **kwargs
        )
        button.pack()