from pymongo import MongoClient

def obtener_conexion():
    client = MongoClient("mongodb://admin:cajero1234@localhost:27017/?authSource=admin")
    db = client["banco_db"]
    return db
