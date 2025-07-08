# main.py

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from tkinter.ttk import Combobox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
from componentes import bloque_radiobuttons, puntajes_dict

df = None
puntajes = {
    'Cielo Abierto': 0, 'Block Caving': 0, 'Sublevel Stoping': 0,
    'Sublevel Caving': 0, 'Longwall': 0, 'Room and Pillar': 0,
    'Shrinkage': 0, 'Cut and Fill': 0, 'Top Slicing': 0, 'Square Set': 0
}
metodos = list(puntajes.keys())


def detectar_delimitador(filepath):
    with open(filepath, 'r', newline='', encoding='utf-8') as file:
        sample = file.read(1024)
        dialect = csv.Sniffer().sniff(sample, delimiters=";,")
        return dialect.delimiter


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
        self.delimitador_detectado = ';'

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
            label="Abrir archivo", command=self.open_file_dialog)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.quit)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        self.config(menu=menu_bar)

    def create_menu_separator(self):
        self.separator = tk.Frame(self, height=2, bg="gray")
        self.separator.pack(fill="x")

    def open_file_dialog(self):
        self.top = Toplevel(self)
        self.top.title("Cargar Archivo")
        self.top.geometry("400x500")
        self.top.grab_set()
        self.top.focus_force()
        self.top.transient(self)

        self.file_path = tk.StringVar()
        tk.Label(self.top, text="Ruta del archivo:").pack(pady=10)
        entry_file = tk.Entry(self.top, textvariable=self.file_path, width=50)
        entry_file.pack(pady=5)

        tk.Button(self.top, text="Explorar",
                  command=self.browse_file).pack(pady=5)

        tk.Label(self.top, text="Seleccionar columna para X:").pack(pady=10)
        self.combo_x = Combobox(self.top)
        self.combo_x.pack(pady=5)

        tk.Label(self.top, text="Seleccionar columna para Y:").pack(pady=10)
        self.combo_y = Combobox(self.top)
        self.combo_y.pack(pady=5)

        tk.Label(self.top, text="Seleccionar columna para Z:").pack(pady=10)
        self.combo_z = Combobox(self.top)
        self.combo_z.pack(pady=5)

        tk.Label(self.top, text="Seleccionar columna de ley (CU/AU):").pack(pady=10)
        self.combo_law = Combobox(self.top)
        self.combo_law.pack(pady=5)

        tk.Button(self.top, text="Guardar y cargar",
                  command=self.load_file).pack(pady=20)

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[
                                               ("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            self.file_path.set(file_path)
            try:
                delimitador = detectar_delimitador(file_path)
                self.delimitador_detectado = delimitador
                temp_df = pd.read_csv(file_path, sep=delimitador, nrows=0)
                column_names = temp_df.columns.tolist()
                self.combo_x['values'] = column_names
                self.combo_y['values'] = column_names
                self.combo_z['values'] = column_names
                self.combo_law['values'] = column_names
                if len(column_names) >= 4:
                    self.combo_x.current(0)
                    self.combo_y.current(1)
                    self.combo_z.current(2)
                    self.combo_law.current(3)
            except Exception as e:
                messagebox.showerror(
                    "Error", "Carga un modelo válido.")

    def load_file(self):
        global df
        ruta_archivo = self.file_path.get()
        if not ruta_archivo:
            messagebox.showerror(
                "Error", "Por favor, seleccione un archivo primero.")
            return
        try:
            df = pd.read_csv(ruta_archivo, sep=self.delimitador_detectado)
            cols_seleccionadas = [self.combo_x.get(), self.combo_y.get(
            ), self.combo_z.get(), self.combo_law.get()]
            for col in cols_seleccionadas:
                if col not in df.columns:
                    messagebox.showerror(
                        "Error", f"La columna '{col}' no existe en el archivo.")
                    return
            messagebox.showinfo(
                "Archivo cargado", "Archivo cargado y columnas seleccionadas correctamente.")
            self.after_read()
            self.top.destroy()
        except Exception as e:
            messagebox.showerror(
                "Error de carga", f"Error al cargar el archivo: {e}")

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
        xc = df[self.combo_x.get()]
        yc = df[self.combo_y.get()]
        zc = df[self.combo_z.get()]
        grade = df[self.combo_law.get()]

        ley_col = self.combo_law.get()

        colores = []
        for valor in grade:
            if ley_col == 'CU' or 'Cu' or 'cu':
                if valor <= 0.2:
                    colores.append('#1f77b4')
                elif valor <= 0.6:
                    colores.append('#2ca02c')
                elif valor <= 1.0:
                    colores.append('#ffdf00')
                elif valor <= 1.5:
                    colores.append('#ff7f0e')
                else:
                    colores.append('#d62728')
            else:  # Au
                if valor <= 0.5:
                    colores.append('#1f77b4')
                elif valor <= 1.0:
                    colores.append('#2ca02c')
                elif valor <= 2.0:
                    colores.append('#ffdf00')
                elif valor <= 3.5:
                    colores.append('#ff7f0e')
                else:
                    colores.append('#d62728')
        ax.scatter(xc, yc, zc, c=colores, marker='o')
        ax.set_xlabel(self.combo_x.get())
        ax.set_ylabel(self.combo_y.get())
        ax.set_zlabel(self.combo_z.get())
        ax.set_title('Modelo de Bloques 3D con Colores por Ley')

        unidad = '%' if ley_col == 'Cu' else 'g/t'

        legend_patches = []

        if ley_col == 'CU':
            legend_patches = [
                mpatches.Patch(color='#1f77b4', label='≤ 0.2% Cu (Estéril)'),
                mpatches.Patch(color='#2ca02c', label='0.3 – 0.6% Cu'),
                mpatches.Patch(color='#ffdf00', label='0.7 – 1.0% Cu'),
                mpatches.Patch(color='#ff7f0e', label='1.1 – 1.5% Cu'),
                mpatches.Patch(color='#d62728', label='> 1.5% Cu')
            ]
        else:  # Au
            legend_patches = [
                mpatches.Patch(color='#1f77b4', label='≤ 0.5 g/t Au'),
                mpatches.Patch(color='#2ca02c', label='0.6 – 1.0 g/t Au'),
                mpatches.Patch(color='#ffdf00', label='1.1 – 2.0 g/t Au'),
                mpatches.Patch(color='#ff7f0e', label='2.1 – 3.5 g/t Au'),
                mpatches.Patch(color='#d62728', label='> 3.5 g/t Au')
            ]
        ax.legend(handles=legend_patches, loc='upper right')

        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.frame_izquierdo)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        self.scroll_y_marco()
        self.create_questionnaire()

    def create_frames(self):
        self.frame_izquierdo = tk.Frame(
            self, width=700, height=600, bg="white")
        self.frame_izquierdo.pack(side="left", fill="both", expand=True)

        self.frame_derecho = tk.Frame(
            self, width=300, height=600, bg="lightgray")
        self.frame_derecho.pack(side="right", fill="both", expand=False)

    def scroll_y_marco(self):
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()

        frame_scroll_area = tk.Frame(
            self.frame_derecho, bg="lightgray", highlightbackground="gray", highlightthickness=1)
        frame_scroll_area.pack(side="top", fill="both", expand=True)

        self.canvas_preguntas = tk.Canvas(
            frame_scroll_area, bg="lightgray", highlightthickness=0)
        scrollbar = tk.Scrollbar(
            frame_scroll_area, orient="vertical", command=self.canvas_preguntas.yview)
        self.canvas_preguntas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas_preguntas.pack(side="left", fill="both", expand=True)

        self.frame_preguntas = tk.Frame(self.canvas_preguntas, bg="lightgray")
        self.canvas_window_id = self.canvas_preguntas.create_window(
            (0, 0), window=self.frame_preguntas, anchor="nw")

        self.canvas_preguntas.bind("<Configure>", lambda e: self.canvas_preguntas.itemconfig(
            self.canvas_window_id, width=e.width))
        self.frame_preguntas.bind("<Configure>", lambda e: self.canvas_preguntas.configure(
            scrollregion=self.canvas_preguntas.bbox("all")))

        self.frame_resultados = tk.Frame(
            self.frame_derecho, bg="lightgray", height=242, highlightbackground="gray", highlightthickness=1)
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

        self.label_subtitulo = tk.Label(self.frame_izquierdo, text="Aquí podrás seleccionar el método de explotación según Nicholas",
                                        font=("Arial", 16, "bold"), bg="white", wraplength=600, justify="center")
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

        boton_frame = tk.Frame(self.frame_resultados, bg="lightgray")
        boton_frame.pack(pady=80)

        tk.Button(boton_frame, text="Finalizar y ver resultados", bg='green', fg='white',
                  font=('Arial', 10, 'bold'), padx=20, pady=10, command=self.mostrar_resultados).pack()

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

        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        tk.Label(self.frame_resultados, text="Resultados Totales",
                 bg='gray', fg='white', font=("Arial", 11, "bold")).pack(pady=3)

        resultados_lineas = [
            f"{metodo:<20}: {pts:>3} pts" for metodo, pts in puntajes_local.items()]
        resultados_centrado = "\n".join(resultados_lineas)

        tk.Label(self.frame_resultados, text=resultados_centrado,
                 font=('Courier New', 10), bg='white', justify='center', anchor='center').pack(fill='both', expand=True, padx=10, pady=5)

        tk.Button(self.frame_resultados, text="Finalizar y ver resultados",
                  bg='green', fg='white', command=self.mostrar_resultados).pack(pady=5)


if __name__ == "__main__":
    win = MainWindow()
    win.mainloop()
