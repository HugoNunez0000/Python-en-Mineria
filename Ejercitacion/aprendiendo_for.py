### EJERCICIOS PARA FOR ###

lista_1 = [1, 2, 87, 43, 21, 15, 6, 16, 26, 100]
lista_2 = [0.33, 'kiwi', 'top', 27, 0.11111]

print(lista_1)

print(lista_2, "\n")


for i in range(len(lista_1)):  # IN RANGE
    print(i)  # va de 0 a 9

print("\n")
# IN ENUMERATE Lo deja como tupla (2, 87) eso hace que no se pueda cambiar
for i, lista_enumerada in enumerate(lista_1):
    print(i, lista_enumerada)

print("\n")
for i in range(len(lista_1)):  # aparece en azul pq me recomienda enumerate
    a = lista_1[i]
    if a >= 15:
        lista_1[i] = 'chanchito'

print(lista_1, "\n")

for i in enumerate(lista_2):
    print(i)

print("\n")
for i in range(len(lista_2)):
    b = lista_2[i]
    if b == 27:
        lista_2[i] = 'magia'

print(lista_2)

tupla_top = (1, 2, 3)

print('hola mundo! \n')
