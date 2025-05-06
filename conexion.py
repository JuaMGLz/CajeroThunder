from pymongo import MongoClient

def obtener_conexion():
    # Conexión local con autenticación
    mongo_uri = "mongodb://admin:cajero1234@localhost:27017/"
    client = MongoClient(mongo_uri)
    db = client["banco_db"]
    return db

