# componentes.py

import tkinter as tk


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
    tk.Label(frame_padre, text=categoria.upper(), bg='gray', fg='white',
             font=('Arial', 10, 'bold')).pack(pady=5, fill='x')

    # Variable asociada a la selección
    selected_option = tk.StringVar(value="")

    for opcion in opciones:
        tk.Radiobutton(
            frame_padre,
            text=opcion,
            variable=selected_option,
            bg='light gray',
            value=opcion,
            command=lambda c=categoria, v=selected_option: callback(c, v)
        ).pack(anchor='w')

    # Guardar variable para acceso futuro
    selected_option_dict[categoria] = selected_option
