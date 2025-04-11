###CLASE DEL 04-11 PRACTICA###

import pandas as pd #es para no estar escribiendo pandas todo el rato

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sofia'],
    'Edad': [7, 50, 14, 22],
    'Pais': ['Venezuela', 'Venezuela', 'Chile', 'Peru']
}
###TEMAS PARA PROYECTO###
#nicholas
#calculadora de tronadura que te diga el area de infleuncia

#creamos primero nuestra variable que siempre se le pone df
df = pd.DataFrame(data)
print(df)

#para crear una nueva columna primero creamos nuestra columna
df['Meses'] = df['Edad']*12

print(df)

df['Adulto'] = 0
df['Adulto'][df['Edad'] >= 18] = 1
print(df)

#Operacion vectorizadas es una operacion que se hace muy rapido sirve para trabajar con bases de datos muy grandes
#Una operacion No vectorizada es una que se tiene que hacer con python y sera muy lenta

#Usar funcion iterrows 
#similar a enumarate

for index, row in df.iterrows():
    print(index)
    print(row)
    
a = 4 + 15
print(a)

for index, row in df.iterrows():
    print(f'Persona {index + 1}') #f es para agregar vairables dentro de un print
    print(f'Soy {row['Nombre']}, tengo {row['Edad']} años y soy de {row['Pais']}')
    print(' ')

#https://github.com/21croz/Clase-4


df_bloques = pd.read_table('Practica/modelo2.txt', sep = '\t', header = 0)  #le estamos diciendoa pandas como esta separado nuestro modelo de bloques
print(df_bloques)

volumen_bloque = 10*10*10 #m°3
df_bloques['TON'] = volumen_bloque*df_bloques['DENSITY']

df_bloques['Cu_Q'] = (df_bloques['CUT']/100)*df_bloques['TON']
col_CUT = df_bloques['CUT'].tolist()

print(col_CUT)
print(max(col_CUT))
