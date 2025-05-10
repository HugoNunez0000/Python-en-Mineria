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
