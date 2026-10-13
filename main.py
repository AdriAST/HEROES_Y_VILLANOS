from heroe import Heroe
from villano import Villano
from gestion import Gestion
from faker import Faker
import logging
from log import configurar_logger
from datetime import datetime


configurar_logger()
logging.info("Inicio del programa Héroes y Villanos")
fake = Faker("es_ES")
gestion = Gestion()

for i in range(1,21):
    nombre = fake.first_name()
    apellido = fake.last_name()
    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%d/%m/%Y")

    if i <= 10:
        personaje = Heroe(nombre, apellido, fecha_nacimiento, i)
    else:
        personaje = Villano(nombre, apellido, fecha_nacimiento, i)
    gestion.agregar_personaje(personaje)

while True:
    print("\n===== HÉROES Y VILLANOS =====")
    print("1. Listar personajes")
    print("2. Buscar personaje por identificador")
    print("3. Buscar personaje por atributo")
    print("4. Realizar enfrentamiento")
    print("5. Crear personaje")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        gestion.listar_personajes()


    elif opcion == "2":
        try:
            identificador = int(input("Introduce el identificador: "))
            gestion.buscar_personaje(identificador)
        except ValueError:
            print("Error: debes introducir un número entero")
            logging.warning("Se ha introducido un identificador no válido")


    elif opcion == "3":

        atributo = input("Introduce el atributo: ")

        valor = input("Introduce el valor: ")

        if atributo in ["identificador", "puntuacion_total",

                        "codigo_limpio", "bien_documentado",

                        "git_god", "arquitecto", "detallista",

                        "chagepeteador", "entregador_tardio",

                        "ausencias", "hablador"]:

            try:

                valor = int(valor)

            except ValueError:

                print("Error: este atributo necesita un número")

                logging.warning("Valor numérico incorrecto en búsqueda")

                continue

        gestion.buscar_por_atributo(atributo, valor)

    elif opcion == "4":
        gestion.pelea()

    elif opcion == "5":
        tipo = input("¿Quieres crear un héroe o un villano?: ").lower()

        if tipo == "heroe" or tipo == "héroe":
            clase = Heroe
        elif tipo == "villano":
            clase = Villano
        else:
            print("Tipo de personaje incorrecto")
            continue

        nombre = input("Introduce el nombre: ")
        apellido = input("Introduce el apellido: ")
        fecha = input("Introduce la fecha de nacimiento (dd/mm/aaaa): ")

        try:
            fecha_comprobada = datetime.strptime(fecha, "%d/%m/%Y")

            if fecha_comprobada.date() > datetime.today().date():
                print("Error: la fecha no puede ser futura")
                logging.warning(f"Fecha de nacimiento futura: {fecha}")
                continue

        except ValueError:
            print("Error: la fecha debe tener el formato dd/mm/aaaa y ser válida")
            logging.warning(f"Fecha de nacimiento incorrecta: {fecha}")
            continue

        try:
            identificador = int(input("Introduce el identificador: "))
            personaje = clase(nombre, apellido, fecha, identificador)
            gestion.agregar_personaje(personaje)
        except ValueError:
            print("Error: el identificador debe ser un número entero")

    elif opcion == "6":
        print("Saliendo del programa...")
        logging.info("Fin del programa")
        break

    else:
        print("Opción incorrecta")
        logging.warning("Opción de menú incorrecta")


