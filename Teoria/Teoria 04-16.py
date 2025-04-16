
#NUMPY
#Es una estrunctura de datos que permite almacenar una coleccionde elementos
#del mismo tipo
#Se usan cuando se necesita eficiencia en el manejo de datos numericos

import numpy as np

a = np.array([1, 2, 3]) #Array 1D
b = np.array([[1, 2, 3],[3, 4, 5], [5, 6, 7]]) #Array 3D (Matriz de 3 x 3)
c = np.zeros((2, 3)) #Matriz 2x3 llena de ceros
d = np.ones((3, 3)) #Matriz de 3x3 llena de unos
e = np.eye(3) #Matriz identidad 3x3
f = np.arange(0, 10, 2) #[0 2 4 6 8]
g = np.linspace(0, 1, 5)  #5 valores entre 0 y 1

print(g)

# #PROPIEDADES DE LOS ARRAYS
# a.shape #Tamaño
# a.dtype #Tipo de dato
# a.ndim #Dimension (1D, 2D, etc)
# a.size #Numero total de elementoss

#print(f.size)

#OPERACIONES
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])

# x + y #[5 7 9]
# x * y #[4 10 18]
# x.mean() #Media
# x.std() #Desviacion estandar
# x.sum() #Suman total
# print(x*y)

#INDEXACION (es para capturar algun valor de un array, los indices parten siempre de 0)
# a = np.array([[1, 2, 3], [4, 5, 6]])
# a[0, 1]  #2
# a[:, 1]  #el : significa todos los valores, en este caso TODAS las filas pero la segunda columna, pq indicamos el 1
# a[1, :]  #Segunda fila
# print(a[1,:])  #aqui tomamos la segunda fila pq indicamos el 1

# #EJEMPLO
# #Simulacion de 1000 valores de una distribcion normal

# # mu, sigma = 0, 0.1
# # samples = np.random.normal(mu, sigma, 1000)
# # print(samples)
# #import matplotlib.pyplot as plt (con esto se puede ver el grafico y la distribucion de los datos)
# #count, bins

# #PANDAS
import pandas as pd
data = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(data, columns=['A', 'B'])
print(df)
#Aqui otro ejemplo donde usamos distribucion normal
# df = pd.DataFrame({
#     'Altura (cm)': np.random.normal(170, 10, 100),
#     'Peso (kg)': np.random.normal(65, 15, 100)
# })

# media_altura = df['Altura (cm)'].mean()
# matriz_covarianza = df.cov().to_numpy()

# # datos = np.random

# #Ejemplo practico con Modleo de bloques

# import pandas as pd

# df = pd.read_csv('data (1).txt', sep='\t')
# df.head()
# #print(df.describe())

# # # ahora queremos filtrar los x y los y
# #filtro = (df['x'] <= 24325 + 200) & ......
# df = df[df['x'] <= 24325 + 200] #Tambien se puede sumar el minimo con el maximo y dividir por 2
# df = df[df['x'] >= 24325 - 200]
# df = df[df['y'] <= 25175 + 200]
# df = df[df['y'] >= 25175 - 200]
# df = df[df['z'] <= 3500]

# print(df.describe())
# mu = 0.572
# sigma = 0.103
# samples = np.random.normal(mu, sigma, 126075)  #ese numero es el numero de variables aleatorias que dabamos

# df['ley2'] = samples
# print(df.head())
# print(df.describe())

# #Primera iteracion de envolvente economica:n cuales bloques son factibles economicamente y estos son los que estan por sobre la ley de corte