# componentes.py

import tkinter as tk

# Diccionario de puntajes
puntajes_dict = {
    'geometria': {
        'Masivo': [3, 4, 2, 3, -49, 0, 2, 0, 3, 0],
        'Tabular': [2, 2, 2, 4, 4, 4, 2, 4, 3, 2],
        'Irregular': [3, 0, 1, 1, -49, 2, 1, 2, 0, 4],
    },
    'potencia / espesor': {
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
    'distribución_leyes': {
        'Uniforme': [3, 4, 3, 4, 4, 3, 3, 3, 4, 3],
        'Gradual': [3, 2, 3, 2, 2, 3, 2, 3, 2, 3],
        'Errática': [3, 0, 1, 0, 0, 3, 1, 3, 0, 3],
    },
    'competencia_macizo': {
        'Baja (<2)': [3, 4, -49, 0, 4, 0, 1, 3, 2, 4],
        'Media (2-4)': [4, 1, 3, 3, 1, 3, 3, 2, 3, 1],
        'Alta (>4)': [4, 1, 4, 3, 0, 4, 4, 2, 3, 1],
    },
    'espaciamiento_estructuras': {
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


def bloque_radiobuttons(frame_padre, categoria, opciones, callback, selected_option_dict):
    """
    Crea un bloque de botones de radio para una categoría y lo agrega al frame padre.

    Parámetros:
    - frame_padre: Frame donde se insertarán los widgets.
    - categoria: Nombre de la categoría (clave del diccionario).
    - opciones: Diccionario con las opciones (clave) y listas de puntajes (valor).
    - callback: Función a llamar cuando se selecciona una opción.
    - selected_option_dict: Diccionario donde se almacenan las variables seleccionadas.
    """

    # Etiqueta de la categoría
    tk.Label(
        frame_padre,
        text=categoria.replace('_', ' ').title(),
        bg='gray',
        fg='white',
        font=('Arial', 11, 'bold'),
        pady=4
    ).pack(fill='x', expand=True, pady=(15, 5))

    # Variable asociada a la selección
    selected_option = tk.StringVar(value="")

    # Frame contenedor con borde para el grupo de opciones
    contenedor_opciones = tk.Frame(
        frame_padre, bg='lightgray', bd=1, relief='solid')
    contenedor_opciones.pack(fill='x', padx=10, pady=(0, 10))
    for opcion in opciones:
        tk.Radiobutton(
            frame_padre,
            text=opcion,
            variable=selected_option,
            bg='light gray',
            value=opcion,
            font=('Courier New', 10),  # Fuente monoespaciada
            justify='left',            # Alinea el texto dentro del botón
            anchor='w',                # Asegura que el texto empiece a la izquierda
            width=25,                  # Fuerza mismo ancho para todos
            command=lambda c=categoria, v=selected_option: callback(c, v)
        ).pack(anchor='center', pady=2)

    # Guardar variable para acceso futuro
    selected_option_dict[categoria] = selected_option
