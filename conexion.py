from pymongo import MongoClient
import certifi
import os

def obtener_conexion():
    # Leer URI desde variable de entorno en Render
    uri = os.getenv("MONGO_URI")
    if uri is None:
        raise Exception("No se encontró la variable MONGO_URI en el entorno.")

    # Agregar seguridad TLS y certificado
    uri += "&tls=true&tlsCAFile=" + certifi.where()

    client = MongoClient(uri)
    return client["banco_db"]