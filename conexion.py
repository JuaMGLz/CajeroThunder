from pymongo import MongoClient
import os

def obtener_conexion():
    # Usa URI del entorno si está disponible, si no, usa localhost
    mongo_uri = os.environ.get("MONGO_URI", "mongodb+srv://admin:cajero1234@cluster0.ndweyrc.mongodb.net/banco_db?retryWrites=true&w=majority")
    client = MongoClient(mongo_uri)
    db = client["banco_db"]
    return db
