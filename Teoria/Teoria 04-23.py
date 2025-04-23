
import pandas as pd
import plotly.express as px

df = pd.read_csv('data (1).txt', sep='\t')
print(df)

#Crear el histograma de la columna 'ley'
fig = px.histogram(df, x='ley', nbins=30, title='Distribucion de ley') #en este caso el nombre del grafico es fig

#Mostrar el grafico
# fig.show()

# fig2 = px.histogram(
#     df, #desde donde se extraen los datos
#     x = 'ley', #la variable que se quiere graficar
#     y = None, #Opcion para contar algo diferente ala frecuencia
#     color = 'ley', #'ley', #columna para colorear por categoria
#     nbins = 20, #numero de barras
#     barmode = 'relative', #como se apilan las barras: stack, overlay, relative
#     histnorm = 'percent', #Normalizacion: percentm probability
#     marginal = 'box', #grafico adicional: rug, box, violin
#     title = 'Histograma de ley'
# )

# fig4 = px.histogram(
#     df, #desde donde se extraen los datos
#     x = None, #eje X usado cuando quieres agrupar por categorias
#     y = 'ley', #eje Y (variable numerica)
#     color = None, #Agrupacion por color
# points = False, # Còmo mostrar los puntos individuales:outliers. all, suspectedoutliers, False 
# notched = False, #Mostrar como notch la mediana
#     ...
# )

# fig4.show()


# import plotly.graph_objects as go

# df = df[df['z'] >= 2900] #Tambien se puede sumar el minimo con el maximo y dividir por 2
# df = df[(df['x'] >= 25250]
# df = df[df['y'] <= 25175 + 200]
# df = df[df['y'] >= 25175 - 200]
# df = df[df['z'] <= 3500]

#con eso puedo ver el modelo de bloques pero no me sirve para ver la envolvente, necesito solo ver los que sean mayor a 1
#para eso aplicamos un filtro


#EN COSTO VENTA Y REFINAMIENTO = 1
#PONER UNA O 2 COLUMNAS QUE SE LLAMEN STATUS.