### TAREA 1 PYTHON EN MINERÍA - HUGO NÚÑEZ PECHUANTE ###


# 1 #

# Importamos Pandas, Numpy, Plotly y les asignamos sus respectivas abreviaturas
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 2 #

# Leemos la base de datos (Modelo de Bloques) y le decimos como se encuentra separado
df = pd.read_csv('data (1).txt', sep='\t')
df.head()

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

mu = 0.414
sigma = 0.195

# Ese numero es el numero de variables aleatorias que dabamos
# Creamos números aleatorios con una distribución normal, que tienen un promedio y una desviación estandar igual al de la columna 'ley'
samples = np.random.normal(mu, sigma, 1048575)

df['ley2'] = samples  # Luego la columna 'ley2' será igual a samples

# A continuacion restringimos la función y evitamos que en samples de un valor negativo
df.loc[df['ley2'] < 0, 'ley2'] = 0

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

# Crear gráfico 3D
print(df['status_ley'].value_counts())
print(df['status_ley2'].value_counts())


# Primero seleccionamos solo los bloques rentables, para esto filtramos bloques rentables para 'status_ley'
bloques_rentables_ley = df[df['status_ley'] == 1]
print(bloques_rentables_ley.describe())

# Filtramos bloques rentables para 'status_ley2'
# bloques_rentables_ley2 = df[df['status_ley2'] == 1]
# print(bloques_rentables_ley2)


# Cargar archivo CSV de la envolvent

# Filtrar bloques con antes_max == 1

# Configurar coordenadas y valor
x = bloques_rentables_ley['x']
y = bloques_rentables_ley['y']
z = bloques_rentables_ley['z']
valor = bloques_rentables_ley['Valueblock_ley']

# Verificamos que hay datos dentro de bloques_rentables_ley
print(bloques_rentables_ley.shape)
print(bloques_rentables_ley[['x', 'y', 'z', 'Valueblock_ley']].describe())


# Coordenadas y valor de los bloques
x = bloques_rentables_ley['x']
y = bloques_rentables_ley['y']
z = bloques_rentables_ley['z']
valor = bloques_rentables_ley['Valueblock_ley']

# Gráfica
fig2 = go.Figure()

fig2.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=10,
        color=valor,
        colorscale='Magma',
        colorbar=dict(title="Valor de los bloques.")
    )
))

# Estilo
fig2.update_layout(
    scene=dict(
        xaxis=dict(showgrid=True, gridcolor='black', title='X', color='black'),
        yaxis=dict(showgrid=True, gridcolor='black', title='Y', color='black'),
        zaxis=dict(showgrid=True, gridcolor='black', title='Z', color='black'),
        bgcolor="white"
    ),
    title="Grafico 3D Eenvolventes de ley, status == 1.",

)

fig2.show()
