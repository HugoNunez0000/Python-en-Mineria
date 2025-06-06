### TAREA 2 CLASES Y HERENCIA ###
### HUGO NÚÑEZ PECHUANTE ###

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
        print(f"La presion de detonacion del explosivo es: {presideton} kPa")
        return

    def linear_density(self, diameter):
        densilin = (3.1416/4)*diameter**2*self.explosive_density
        print(f"La densidad lineal del explosivo es: {densilin} kg/m")
        return

    def kg_anfo_equivalent(self, weight_explosive):
        kg_ANFO = (self.relative_power*weight_explosive)/100
        print(
            f" 500 kilogramos del explosivo equivalen a {kg_ANFO} kg de ANFO")
        return

    def is_for_water(self):
        if self.water_resistance == "Si":
            print("El explosivo Sí es resistente al agua")
        elif self.water_resistance == "No":
            print("El explosivo No es resitente al agua")
        return


explosivo1 = Explosives("ANFO", 2.6, 3, 6, "No")
explosivo1.detonation_pressure()
explosivo1.linear_density(80)
explosivo1.kg_anfo_equivalent(500)
explosivo1.is_for_water()
