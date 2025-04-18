from pymongo import MongoClient
import os

def obtener_conexion():
    # Usa URI del entorno si está disponible, si no, usa localhost
    mongo_uri = os.environ.get("MONGO_URI", "mongodb://admin:cajero1234@localhost:27017/?authSource=admin")
    client = MongoClient(mongo_uri)
    db = client["banco_db"]
    return db
