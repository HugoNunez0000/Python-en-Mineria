### TAREA 2 CLASES Y HERENCIA ###
### HUGO NÚÑEZ PECHUANTE ###

'''PARTE 1 DEFINICION DE CLASES'''

print("PARTE 1")
print("\n")


class Explosives:
    def __init__(
            self, commercial_name,
            explosive_density,
            vod, relative_power,
            water_resistance):

        self.commercial_name = commercial_name
        self.explosive_density = explosive_density
        self.vod = vod
        self.relative_power = relative_power
        self.water_resistance = water_resistance
        return

    def detonation_pressure(self):
        presideton = (1/4)*self.explosive_density*self.vod**2
        print(
            f"La presion de detonacion del explosivo {self.commercial_name} es: {presideton} kPa")
        return

    def linear_density(self, diameter_mm):
        densilin = (3.1416/4)*diameter_mm**2*self.explosive_density
        print(
            f"Considerando un diametro de {diameter_mm} mm, la densidad lineal del explosivo {self.commercial_name} es: {densilin} kilogramos por metro")
        return

    def kg_anfo_equivalent(self, weight_explosive):
        kg_ANFO = (self.relative_power*weight_explosive)/100
        print(
            f"500 kilogramos del explosivo {self.commercial_name} equivalen a {kg_ANFO} kg de ANFO")
        return

    def is_for_water(self):
        if self.water_resistance == 'Si':
            print(
                f"El explosivo {self.commercial_name} Sí es resistente al agua")
        elif self.water_resistance == 'No':
            print("El explosivo No es resitente al agua")
        return


# CREACION DE 2 EXPLOSIVOS

# Instanciar pasando los valores iniciales :
Explosive_1 = Explosives('Tronex Plus', 1.18, 5200, 1.22, 'Si')

# Crear una segunda instancia:
Explosive_2 = Explosives('Emultex CP', 1.15, 4400, 0.89, 'Si')

# a) Calcular las presiones de detonación
Explosive_1.detonation_pressure()
Explosive_2.detonation_pressure()
print("\n")

# b) Densidad lineal para diametro de 140 mm
Explosive_1.linear_density(140)
Explosive_2.linear_density(140)
print("\n")

# c) A cuántos kg de ANFO equivalen 500 kg del explosivo
Explosive_1.kg_anfo_equivalent(500)
Explosive_2.kg_anfo_equivalent(500)
print("\n")

# d) ¿Los explosivos son resistentes al agua?
Explosive_1.is_for_water()
Explosive_2.is_for_water()
print("\n")


print("PARTE 2")
print("\n")
