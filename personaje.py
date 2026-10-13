from datetime import datetime, date

class Personaje:

    def __init__(self, nombre, apellido, fecha_nacimiento, identificador):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.identificador = identificador
        self.puntuacion_total = 0
    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
         f"Apellidos: {self.apellido}\n"
         f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
         f"Identificador: {self.identificador}\n"
         f"Puntuación total: {self.puntuacion_total}\n"
         f"Edad: {self.calcular_edad()} años")

    def calcular_edad(self):
        fecha = datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y").date()
        anio_nacimiento = fecha.year
        hoy = date.today()
        edad_real = hoy.year - anio_nacimiento
        if(hoy.month, hoy.day) < (fecha.month, fecha.day):
            edad_real -= 1
        return edad_real