from pymongo import MongoClient
import os
import certifi
from pymongo.ssl_support import get_ssl_context

def obtener_conexion():
    uri = os.getenv("MONGO_URI")  # mejor usar variable de entorno
    if not uri:
        raise Exception("MONGO_URI no definida")

    ssl_context = get_ssl_context(ca_certs=certifi.where())

    client = MongoClient(uri, ssl=True, ssl_cert_reqs='CERT_REQUIRED', ssl_ca_certs=certifi.where())
    return client["banco_db"]
