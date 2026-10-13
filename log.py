import logging

def configurar_logger():
    logging.basicConfig(
        filename="heroes_villanos.log",
        level= logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )