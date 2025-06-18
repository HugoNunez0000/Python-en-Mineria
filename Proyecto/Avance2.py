import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Variables globales
df = None
puntajes = {
    'Cielo Abierto': 0,
    'Block Caving': 0,
    'Sublevel Stoping': 0,
    'Sublevel Caving': 0,
    'Longwall': 0,
    'Room and Pillar': 0,
    'Shrinkage': 0,
    'Cut and Fill': 0,
    'Top Slicing': 0,
    'Square Set': 0
}
metodos = list(puntajes.keys())

puntajes_dict = {
    'geometria': {
        'Masivo': [3, 4, 2, 3, -49, 0, 2, 0, 3, 0],
        'Tabular': [2, 2, 2, 4, 4, 4, 2, 4, 3, 2],
        'Irregular': [3, 0, 1, 1, -49, 2, 1, 2, 0, 4],
    },
    'potencia': {
        'Baja (0-10m)': [2, -49, 1, -49, 4, 4, 1, 4, -49, 4],
        'Intermedia (10-30m)': [3, 0, 2, 0, 0, 2, 2, 4, 0, 4],
        'Potente (30-100m)': [4, 2, 4, 4, -49, -49, 4, 0, 3, 1],
        'Muy potente (>100m)': [4, 4, 3, 4, -49, -49, 3, 0, 4, 1],
    },
    'inclinacion': {
        'Horizontal (0-20°)': [3, 3, 2, 1, 4, 4, 2, 0, 4, 2],
        'Intermedio (20-55°)': [3, 2, 1, 1, 0, 1, 1, 3, 1, 3],
        'Vertical (>55°)': [4, 4, 4, 4, -49, 0, 4, 4, 2, 3],
    },
    'leyes': {
        'Uniforme': [3, 4, 3, 4, 4, 3, 3, 3, 4, 3],
        'Gradual': [3, 2, 3, 2, 2, 3, 2, 3, 2, 3],
        'Errática': [3, 0, 1, 0, 0, 3, 1, 3, 0, 3],
    },
    'competencia_macizo': {
        'Baja (<2)': [3, 4, -49, 0, 4, 0, 1, 3, 2, 4],
        'Media (2-4)': [4, 1, 3, 3, 1, 3, 3, 2, 3, 1],
        'Alta (>4)': [4, 1, 4, 3, 0, 4, 4, 2, 3, 1],
    },
    'espaciado': {
        'Muy cercano (>16 ff/m)': [2, 4, 0, 0, 4, 0, 0, 3, 1, 4],
        'Cercano (10-16 ff/m)': [3, 4, 0, 2, 4, 1, 1, 3, 1, 4],
        'Espaciado (3-10 ff/m)': [4, 3, 1, 4, 0, 2, 3, 2, 2, 2],
        'Muy espaciado (<3 ff/m)': [4, 0, 4, 4, 0, 4, 4, 2, 4, 1],
    },
    'competencia_estructuras': {
        'Baja': [2, 4, 0, 0, 4, 0, 0, 3, 1, 4],
        'Media': [3, 3, 2, 2, 3, 2, 2, 3, 2, 3],
        'Alta': [1, 0, 4, 2, 0, 4, 4, 2, 4, 2],
    },
}


def aplicar_puntaje(categoria, opcion):
    if categoria in puntajes_dict and opcion in puntajes_dict[categoria]:
        valores = puntajes_dict[categoria][opcion]
        for i, metodo in enumerate(metodos):
            if valores[i] != -49:
                puntajes[metodo] += valores[i]


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_variables()
        self.window_settings()
        self.create_menu()
        self.create_menu_separator()
        self.create_frames()
        self.show_welcome_message()

    def window_variables(self):
        self.WIN_WIDTH = 1000
        self.WIN_HEIGHT = 800

    def window_settings(self):
        self.title("Metodología de Nicholas")
        self.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        self.resizable(False, False)

    def create_menu(self):
        menu_bar = tk.Menu(self)
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(label="Abrir archivo", command=self.open_file)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.quit)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        self.config(menu=menu_bar)

    def create_menu_separator(self):
        self.separator = tk.Frame(self, height=2, bg="gray")
        self.separator.pack(fill="x")

    def create_frames(self):
        self.frame_izquierdo = tk.Frame(
            self, width=700, height=600, bg="white")
        self.frame_izquierdo.pack(side="left", fill="both", expand=False)

        self.frame_derecho = tk.Frame(
            self, width=300, height=600, bg="lightgray")
        self.frame_derecho.pack(side="right", fill="both", expand=True)

    def show_welcome_message(self):
        self.label_bienvenida = tk.Label(self.frame_izquierdo, text="¡Bienvenido!", font=(
            "Arial", 20, "bold"), bg="white", justify="center")
        self.label_bienvenida.place(relx=0.5, rely=0.4, anchor="center")

        self.label_subtitulo = tk.Label(
            self.frame_izquierdo,
            text="Aquí podrás Seleccionar el Método de Explotación según Nicholas",
            font=("Arial", 16, "bold"),
            bg="white",
            wraplength=600,
            justify="center")
        self.label_subtitulo.place(relx=0.5, rely=0.5, anchor="center")

        self.show_options()

    def show_options(self):
        canvas = tk.Canvas(self.frame_derecho, bg='lightgray')
        scrollbar = tk.Scrollbar(
            self.frame_derecho, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg='lightgray')

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for categoria, opciones in puntajes_dict.items():
            tk.Label(scroll_frame, text=categoria.upper(), bg='gray', fg='white', font=(
                'Arial', 10, 'bold')).pack(pady=5, fill='x')
            for opcion in opciones:
                tk.Button(scroll_frame, text=opcion, command=lambda c=categoria,
                          o=opcion: aplicar_puntaje(c, o)).pack(pady=2, fill='x')

        tk.Button(scroll_frame, text="Finalizar y ver resultado", bg='green',
                  fg='white', command=self.mostrar_resultado).pack(pady=20)

    def mostrar_resultado(self):
        mejor3 = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)[:3]
        resultado = "\n".join(
            [f"{metodo}: {pts} pts" for metodo, pts in mejor3])
        messagebox.showinfo("Mejores métodos según Nicholas", resultado)

    def open_file(self):
        global df
        ruta_archivo = filedialog.askopenfilename(title="Abrir archivo")
        if ruta_archivo:
            df = pd.read_csv(ruta_archivo, sep=';')
            messagebox.showinfo("Archivo cargado",
                                "Se ha cargado el archivo correctamente")
            print(df)
            self.after_read()

    def after_read(self):
        if df is None:
            messagebox.showerror("Error", "No se ha cargado ningún archivo")
            return

        if hasattr(self, 'label_bienvenida') and self.label_bienvenida.winfo_exists():
            self.label_bienvenida.destroy()

        for widget in self.frame_izquierdo.winfo_children():
            widget.destroy()

        fig = plt.figure(figsize=(7, 6))
        ax = fig.add_subplot(111, projection='3d')

        df_plot = df.head(1000)

        for _, row in df_plot.iterrows():
            xc, yc, zc = row['XC'], row['YC'], row['ZC']
            dx, dy, dz = row['XINC'], row['YINC'], row['ZINC']
            x = xc - dx / 2
            y = yc - dy / 2
            z = zc - dz / 2

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
        ax.set_title('Modelo de bloques 3D')
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.frame_izquierdo)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)


if __name__ == "__main__":
    win = MainWindow()
    win.mainloop()
