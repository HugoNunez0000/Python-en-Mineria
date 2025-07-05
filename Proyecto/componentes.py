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
