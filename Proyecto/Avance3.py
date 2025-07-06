import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from tkinter.ttk import Combobox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# Importamos el diccionario
from componentes import bloque_radiobuttons, puntajes_dict

df = None
column_names = []  # Para almacenar los nombres de las columnas

puntajes = {
    'Cielo Abierto': 0, 'Block Caving': 0, 'Sublevel Stoping': 0,
    'Sublevel Caving': 0, 'Longwall': 0, 'Room and Pillar': 0,
    'Shrinkage': 0, 'Cut and Fill': 0, 'Top Slicing': 0, 'Square Set': 0
}

metodos = list(puntajes.keys())


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
        archivo_menu.add_command(
            label="Cargar archivo", command=self.open_file_dialog)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.quit)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        self.config(menu=menu_bar)

    def create_menu_separator(self):
        self.separator = tk.Frame(self, height=2, bg="gray")
        self.separator.pack(fill="x")

    def open_file_dialog(self):
        # Crear una ventana emergente para cargar el archivo
        self.top = Toplevel(self)
        self.top.title("Cargar Archivo")
        self.top.geometry("400x200")

        # Campo para la ruta del archivo
        self.file_path = tk.StringVar()
        tk.Label(self.top, text="Ruta del archivo:").pack(pady=10)
        entry_file = tk.Entry(self.top, textvariable=self.file_path, width=50)
        entry_file.pack(pady=5)

        # Botón para explorar archivos
        tk.Button(self.top, text="Explorar",
                  command=self.browse_file).pack(pady=5)

        # Botón para guardar y cargar el DataFrame
        tk.Button(self.top, text="Guardar",
                  command=self.open_column_selection).pack(pady=20)

    def browse_file(self):
        # Método para abrir el explorador de archivos
        file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[
                                               ("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            self.file_path.set(file_path)

    def open_column_selection(self):
        global df, column_names
        try:
            # Cargar el archivo CSV
            ruta_archivo = self.file_path.get()
            if ruta_archivo:
                # Leer el archivo completo para obtener los nombres de las columnas
                # Cambia el separador si es necesario
                df = pd.read_csv(ruta_archivo, sep=';')
                column_names = df.columns.tolist()  # Obtener nombres de columnas

                # Crear un nuevo Toplevel para seleccionar columnas
                self.column_selection_window(column_names)

            else:
                messagebox.showerror(
                    "Error", "Por favor, seleccione un archivo.")
        except Exception as e:
            messagebox.showerror(
                "Error de carga", f"Error al cargar el archivo: {e}")

    def column_selection_window(self, column_titles):
        column_window = Toplevel(self)
        column_window.title("Seleccionar Columnas")
        column_window.geometry("400x300")

        # Combobox para seleccionar las columnas
        tk.Label(column_window, text="Seleccionar columna para X:").pack(pady=10)
        self.combo_x = Combobox(column_window, values=column_titles)
        self.combo_x.pack(pady=5)

        tk.Label(column_window, text="Seleccionar columna para Y:").pack(pady=10)
        self.combo_y = Combobox(column_window, values=column_titles)
        self.combo_y.pack(pady=5)

        tk.Label(column_window, text="Seleccionar columna para Z:").pack(pady=10)
        self.combo_z = Combobox(column_window, values=column_titles)
        self.combo_z.pack(pady=5)

        tk.Label(column_window,
                 text="Seleccionar columna de ley (CU/AU):").pack(pady=10)
        self.combo_law = Combobox(column_window, values=column_titles)
        self.combo_law.pack(pady=5)

        # Botón para confirmar selección de columnas
        tk.Button(column_window, text="Confirmar Selección",
                  command=self.confirm_column_selection).pack(pady=20)

    def confirm_column_selection(self):
        if df is not None:
            self.after_read()

    def after_read(self):
        if df is None:
            messagebox.showerror("Error", "No se ha cargado ningún archivo")
            return

        for widget in self.frame_izquierdo.winfo_children():
            widget.destroy()

        # Obtener los nombres de las columnas seleccionadas
        col_x = self.combo_x.get()
        col_y = self.combo_y.get()
        col_z = self.combo_z.get()
        col_law = self.combo_law.get()

        # Crear el gráfico 3D
        fig = plt.figure(figsize=(7, 6))
        ax = fig.add_subplot(111, projection='3d')

        # Usar los nombres de las columnas seleccionadas
        xc = df[col_x]
        yc = df[col_y]
        zc = df[col_z]
        grade = df[col_law]

        ax.scatter(xc, yc, zc, c=grade, marker='o')
        ax.set_xlabel(col_x)  # Etiqueta X con el nombre de la columna
        ax.set_ylabel(col_y)  # Etiqueta Y con el nombre de la columna
        ax.set_zlabel(col_z)  # Etiqueta Z con el nombre de la columna
        ax.set_title('Modelo de bloques 3D')
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.frame_izquierdo)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        self.create_questionnaire()

    def create_frames(self):
        self.frame_izquierdo = tk.Frame(
            self, width=700, height=600, bg="white")
        self.frame_izquierdo.pack(side="left", fill="both", expand=True)

        self.frame_derecho = tk.Frame(
            self, width=300, height=600, bg="lightgray")
        self.frame_derecho.pack(side="right", fill="both", expand=False)

        # ----- Frame superior con scroll -----
        frame_scroll_area = tk.Frame(self.frame_derecho, bg="lightgray")
        frame_scroll_area.pack(side="top", fill="both", expand=True)

        self.canvas_preguntas = tk.Canvas(
            frame_scroll_area, bg="lightgray", highlightthickness=0)
        scrollbar = tk.Scrollbar(
            frame_scroll_area, orient="vertical", command=self.canvas_preguntas.yview)
        self.canvas_preguntas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas_preguntas.pack(side="left", fill="both", expand=True)

        self.frame_preguntas = tk.Frame(self.canvas_preguntas, bg="lightgray")
        self.canvas_preguntas.create_window(
            (0, 0), window=self.frame_preguntas, anchor="nw")

        self.frame_preguntas.bind("<Configure>", lambda e: self.canvas_preguntas.configure(
            scrollregion=self.canvas_preguntas.bbox("all")))

        # ----- Frame inferior con borde negro -----
        self.frame_resultados = tk.Frame(
            self.frame_derecho, bg="lightgray", height=200, highlightbackground="gray", highlightthickness=2)
        self.frame_resultados.pack(side="bottom", fill="x")
        self.frame_resultados.pack_propagate(False)

        self.bind_mousewheel()

    def bind_mousewheel(self):
        def _on_mousewheel(event):
            self.canvas_preguntas.yview_scroll(
                int(-1 * (event.delta / 120)), "units")
        self.canvas_preguntas.bind_all("<MouseWheel>", _on_mousewheel)

    def show_welcome_message(self):
        self.label_bienvenida = tk.Label(self.frame_izquierdo, text="¡Bienvenido!", font=(
            "Arial", 20, "bold"), bg="white", justify="center")
        self.label_bienvenida.place(relx=0.5, rely=0.4, anchor="center")

        self.label_subtitulo = tk.Label(self.frame_izquierdo, text="Aquí podrás seleccionar el método de explotación según Nicholas", font=(
            "Arial", 16, "bold"), bg="white", wraplength=600, justify="center")
        self.label_subtitulo.place(relx=0.5, rely=0.5, anchor="center")

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

    def aplicar_puntaje(self, categoria, selected_option):
        opcion = selected_option.get()
        if categoria in puntajes_dict and opcion in puntajes_dict[categoria]:
            return puntajes_dict[categoria][opcion]
        return None

    def mostrar_resultados(self):
        puntajes_local = {metodo: 0 for metodo in puntajes}

        for categoria, var in self.selected_options.items():
            valores = self.aplicar_puntaje(categoria, var)
            if valores:
                for i, metodo in enumerate(metodos):
                    if valores[i] != -49:
                        puntajes_local[metodo] += valores[i]

        resultados = "\n".join(
            [f"{metodo}: {pts} pts" for metodo, pts in puntajes_local.items()])

        # Limpia solo los widgets que NO sean el botón (para evitar que desaparezca)
        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        # Mostrar título
        tk.Label(self.frame_resultados, text="Resultados Totales",
                 font=("Arial", 11, "bold")).pack(pady=3)

        # Mostrar resultados en Text
        text_resultados = tk.Text(
            self.frame_resultados, height=6, font=('Courier', 10), wrap='none')
        text_resultados.pack(fill='both', expand=True, padx=5, pady=5)

        text_resultados.insert('1.0', resultados)
        text_resultados.configure(state='disabled')

        # Crear nuevamente el botón para poder presionar varias veces
        tk.Button(self.frame_resultados, text="Finalizar y ver resultados",
                  bg='green', fg='white', command=self.mostrar_resultados).pack(pady=5)


if __name__ == "__main__":
    win = MainWindow()
    win.mainloop()
