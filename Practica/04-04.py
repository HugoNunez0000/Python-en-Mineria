###EJERCICIO 1 PLANAR UNA LISTA###

lst = [[1, 2], [3, 4], [5,6], [7,8]]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]

for elem in lst:
    print(elem)

lst_resultado = []
for elem in lst:
    for num in elem:
        lst_resultado.append(num) #agrega elementos app es agregar end es al final, insert ?? 

print(lst_resultado)


###EJERCIO 2 ENCONTRAR EL NUMERO MAYOR Y EL NUMERO MENOR

lst = [3, 5, 20, 9, 1, 50, 10, 100]
res = [1, 100]

#for i in lst:
 #   numer = lst[i]
  #  if numer < 

nmenor, nmayor = lst[0], lst[0]  #almaceno nmenor y nmayor en el primer elemento de la lst

for num in lst:
    if num > nmayor:
        nmayor = num

    if num < nmenor:
        nmenor = num

print(nmenor, nmayor)

###FUNCIONES
#  con def se crea una funcion

#def suma(a, b):
  #  resultado = a + b
  #  return resultado

### CREAR UNA FUNCION QUE, AL INGRESAR UNA LISTA CON n RADIOS DE CIRCULO, DEVUELVA LAS n AREAS

### ENTRADA: [1, 2, 3, 4]
#SALIDA: [1]

from math import pi #desde la libreria math importo solo la variable pi

def calc_areas(lst): #lst en este caso simboliza una variable de tipo lista porque eso piden
    lst_areas = []
    for elem in lst:
        area = elem**2*pi
        lst_areas.append(area)
    return lst_areas    ###SI A UNA FUNCION NO LE DIGO QUE RETORNE ALGO NO ENTREGARA NADA

print(calc_areas([1, 2, 3, 4, 5]))


###CREAR UNA FUNCION QUE, DADA UNA STRING, DEVUELVA LA CANTIDD DE VOCALES QUE HAYA EN ELLA

## ENTRADA: 'KAMATACHUKY'
## SALIDA: 4

#def vocales(a):
    #for elem in a:  ## se puede usar pa lista y para string
        #for i in range len(a)

def count_vocals(palabra):
    vocal = 'aeiouAEIOU'
    contador = 0
    for letra in palabra:
        if letra in vocal:
            contador += 1 #es igual a contador =  contador + 1

    return contador

print(count_vocals('NKZ'))

### CREAR UNA FUNCION QUE DADO UN NUMERO RETORNE TRUE SI ES PRIMO Y FALSE SI NO ES PRIMO

#def num_primo(numero):
   # for i in range(2, numero):
       # if numero/i != 0:
        #    print("No es primo")


def es_primo(num):
    for i in range(2,num):
        if num%i == 0:  #EL % ES EL RESIDUO POR EJEMPLO AQUI ENTREGA SI EL NUMERO PARTIDO POR i ENTREGA RESIDUP O NO
         return False
    return True                                     #EL == ES PARA COMPARAR
#print(es_primo(20))    º


# def es_primo_con_lista(num):
#     bool = []
#     for elem in num:
#         for i in range(2,elem):
#             if elem%i == 0:  #EL % ES EL RESIDUO POR EJEMPLO AQUI ENTREGA SI EL NUMERO PARTIDO POR i ENTREGA RESIDUP O NO
#                 bool.append(False)
#                 return
#             else:
#                 bool.append(True)
#                 return
#                          #EL == ES PARA COMPARAR
#     return bool


# print(es_primo_con_lista([2, 6, 7]))

# def primos(lista_numeros):

### BREAK
contador = 0
while True:
    contador += 1
    print(contador)

    if contador == 17:
        break