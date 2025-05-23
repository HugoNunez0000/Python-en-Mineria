### TAREA 1 PYTHON EN MINERÍA - HUGO NÚÑEZ PECHUANTE ###


# 1 #

# Importamos Pandas, Numpy, Plotly y les asignamos sus respectivas abreviaturas
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go


# 2 #

# Leemos la base de datos (Modelo de Bloques) y le decimos como se encuentra separado
df = pd.read_csv('data.txt', sep='\t')
df.head()

print("\n")
print("La estadística descriptiva del modelo de bloques es:\n")
print(df.describe())  # Mostramos la estadística descriptiva del modelo de bloques
print("\n")

# Podemos ver que el promedio (mean) es 0.414 y la desviación estandar (std) es 0.195
# Esto lo usaremos para crear la columna 'ley2'


# 3 #

# Ahora Graficamos el histograma y el boxplot de la variable 'ley'

HistoBox = px.histogram(
    df,  # Desde donde se extraen los datos
    x='ley',  # la variable que se quiere graficar
    y=None,  # Opcion para contar algo diferente a la frecuencia
    color=None,  # 'ley', #Columna para colorear por categoría
    nbins=50,  # Numero de barras
    barmode='stack',  # Como se apilan las barras: stack, overlay, relative
    histnorm='percent',  # Normalizacion: percent, probability
    marginal='box',  # Grafico adicional: rug, box, violin
    title='Histrograma de la variable ley'
)
HistoBox.show()


# 4 #

# Creamos la columna ‘ley2’ con valores aleatorios y estadística igual a la variable ‘ley’.
# Para crear una nueva columna primero creamos nuestra columna

mu = 0.414
sigma = 0.195

# Ese numero es el numero de variables aleatorias que dabamos
# Creamos números aleatorios con una distribución normal, que tienen un promedio y una desviación estandar igual al de la columna 'ley'
# Ese nunero es la cantidad de datos que tiene la columna 'ley', el de 'ley2' debe ser igual.

samples = np.random.normal(mu, sigma, 1048575)

df['ley2'] = samples  # Luego la columna 'ley2' será igual a samples

# A continuacion restringimos la función y evitamos que en samples (al ser random) de un valor negativo.
df.loc[df['ley2'] < 0, 'ley2'] = 0

# Mostramos la estadistica descriptiva de df con esta nueva columna incorporada.
print("La estadistica descriptiva del modelo de bloques con la columna 'ley2' incorporada es:\n")
print(df.describe())
print("\n")

# 5 #

# Creamos una columna para cada variable de ley que valorice cada uno de los bloques de acuerdo a la ecuación:
# V_b = Ton_block * [(P_Cu - C_VyR) * [Ley_Cu * R * 2204.62 - (C_p + C_m )]

# 5.1 #
# Para eso primero definimos los valores de la formula

# V_b: Valor del bloque [USD].      ----> Es lo que queremos calcular
# Ley_Cu: Ley del bloque [%].       ----> Lo tenemos
# Ton_block: Tonelaje del bloque [ton]. ----> Esto lo calcularemos a continuacion en # 5.2 #

P_Cu = 4.30  # Precio cobre [USD/lb].
C_VyR = 0.95  # Costo venta y refinamiento [USD/lb].
R = 0.85  # Recuperación [%].
C_p = 10  # Costo planta [USD/ton].
C_m = 11.5  # Costo mina [USD/ton].

# 5.2 #
# Para calcular el tonelaje del bloque tenemos que multiplicar el volumen del bloque por la densidad
# Asumimos una densidad de 2.6 kg/m3

df['Density'] = 2.6
# El volumen del bloque es 10 * 10 * 10 debido a que al ver los datos en x, y , z vemos que van saltando de 10 en 10
df['Volume'] = 10 * 10 * 10

# Luego el tonelaje del bloque será
df['Ton_block'] = df['Density'] * df['Volume']

# 5.3 #

# Fórmula aplicada a la columna 'ley'
df['Valueblock_ley'] = df['Ton_block'] * \
    (((P_Cu - C_VyR) * (df['ley'] / 100) * R * 2204.62) - (C_p + C_m))

# Fórmula aplicada a la columna 'ley2'
df['Valueblock_ley2'] = df['Ton_block'] * \
    (((P_Cu - C_VyR) * (df['ley2'] / 100) * R * 2204.62) - (C_p + C_m))


# 6 #

# Creamos la columna ‘status’ para cada columna de valor de bloques donde: bloques positivos ==1 y bloques negativos o cero == 0.
# Como tenemos 2 condiciones (1 o 0) utilizaresmos la función where de numpy

# Así para la columna 'Valueblock_ley'
df['status_ley'] = np.where(df['Valueblock_ley'] > 0, 1, 0)

# Y para la columna 'Valueblock_ley2'
df['status_ley2'] = np.where(df['Valueblock_ley2'] > 0, 1, 0)

print("La tabla con los valores de bloques según la ley y con su respectivo status se muestra a continuación:\n")
print(df)


# 7 #

# Graficamos en 3D las dos envolventes de ley de acuerdo a su columna status

# Dejamos solo los bloques con status_ley == 1
# De esta forma solo estaremos trabajando con los bloques que son rentables de extraer.

bloques_envolvente_ley1 = df[df['status_ley'] == 1]


# Creamos el gráfico 3D
graf1 = go.Figure()

graf1.add_trace(go.Scatter3d(
    x=bloques_envolvente_ley1['x'],
    y=bloques_envolvente_ley1['y'],
    z=bloques_envolvente_ley1['z'],
    mode='markers',
    marker=dict(
        size=5,
        # Se graficará según el valor del bloque
        color=bloques_envolvente_ley1['Valueblock_ley'],
        colorscale='Inferno',
        colorbar=dict(title='Valor del Bloque en USD'),
        opacity=0.5
    )
))

graf1.update_layout(
    title='Grafico 3D de envolvente de ley de acuerdo a status_ley ',
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z',
        bgcolor='white'
    )
)

graf1.show()


# Ahora lo mimso para ley2

# Dejamos solo los bloques con status_ley2 == 1
bloques_envolvente_ley2 = df[df['status_ley2'] == 1]

# Creamos el grafico 3D
graf2 = go.Figure()

graf2.add_trace(go.Scatter3d(
    x=bloques_envolvente_ley2['x'],
    y=bloques_envolvente_ley2['y'],
    z=bloques_envolvente_ley2['z'],
    mode='markers',
    marker=dict(
        size=5,
        color=bloques_envolvente_ley2['Valueblock_ley2'],
        colorscale='Magma',
        colorbar=dict(title='Valor del Bloque en USD'),
        opacity=0.5
    )
))

graf2.update_layout(
    title='Grafico 3D de envolvente de ley2 de acuerdo a status_ley2 ',
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z',
        bgcolor='white'
    )
)

graf2.show()
