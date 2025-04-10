def multiplicar(x, y): return x*y


print(multiplicar(3, 4))

# def SE USA PARA DEFINIR UNA FUNCION

# FUNCIONN RECIBE LISTA DE NUMEROS Y DEVUELVE LISTA CON PARES


def filtrar_pares(lista_numeros):
    pares = []
    for num in lista_numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares


# EJEMPLO DE USO
numeros = [x for x in range(1, 10+1)]
print(filtrar_pares(numeros))  # SALIDA_ [2, 4, 6, 8, 10]

# CONTAR VECES QUE APARECE UNA PALABRA


def contar_palabras(frase):
    palabras = frase.lower().split()  # LOWER HACE TODAS MINUSCULAS
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo


# EJEMPLO DE USO:
texto = "EL SOL BRILLA Y EL CIELO ESTA DESPEJADO"
texto = input('Ingresa una oracion: ')
print(contar_palabras(texto))
# Salida: {'el' : 2, 'sol' : 1....}

# todas las variables que definimos dentro de nuestras FUNCIONES SOLO SE UTILIZARAN DENTRO DE LA FUNCION

# while True: --> hace que el while inicie altiro
# int ---> numero entero ej: 3,9 ,16
# random ---> crea numeros random entre cierto rango

# Gestor de tareas
# def gestor_tareas():
# tareas = []
# while True:
#   print("Gestor de tareas")
# print("1. Agregar tarea")

# def calculo_circulo():
# radio=


def perimetro_area(a):  # aqui a es el argumento
    perimetro = 2 * 3, 1415*a
    area = 3, 1415 * a**2
    return (perimetro, area)


result = perimetro_area(5)
print(result)
