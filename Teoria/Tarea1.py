### TAREA 1 PYTHON EN MINERÍA - HUGO NÚÑEZ PECHUANTE ###


# 1 #

# Importamos Pandas, Numpy y Plotly y les asignamos sus respectivas abreviaturas
import plotly.express as px
import pandas as pd
import numpy as np


# 2 #

# Leemos la base de datos (Modelo de Bloques) y le decimos como se encuentra separado
df = pd.read_csv('data (1).txt', sep='\t')
df.head()

# Filtrar los datos
# Restamos el valor máximo con el mínimo y dividimos por 2 para filtrar (nos da 220)
df = df[df['x'] <= 24325 + 220]
df = df[df['x'] >= 24325 - 220]
df = df[df['y'] <= 25175 + 220]
df = df[df['y'] >= 25175 - 220]
df = df[df['z'] <= 3250]

print(df.describe())  # Mostramos la estadística descriptiva del modelo de bloques


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
    title='Histrograma de ley'
)
HistoBox.show()


# 4 #

# Creamos la columna ‘ley2’ con valores aleatorios y estadística igual a la variable ‘ley’.
# Para crear una nueva columna primero creamos nuestra columna

mu = 0.565
sigma = 0.083

# Ese numero es el numero de variables aleatorias que dabamos
# Creamos números aleatorios con una distribución normal, que tienen un promedio y una desviación estandar igual al de la columna 'ley'
samples = np.random.normal(mu, sigma, 101250)

df['ley2'] = samples  # Luego la columna 'ley2' será igual a samples

# Mostramos la estadistica descriptiva de df con esta nueva columna incorporada
print(df.describe())


# 5 #

# Creamos una columna para cada variable de ley que valorice cada uno de los bloques de acuerdo a la ecuación:
# V_b = Ton_block * [(P_Cu - C_VyR) * [Ley_Cu * R * 2204.62 - (C_p + C_m )]

# 5.1 #
# Para eso primero definimos los valores de la formula

# V_b: Valor del bloque [USD].      ----> Es lo que queremos calcular
# Ley_Cu: Ley del bloque [%].       ----> Lo tenemos
# Ton_block: Tonelaje del bloque [ton]. ----> Esto lo calcularemos a continuacion en # 5.2 #

P_Cu = 4.30  # Precio cobre [USD/lb].
C_VyR = 0.26  # Costo venta y refinamiento [USD/lb].
R = 0.85  # Recuperación [%].
C_p = 8.5  # Costo planta [USD/ton].
C_m = 10  # Costo mina [USD/ton].

# 5.2 #
# Para calcular el tonelaje del bloque tenemos que multiplicar el volumen del bloque por la densidad
# Asumimos una densidad de 2.6 kg/m3

df['Density'] = 2.6
df['Volume'] = df['x'] * df['y'] * df['z']

# Luego el tonelaje del bloque será
df['Ton_block'] = df['Density'] * df['Volume']

# 5.3 #

# Fórmula aplicada a la columna 'ley'
df['Valueblock_ley'] = df['Ton_block'] * \
    (((P_Cu - C_VyR) * df['ley'] * R * 2204.62) - (C_p + C_m))

# Fórmula aplicada a la columna 'ley2'
df['Valueblock_ley2'] = df['Ton_block'] * \
    (((P_Cu - C_VyR) * df['ley2'] * R * 2204.62) - (C_p + C_m))

print(df)


# 6 #

# Creamos la columna ‘status’ para cada columna de valor de bloques donde: bloques positivos ==1 y bloques negativos o cero == 0.
# Como tenemos 2 condiciones (1 o 0) utilizaresmos la función where de numpy

# Así para la columna 'Valueblock_ley'
df['status_ley'] = np.where(df['Valueblock_ley'] > 0, 1, 0)

# Y para la columna 'Valueblock_ley2'
df['status_ley2'] = np.where(df['Valueblock_ley2'] > 0, 1, 0)

print(df)


# 7 #

# Graficamos en 3D las dos envolventes de ley de acuerdo a su columna status == 1.

fig = px.scatter_3d(
    df,
    x='x',
    y='y',
    z='z',
    color='Valueblock_ley',  #
    title='Envolvente de ley respecto a status',
    color_continuous_scale='Inferno',
    opacity=0.4
)
fig.show()

fig = px.scatter_3d(
    df,
    x='x',
    y='y',
    z='z',
    color='Valueblock_ley2',
    title='Envolvente de ley2 respecto a status',
    color_continuous_scale='Cividis',
    opacity=0.7
)
fig.show()
