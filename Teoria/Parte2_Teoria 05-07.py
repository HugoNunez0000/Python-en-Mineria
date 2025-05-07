###POO 05-07###

#Paradigma es una forma de ver las cosas, en programaciòn es una forma de organizar las lineas de codigo
# Clase es para agrupar funciones y variables
# Cosas cotidianas representadas como clases
# atributos son las caracteristicas
# metodos son las funcionalidades


# Plantilla: Modelo que se puede copiar para crear una cosa, las cosas 
# que se crean con las plantillas son los objetos, un objeto puede tener: atributos y metodos

# Esto es una plantilla
# class Zorro:
#     def__init__(self, color, edad, peso):
#     self.color = color
#     self.edad = edad
#     self.peso = peso 


#     def correr(self):

#Cual es la gracia de usar clases?
#R= Por ejemplo queremos crear una aplicaciòn para saber caracteristicas 
#de minerales Calcosina tiene cobre, galena de plomo, atacamita de cobre
#cuando usamos clases solo defines el objeto(ej:Calcosina)

# class Persona:
     #1. Propiedades, caracteristicas o atributos:
# nombre = ''
# apellido = ''
# edad = 0
# dormida = True

#Atribuos de instacia (estado inicial):
#     def __init__(self, ape, nom, edad, dorm): #el parentesis de una funcion(argumento de una funcion) es el contrusctuctor y ente caso es self init
#         self.apellido = ape   ##EL INIT VA A SER LO PRIMERO QUE SE EJHECUTE pq es INICIALIZATION
#         self.nombre = nom 
#         self.edad = edad
#         self.dormida = dorm
#     #      #2. Funcionalidades o mètodos:
#     def despertar(self):
#             self.dormida = False
#             print('!Buen dìa!')
    
# #1.1 Instanciar pasando los valores iniciales :
# persona_1 = Persona('Vivero', 'Guillermo', 28, False)
# print(persona_1.nombre)

# #1.2 Crear una segunda instancia:
# persona_2 = Persona('Nicolas', 'Alarcon', 27, True)
# print(persona_2.dormida)






# #3. Crear una instancia u objeto: #Instanciacion es crear un objeto
# persona_1 = Persona()

# #4. Asignar apellidos a la persona:
# persona_1.apellido = 'Vivero'
# print(persona_1.apellido)

# #self, this, puede ser raton, etc. 

# #5. Despertar a la pesona
# persona_1.despertar() #Llamo a la funcion
# print(persona_1.dormida)  #Al ser una funcion se le pone parentesis

# #eso es porque la variable dormida es una variable dentro de una funcion (local)

# # 6. Crear un segundo objeto persona:
# persona_2 = Persona()
# persona_2.apellido = 'Lopez'

# #7. El objeto se inicia con los valores por dejecto
# print(persona_2.dormida)

class Mineral:

    def __init__(self, nom, col, dur, den): #el parentesis de una funcion(argumento de una funcion) es el contrusctuctor y ente caso es self init
        self.nombre = nom   ##EL INIT VA A SER LO PRIMERO QUE SE EJHECUTE pq es INICIALIZATION
        self.color = col 
        self.dureza = dur
        self.densidad = den
    #      #2. Funcionalidades o mètodos:
    def ElNombre(self):
            print('Este mineral es:', self.nombre) #para acceder a cualquier funcion o variable de la clase es conn self

mineral_1 = Mineral('Bornita', 'Morado', 4, 2.7)

mineral_1.ElNombre()

