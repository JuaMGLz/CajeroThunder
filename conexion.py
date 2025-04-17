from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

usuario = "admin"
password = "cajero1234"
host = "187.190.159.78"
puerto = 27017
base_datos = "banco_db"

uri = f"mongodb://{usuario}:{password}@{host}:{puerto}/?authSource=admin"

def obtener_conexion():
    try:
        client = MongoClient(uri)
        client.admin.command('ping')  # Verifica la conexión
        db = client[base_datos]
        return db
    except ConnectionFailure as e:
        print("Error de conexión:", e)
        return None
