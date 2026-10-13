from heroe import Heroe
from villano import Villano
import random
import logging

class Gestion:
    def __init__(self):
        self.personajes = {}

    def agregar_personaje(self, personaje):
        if personaje.identificador not in self.personajes:
            self.personajes[personaje.identificador] =  personaje
            logging.info(f"personaje agregado: {personaje.nombre} {personaje.apellido} con id {personaje.identificador}")
        else:
            print("Error el id ya está ocupado")
            logging.error(f"Id duplicado: {personaje.identificador}")

    def listar_personajes(self):
        if not self.personajes:
            print("No hay ningún personaje para mostrar")
        else:
            for personaje in self.personajes.values():
                print(personaje)

    def buscar_personaje(self, identificador):
        if identificador in self.personajes:
            print(self.personajes[identificador])
        else:
            print("No se ha encontrado el personaje")

    def buscar_por_nombre(self, nombre):
        encontrado = False
        for personaje in self.personajes.values():
            if personaje.nombre == nombre:
                print(personaje)
                encontrado = True
        if not encontrado:
                print("No se ha encontrado ningún personaje con ese nombre")


    def buscar_por_apellido(self, apellido):
        encontrado = False
        for personaje in self.personajes.values():
            if personaje.apellido == apellido:
                print(personaje)
                encontrado = True
        if not encontrado:
                print("No se ha encontrado ningún personaje con ese apellido")

    def buscar_por_atributo(self, atributo, valor):
        encontrado = False
        atributo_existe = False

        for personaje in self.personajes.values():
            if hasattr(personaje, atributo):
                atributo_existe = True

                if getattr(personaje, atributo) == valor:
                    print(personaje)
                    logging.info(f"Personaje encontrado por {atributo}: {valor}")
                    encontrado = True

        if not atributo_existe:
            print("Error: el atributo introducido no existe")
            logging.warning(f"Atributo inexistente: {atributo}")

        elif not encontrado:
            print("No se ha encontrado ningún personaje")
            logging.warning(f"No se ha encontrado ningún personaje con {atributo}: {valor}")

    def pelea(self):
        heroes = []
        villanos = []

        for personaje in self.personajes.values():
            if isinstance(personaje, Heroe):
                heroes.append(personaje)
            elif isinstance(personaje, Villano):
                villanos.append(personaje)
            else:
                print("El personaje no está calificado como héroe o villano")

        if not heroes or not villanos:
            print("No hay suficientes personajes para realizar una pelea")
            logging.warning("No hay suficientes personajes para realizar una pelea")
        else:
            heroe_elegido = random.choice(heroes)
            villano_elegido = random.choice(villanos)
            logging.info(f"Enfrentamiento entre héroe {heroe_elegido.nombre} y villano {villano_elegido.nombre}")

            print("\n--- ENFRENTAMIENTO ---")
            print(f"Héroe: {heroe_elegido.nombre} - {heroe_elegido.puntuacion_total} puntos")
            print(f"Villano: {villano_elegido.nombre} - {villano_elegido.puntuacion_total} puntos")

            diferencia = abs(heroe_elegido.puntuacion_total - villano_elegido.puntuacion_total)

            print(f"Diferencia de puntuación: {diferencia} puntos")

            if diferencia <= 20:
                print("El enfrentamiento está equilibrado")
            else:
                print("El enfrentamiento está desequilibrado")

            if heroe_elegido.puntuacion_total > villano_elegido.puntuacion_total:
                print(f"El ganador es el héroe {heroe_elegido.nombre}")
                logging.info(f"Ganador del enfrentamiento: Héroe {heroe_elegido.nombre}")
            elif heroe_elegido.puntuacion_total == villano_elegido.puntuacion_total:
                print("¡El enfrentamiento ha terminado en empate!")
                logging.info("El enfrentamiento ha terminado en empate")
            else:
                print(f"El ganador es el villano {villano_elegido.nombre}")
                logging.info(f"Ganador del enfrentamiento: Villano {villano_elegido.nombre}")






