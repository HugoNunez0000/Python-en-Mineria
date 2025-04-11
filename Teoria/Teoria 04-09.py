# #Instalar libreria
# #pip install pandas

# #importar libreria
# sirve para hacer data frames, puede leer 
# es super rapido pandas pq su base es r
import pandas as pd
# import numpy as np #numpy es para colocar numeros y crear juegos matematicos

# #primero crearemos un diccionario
# #crear un dataframe desde un diccionario

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sofia'],
    'Edad': [23, 25, 30, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Madrid']
}

df = pd.DataFrame(data)  # con esto lo mostrara como tabla de excel
print(df)

# ###Acceder a los datos (esto es por si no quiero que se muestren todos los datos ya que en un modelo de bloques son muchos)

# df.head(2)  # primeras filas
# df.tail(2)  # ultimas 2 filas
# df['Nombre'] #si querermos acceder o extraer una columna
print(df.iloc[1])  # Fila por indice

# ###Descripcion basica estadistica(cuantitativa)

# df.describe()
# df.info()
# #Nan, nan, no null son las celdas en excel que no tienen ningun valor, ni si quiera hay un 0
# df['Edad'].mean()
# df['Edad'].max()

# ###Filtrado de datos

# df2 = df.copy()
# df2 = df2[df2['Ciudad'] == 'Madrid']  #Va a imprimir las solo las personas que su ciudad sea Madrid
# df2 = df2[df2['Edad'] > 24]
# #df2 = df2[df2['Edad'] > 24 & df['Ciudad'] == 'Sevila'] #aqui con 2 condiciones
# print(df2)

# ###Limpiar datos
# df.dropna(inplace=True)     #Eliminar nulos, #si queremos que la funcion realice un trabajo usamos inplace=True
# df.fillna(0, inplace=True)  #Reemplazar nulos
# df.rename(columns={'Nombre' : 'Nombre_completo'}, inplace=True)

# ###Cargar y guardar CSV
# #df.to_csv('datos.csv', index=False)  #Guardar  #index=False es para que no me cargue una columna con todos los indices
# #df = pd.read_csv('data.txt', sep='/t')  #Cargar

# ###Agrupar y ordenar
# # df.groupby('Ciudad')
# # df.sort_values(by='Edad', ascending=False)
# # print(df.sort_values(by='Edad', ascending=False))

# ###https://github.com/oyarzo-diego/python2


#################################################
######## TRABAJO CON MD MODELO DE BLOQUES#########
#################################################

# import pandas as pd

# df = pd.read_csv('data.txt', sep='\t')
# df.head()
# print(df.describe())

# # ahora queremos filtrar los x
# df = df[df['x'] <= 24325 + 100]
# df = df[df['x'] >= 24325 - 100]
# df = df[df['y'] <= 25175 + 100]
# df = df[df['y'] >= 25175 - 100]

# precio_cu = 4.5
# costo_ryv = 1  # costo de refinamiento y venta
# densidad = 2, 7
# ton = 1000*densidad  # volumen por densidad
# costo_mina = 18
# costo_planta = 19
# recuperacion = 0.85
# constante = 2204.62

# df['Valor_de_Bloque'] = ton*(precio_cu - costo_ryv) * (df['ley'] / 100) * \
#     recuperacion * constante - ton*(costo_mina+costo_planta)
# # print(df.head(10))
# print(df.describe())

# # for row in df.iterrows():
# #     if row['Valor_de_Bloque'] >=0:
# #         row['state'] = 1              #ESTO NO VA


# # print(df.describe())

# # #Lo que queremos hacer es cambiar el state cuando este sea menor a 0
# # df['state'] = 0

# # for i in range(len(df)):
# #     row = df.iloc[i]
# #     if row['Valor_de_Bloque'] >= 0:
# #         row['state'] = 1

# # print(df.describe())


# for i in range(len(df)):
#     if df.iloc[i][4] >= 0:  # aqui el iloc revisa la fila i y la columna 4
#         df.iat[i, 5] = 1
