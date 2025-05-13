# print("Hola Mundo")
# print("chao Mundo")

# #Tipos de variable

# num = 30
# nombre ="Puro Kes"
# num1,num2 = 10, 20
# grav = 9.8

# my_lista = [1, 2, 9.8, "hola", 1000, [1, 2]] #Caja con mas cajas dentro
# my_tupla = (1, "chao", 20,4) #Similar a tupla la dif es que las listas se pueden cambiar
#            #|-----> ese elemento es el 0
# #las listas se pueden modificar mediente codigos y las tuplas nunca cambian, las tuplas son mas rapidas de ocupar ya que no cambian su contenido (el pc se demora menos)

# #diccionario dicc = {}

# numero = 20
# if numero == 20:
#     print("El numero es igual a 20")
# else:
#     print("El numero no es 20")

# for i in range(10):
#     print(i)

# var1 = 1
# while var1 < 100:
#     print("Puro Kes")
#     var1 = var1 + 1

#     a = 400

# print(a)

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import math as mt
# Parte 2
df = pd.read_csv('data (1).txt', sep='\t')
print(df.head())
print(df.describe())


# parte 3
Fig_histobox = px.histogram(
    df,  # Desde donde se extraen los datos
    x='ley',  # la variable que se quiere graficar
    y=None,  # Opcion para contar algo diferente a la frecuencia
    color=None,  # 'ley', #Columna para colorear por categoría
    nbins=50,  # Numero de barras
    barmode='stack',  # Como se apilan las barras: stack, overlay, relative
    histnorm='percent',  # Normalizacion: percent, probability
    marginal='box',  # Grafico adicional: rug, box, violin
    title='Histrograma y boxplot de ley'
)
Fig_histobox.show()

# Parte 4
# Calculo de  la media y desviación estándar de la columna 'ley'
# mostramos valores unicos de x, unique es para que no se repitan valores
coordx = df['x'].unique()
coordxord = np.sort(coordx)  # X de menor a mayor
# podemos cambiar el median a max dejandolo como filtro opcional
Xfiltrado = df[df['x'] <= np.max(coordxord)]
mu = Xfiltrado['ley'].mean()  # Media de la columna 'ley'
sigma = Xfiltrado['ley'].std()  # Desviación estándar de la columna 'ley'
print(
    f'se muestra la ley media en la coord x< {np.median(coordxord)}, el cual es {mu}%')
print(sigma)
print('---'*50)
#  muestras de una distribución normal con la media y desviación estándar calculadas
# Generar muestras con la media y desviación estándar
samples = np.random.normal(mu, sigma, len(df))

#  muestras generadas a la nueva columna 'ley2'
df['ley2'] = samples

# Reemplazar cualquier valor negativo de 'ley2' por 0
# Limpiamos datos reemplazando los menores a 0 de 'ley2' x 0
df.loc[df['ley2'] < 0, 'ley2'] = 0

# Verificación de los resultados
# Ver las primeras filas para asegurarte de que 'ley2' se haya agregado correctamente
print(df.head())
print(df.describe())  # Ver la descripción estadística con la nueva columna 'ley2'

# parte 5
Fig_histobox_ley2 = px.histogram(
    df,  # Desde donde se extraen los datos
    x='ley2',  # la variable que se quiere graficar
    y=None,  # Opcion para contar algo diferente a la frecuencia
    color=None,  # Columna para colorear por categoría
    nbins=50,  # Numero de barras
    barmode='stack',  # Como se apilan las barras: stack, overlay, relative
    histnorm='percent',  # Normalización: percent, probability
    marginal='box',  # Gráfico adicional: rug, box, violin
    title='Histograma y boxplot de ley2'
)
Fig_histobox_ley2.show()

# Superponer histogramas de ley y ley2
fig_compare = go.Figure()
fig_compare.add_trace(go.Histogram(x=df['ley'], name='ley', opacity=0.6))
fig_compare.add_trace(go.Histogram(x=df['ley2'], name='ley2', opacity=0.6))

fig_compare.update_layout(
    barmode='overlay',
    title='Comparación de histogramas: ley vs ley2',
    xaxis_title='Valor',
    yaxis_title='Frecuencia'
)

fig_compare.show()

# Parte 6: Definir constantes
densidad = 2.7  # g/cm³ o ton/m³
precio_cu = 4.5  # USD/lb
costo_ryv = 1  # USD/lb
costo_mina = 18  # USD/ton
costo_planta = 19  # USD/ton
recuperacion = 0.85  # %
constante = 2204.62  # lb/ton

# Parte 7: Calcular tonelaje (usando dimensiones del bloque)
# Asumimos que cada bloque tiene el mismo tamaño en x, y, z
# volumen = 10m x 10m x 10m = 1000 m³; tonelaje = volumen * densidad
volumen = 1000  # m³
ton = volumen * densidad  # Toneladas por bloque

# Parte 8: Calcular Valor de Bloque para 'ley' y 'ley2'
df['Vb_ley'] = ton * ((precio_cu - costo_ryv) * (df['ley'] / 100)
                      * recuperacion * constante - (costo_mina + costo_planta))
df['Vb_ley2'] = ton * ((precio_cu - costo_ryv) * (df['ley2'] / 100)
                       * recuperacion * constante - (costo_mina + costo_planta))

# Parte 9: Crear columnas 'status' para identificar bloques con valor positivo
df['status_ley'] = np.where(df['Vb_ley'] > 0, 1, 0)
df['status_ley2'] = np.where(df['Vb_ley2'] > 0, 1, 0)

# Parte 10: Ver cantidad de bloques positivos y negativos
print(df['status_ley'].value_counts())
print(df['status_ley2'].value_counts())


# Filtrar los bloques con status_ley == 1
bloques_validos = df[df['status_ley'] == 1]
print(bloques_validos)
# Crear gráfico 3D
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=bloques_validos['x'],
    y=bloques_validos['y'],
    z=bloques_validos['z'],
    mode='markers',
    marker=dict(
        size=5,
        color=bloques_validos['ley'],
        colorscale='Viridis',
        colorbar=dict(title='Ley [%]'),
        opacity=0.8
    )
))

fig.update_layout(
    title='Envolvente 3D – Ley original (status_ley == 1)',
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z',
        bgcolor='white'
    )
)

fig.show()
