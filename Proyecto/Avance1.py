

import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# Variables Globales
# 0.VARIABLES GLOBALES
df = None


# 'funcion open file'


def open_file():
    global df
    ruta_archivo = filedialog.askopenfilename(title="Abrir archivo")
    if ruta_archivo:
        df = pd.read_csv(ruta_archivo, sep=';')
        messagebox.showinfo("Archivo cargado",
                            "Se ha cargado el archivo correctamente")
        print(df)
        after_read()
    return

# Función after_read


def after_read():
    if df is None:
        messagebox.showerror("Error", "No se ha cargado ningún archivo")
        return

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Opcional: limitar cantidad de bloques para que no sature la gráfica
    df_plot = df.head(1000)

    for _, row in df_plot.iterrows():
        xc, yc, zc = row['XC'], row['YC'], row['ZC']
        dx, dy, dz = row['XINC'], row['YINC'], row['ZINC']

        # Calculamos el origen (esquina inferior) del cubo
        x = xc - dx / 2
        y = yc - dy / 2
        z = zc - dz / 2

        # Generamos los vértices del cubo
        vertices = [
            [x, y, z],
            [x + dx, y, z],
            [x + dx, y + dy, z],
            [x, y + dy, z],
            [x, y, z + dz],
            [x + dx, y, z + dz],
            [x + dx, y + dy, z + dz],
            [x, y + dy, z + dz],
        ]

        # Definimos las caras del cubo
        caras = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[4], vertices[7], vertices[3], vertices[0]]
        ]

        ax.add_collection3d(Poly3DCollection(
            caras, facecolors='lightblue', linewidths=0.5, edgecolors='gray', alpha=0.8))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Modelo de bloques 3D')
    plt.tight_layout()
    plt.show()


# AHORA CREAMOS LA CLASE

class MainWindow(tk.Tk):  # Esta es una clase que es una ventana
    def __init__(self):
        super().__init__()
        self.window_variables()
        self.window_settings()

        self.widgets_create()
        self.widgets_layout()

    def window_variables(self):
        self.WIN_WIDTH = 800  # Aqui definimos la geometría de la ventana
        self.WIN_HEIGHT = 600

    def widgets_create(self):
        self.btn_cargar = tk.Button(
            self, text="Cargar archivo", command=open_file)

    def widgets_layout(self):
        self.btn_cargar.pack(pady=20)
        return


# Estos son los parámetros de la ventana (titulo, geomtría)


    def window_settings(self):
        self.title("Metodología de Nicholas")
        self.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        self.resizable(False, False)
        return


# AQUI FALTA EL LOOP Y LLAMAR A LA CLASE


if __name__ == "__main__":  # ESTO EJECUTA EL ARCHIVO SOLO SI LO ESTOY LLAMANDO
    win = MainWindow()
    win.mainloop()
