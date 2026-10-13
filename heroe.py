from personaje import Personaje
import random

class Heroe(Personaje):
    def __init__(self, nombre, apellido, fecha_nacimiento, identificador):
        super().__init__(nombre, apellido, fecha_nacimiento, identificador)
        self.codigo_limpio = random.randint(0,100)
        self.bien_documentado = random.randint(0,100)
        self.git_god = random.randint(0,100)
        self.arquitecto = random.randint(0,100)
        self.detallista = random.randint(0,100)
        self.puntuacion_total = round((self.codigo_limpio + self.bien_documentado + self.git_god + self.arquitecto + self.detallista)/ 5)

    def __str__(self):
        return super().__str__() + (f"\nCódigo limpio {self.codigo_limpio}"
                                    f"\nBien documentado {self.bien_documentado}"
                                    f"\nGIT god {self.git_god}"
                                    f"\nArquitecto {self.arquitecto}"
                                    f"\nDetallista {self.detallista}")
