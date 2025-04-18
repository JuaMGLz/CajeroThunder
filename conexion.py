from pymongo import MongoClient
import certifi

def obtener_conexion():
    uri = "mongodb+srv://admin:cajero1234@cluster0.ndweyrc.mongodb.net/?retryWrites=true&w=majority&tls=true&tlsCAFile=" + certifi.where()
    client = MongoClient(uri)
    db = client["banco_db"]
    return db


import certifi
print("Certifi path en Render:", certifi.where())