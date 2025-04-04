#Clase 2 la del 28-03

for i in range(5): # 0 1 2 3 4
    print(i)

my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)): # 0 1 2 3 4
    elem = my_list[i]
    print(elem)

my_list[2] = "hola"

print(my_list)

my_tuple = (1, 2, 3, 4, 5, 'Hola', 'Chao')
print(my_tuple)

my_list = [10, 5, 4, 15, 2, 9, 20, 100]

#for i in range(len(my_list)):
   # if my_list[i] >= 10:
    #my_list[i] = 'chanchito'
    
#print(my_list)

for i in range(len(my_list)):
    elem = my_list[i]
    if elem >= 10:
        my_list[i] = 'chuquicamata'

print(my_list)        


#Diccionarios

#keys, values, items
dicc = {
    'nombre' : 'felipe',
    'edad' : 23,
    'universidad' : 'Udec'
}

print(dicc['universidad'])

rock_database = {
    'nombre' : 'Diorita',
    'RMR' : 90,
    'UCS' : 250
}
print(rock_database['UCS'])

rock_database = {
    'Diorita' : {
        'RMR' : 90,
        'UCS' : 200,
        'Dureza' : 5

    },
    'Andesita' : {
        'RMR' : 70,
        'UCS' : 220,
        'Dureza' : 8

    }
}

print(rock_database['Andesita']['UCS'])