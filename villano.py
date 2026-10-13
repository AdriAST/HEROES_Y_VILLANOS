from personaje import Personaje
import random

class Villano(Personaje):
    def __init__(self, nombre, apellido, fecha_nacimiento, identificador):
        super().__init__(nombre, apellido, fecha_nacimiento, identificador)
        self.chagepeteador = random.randint(0,100)
        self.entregador_tardio = random.randint(0,100)
        self.ausencias = random.randint(0,100)
        self.hablador = random.randint(0,100)
        self.puntuacion_total = round((self.chagepeteador + self.entregador_tardio + self.ausencias + self.hablador) / 4)

    def __str__(self):
        return super().__str__() + (f"\nChagepeteador {self.chagepeteador}"
                                    f"\nEntregador tardio {self.entregador_tardio}"
                                    f"\nAusencias {self.ausencias}"
                                    f"\nHablador {self.hablador}")