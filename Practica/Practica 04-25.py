import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table('database.txt', sep = ' ')
# print(df)

# #DEFINIR LOS EJES DEL GRAFICO
# ejex = df['X']
# ejey = df['Y']
# etiquetas = ['Linea']

# #CREAR EL GRAFICO
# plt.plot(ejex, ejey, label = etiquetas)
# plt.xlabel('Eje x')
# plt.ylabel('Eje y')
# plt.title('Mi primer Grafico en Matplotlib')
# plt.legend() #con eso mostramos la leyenda

# #MOSTRAR EL GRAFICO
# plt.show()

#AHORA TRABAJAMOS CON OTRA BASE DE DATOS
# df2 = pd.read_table('modelo2.txt', sep = '\t')
# print(df2)

# datos = df2['CUT']

# plt.hist(datos, bins = 8, color = 'pink',edgecolor = 'black')

# plt.xlabel('Ley de cobre [%]')
# plt.ylabel('Frecuencia')
# plt.title('Histograma de dispersion de ley de cobre')

# plt.show()


# 1 FILA Y 2 COLUMNAS
fig, ax = plt.subplots(1, 2) #fig representa todo el lienzo en que yo voy a hacer los graficos, ax representa cada uno de los graficos que yo voy a hacer

ax[0].plot([8, 15, 12, 21], [3, 4, 7, 1])
ax[0].set_title('Grafico 1')

ax[1].bar([10, 14, 4, 9, 2], [22, 13, 6, 0, 5])
ax[1].set_title('Grafico 2')

plt.tight_layout()
plt.show()
