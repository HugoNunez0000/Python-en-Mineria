import tkinter as tk

# class LabelEntry:

#     # def __init__(self, parent, label = ''):
#     #     #Label 2
#     #     label_2 = tk.Label(parent, text = 'Densidad de la roca')
#     #     label_2.grid(row = 1, column = 0, sticky = 'w')

#     #     entry_2 = tk.Entry(parent)
#     #     entry_2.grid(row = 1, column = 1)

#     #     units_2 = tk.Label(parent, text = 'g/cm3')
#     #     units_2.grid(row = 1, column = 2, sticky = 'w')

class LabelEntry(tk.Frame):
    '''Entrada de texto con etiquetas'''

    def __init__(self, parent, label = '', units = ''):

        #configurar el frame:
        super().__init__(parent)

        #crear la etiqueta del nombre:
        self.label = tk.Label(self, text = label)
        self.label.grid(row = 0, column = 0, sticky = ' w')

        #crear entrada de texto:
        self.entry = tk.Entry(self)
        self.entry.grid(row = 0, column = 1)

        #crear unidad de medida
        self.units = tk.Label(self, text = units)
        self.units.grid(row = 0, column = 2)


# root = tk.Tk()

# entry_1 = LabelEntry(root, label = 'Densidad de roca', units = 'g/cm3')
# entry_1.pack()

# root.mainloop()