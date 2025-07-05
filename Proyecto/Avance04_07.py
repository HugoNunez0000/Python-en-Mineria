# main.py

import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from componentes import bloque_radiobuttons

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

df = None

puntajes = {
    'Cielo Abierto': 0, 'Block Caving': 0, 'Sublevel Stoping': 0,
    'Sublevel Caving': 0, 'Longwall': 0, 'Room and Pillar': 0,
    'Shrinkage': 0, 'Cut and Fill': 0, 'Top Slicing': 0, 'Square Set': 0
}

metodos = list(puntajes.keys())

puntajes_dict = {
    'geometría': {
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
    'inclinación': {
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


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_variables()
        self.window_settings()
        self.create_menu()
        self.create_menu_separator()
        self.create_frames()
        self.show_welcome_message()
        self.selected_options = {}

    def window_variables(self):
        self.WIN_WIDTH = 1000
        self.WIN_HEIGHT = 600

    def window_settings(self):
        self.title("Metodología de Nicholas")
        self.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        self.resizable(True, True)

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

    def open_file(self):
        global df
        try:
            ruta_archivo = filedialog.askopenfilename(title="Abrir archivo")
            if ruta_archivo:
                df = pd.read_csv(ruta_archivo, sep=';')
                self.after_read()
                messagebox.showinfo("Archivo cargado",
                                    "Se ha cargado el archivo correctamente")
        except:
            messagebox.showerror(
                "Error de carga", "Ingrese un archivo .csv o .txt que represente un modelo de bloques")

    def scroll_y_marco(self):
        # Limpiar si ya existía (por recarga)
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()

        # ----- Panel scrollable (arriba) -----
        frame_scroll_area = tk.Frame(
            self.frame_derecho,
            bg="lightgray",
            highlightbackground="gray",
            highlightthickness=1
        )
        frame_scroll_area.pack(side="top", fill="both", expand=True)

        self.canvas_preguntas = tk.Canvas(
            frame_scroll_area, bg="lightgray", highlightthickness=0)
        scrollbar = tk.Scrollbar(
            frame_scroll_area, orient="vertical", command=self.canvas_preguntas.yview)
        self.canvas_preguntas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas_preguntas.pack(side="left", fill="both", expand=True)

        self.frame_preguntas = tk.Frame(self.canvas_preguntas, bg="lightgray")

        # Guardamos el ID del window creado
        self.canvas_window_id = self.canvas_preguntas.create_window(
            (0, 0),
            window=self.frame_preguntas,
            anchor="nw"
        )
        self.canvas_preguntas.bind(
            "<Configure>",
            lambda e: self.canvas_preguntas.itemconfig(
                self.canvas_window_id, width=e.width)
        )
        self.frame_preguntas.bind(
            "<Configure>",
            lambda e: self.canvas_preguntas.configure(
                scrollregion=self.canvas_preguntas.bbox("all"))
        )

        # ----- Panel de resultados (abajo) -----
        self.frame_resultados = tk.Frame(
            self.frame_derecho,
            bg="lightgray",
            height=242,
            highlightbackground="gray",
            highlightthickness=1
        )
        self.frame_resultados.pack(side="bottom", fill="x")
        self.frame_resultados.pack_propagate(False)

        self.bind_mousewheel()

    def create_frames(self):

        self.frame_izquierdo = tk.Frame(
            self, width=700, height=600, bg="white")
        self.frame_izquierdo.pack(side="left", fill="both", expand=True)

        # El frame_derecho se mantiene, pero vacío inicialmente
        self.frame_derecho = tk.Frame(
            self, width=300, height=600, bg="lightgray")
        self.frame_derecho.pack(side="right", fill="both", expand=False)

    def bind_mousewheel(self):
        def _on_mousewheel(event):
            self.canvas_preguntas.yview_scroll(
                int(-1 * (event.delta / 120)), "units")
        self.canvas_preguntas.bind_all("<MouseWheel>", _on_mousewheel)

    def show_welcome_message(self):
        self.label_bienvenida = tk.Label(
            self.frame_izquierdo,
            text="¡Bienvenido!",
            font=("Arial", 20, "bold"),
            bg="white",
            justify="center"
        )
        self.label_bienvenida.place(relx=0.5, rely=0.4, anchor="center")

        self.label_subtitulo = tk.Label(
            self.frame_izquierdo,
            text="Aquí podrás seleccionar el método de explotación según Nicholas",
            font=("Arial", 16, "bold"),
            bg="white",
            wraplength=600,
            justify="center"
        )
        self.label_subtitulo.place(relx=0.5, rely=0.5, anchor="center")

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
        xc, yc, zc = df['XC'], df['YC'], df['ZC']
        grade = df['CU']
        ax.scatter(xc, yc, zc, c=grade, marker='o')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Modelo de bloques 3D')
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.frame_izquierdo)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        # 🚀 Aquí se crea el panel derecho completo
        self.scroll_y_marco()

        # Luego las preguntas
        self.create_questionnaire()

    def create_questionnaire(self):
        for categoria, opciones in puntajes_dict.items():
            bloque_radiobuttons(
                frame_padre=self.frame_preguntas,
                categoria=categoria,
                opciones=opciones,
                callback=self.aplicar_puntaje,
                selected_option_dict=self.selected_options
            )
        # Frame contenedor centrado
        boton_frame = tk.Frame(self.frame_resultados, bg="lightgray")
        boton_frame.pack(pady=80)  # aumenta separación superior

        # Botón centrado dentro del frame
        tk.Button(
            boton_frame,
            text="Finalizar y ver resultados",
            bg='green',
            fg='white',
            font=('Arial', 10, 'bold'),   # fuente más grande y clara
            padx=20,                      # espacio interno horizontal
            pady=10,                      # espacio interno vertical
            command=self.mostrar_resultados
        ).pack()
        # Cambia aplicar_puntaje para que SOLO DEVUELVA la lista de valores:

    def aplicar_puntaje(self, categoria, selected_option):
        opcion = selected_option.get()
        if categoria in puntajes_dict and opcion in puntajes_dict[categoria]:
            return puntajes_dict[categoria][opcion]
        return None

    # Cambia mostrar_resultados para que use un diccionario local nuevo:

    def mostrar_resultados(self):
        puntajes_local = {metodo: 0 for metodo in puntajes}

        for categoria, var in self.selected_options.items():
            valores = self.aplicar_puntaje(categoria, var)
            if valores:
                for i, metodo in enumerate(metodos):
                    if valores[i] != -49:
                        puntajes_local[metodo] += valores[i]

        # Limpia solo los widgets que NO sean el botón (para evitar que desaparezca)
        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        # Mostrar título
        tk.Label(self.frame_resultados, text="Resultados Totales",
                 bg='gray',
                 fg='white',
                 font=("Arial", 11, "bold")).pack(pady=3)

    # 1. Formatear resultados como tabla
        resultados_lineas = [
            f"{metodo:<20}: {pts:>3} pts" for metodo, pts in puntajes_local.items()
        ]
        resultados_centrado = "\n".join(resultados_lineas)

        # 2. Mostrar usando Label centrado
        tk.Label(
            self.frame_resultados,
            text=resultados_centrado,
            font=('Courier New', 10),
            bg='white',
            justify='center',
            anchor='center'
        ).pack(fill='both', expand=True, padx=10, pady=5)

        # Crear nuevamente el botón para poder presionar varias veces
        tk.Button(self.frame_resultados, text="Finalizar y ver resultados",
                  bg='green', fg='white', command=self.mostrar_resultados).pack(pady=5)


if __name__ == "__main__":
    win = MainWindow()
    win.mainloop()
