
'''CLASES'''

# class Person:
#     def __init__(self, name, age, job, area):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.area = area
    
#     def greet(self): #'El self solamente me dice que esta funcion esta dentro de mi clase'
#         print(f"Hola , soy {self.name}, tengo {self.age} años")
    
# persona1 = Person("Hugo", 23, "Ingeniero", "Tronadura")
# persona1.greet()

class Machine:
    def __init__(self, type, model, performance):
        self.type = type
        self.model = model
        self.performance = performance
        return
    
    def presentation(self):
        print(f"Tipo: {self.type}, Modelo: {self.model}, Rendimiento: {self.performance}")
        return
    
    def fuel(self, distance):
        needed_fuel = distance/self.performance
        print(f"Para avanzar {distance} km, necesitamos {needed_fuel} litros de combustible.")
        return



camion1 = Machine("Camion", "CAT", 0.2)
camion1.presentation()
camion1.fuel(340)


# class Rock:
#     def __init__(self, rocktype, density, grade):
#         self.rocktype = rocktype
#         self.density = density
#         self.grade = grade

#     def value(self, volume, price, recovery, costs):
#         block_tonnage = volume * self.density
#         earnings = block_tonnage * price * recovery *
#         losses = 

# rock1 = Rock(
#     rocktype = 'Calcopirita',
#     density = 2.78,
#     grade = 0.9)

# rock1.value(
# )

class Person:
    def __init__(self, name, age, job, area, income):
        self.name = name
        self.age = age
        self.job = job
        self.area = area
        self.income = income


    def presentation(self): #'El self solamente me dice que esta funcion esta dentro de mi clase'
        print(f"Hola , soy {self.name} y tengo {self.age} años")
        return

    def income_greet(self):
        print(f"Soy {self.name} y gano {self.income} pesos")

    def years(self):
        if self.age > 30:
            # self.income = self.income * 2
            self.income *= 2




persona1 = Person("Hugo", 33, "Ingeniero", "Tronadura", 1200000)
persona1.presentation()
persona1.income_greet()
persona1.years()
persona1.income_greet()