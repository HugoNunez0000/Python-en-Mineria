import tkinter as tk

root = tk.Tk()

var_1 = tk.IntVar(value=10)
var_2 = tk.IntVar(value=0)

title = tk.Label(root, text='TITULO')
radio_1 = tk.Radiobutton(root, text='Opción 1', variable=var_1, value=0)
radio_2 = tk.Radiobutton(root, text='Opción 2', variable=var_1, value=10)
radio_3 = tk.Radiobutton(root, text='Opción 3', variable=var_1, value=20)

title = tk.Label(root, text='TITULO')
radio_4 = tk.Radiobutton(root, text='Opción 1', variable=var_1, value=0)

# title.pack()
radio_1.pack()
radio_2.pack()
radio_3.pack()

title.pack(pady=(10, 0))
radio_4.pack()


def get_value(event):
    print(var_1.get())


radio_1.bind('<Button-1>', get_value)
radio_2.bind('<Button-1>', get_value)
radio_3.bind('<Button-1>', get_value)

root.mainloop()
