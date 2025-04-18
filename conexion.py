from pymongo import MongoClient
import certifi

def obtener_conexion():
    print("Ubicación del certificado:", certifi.where())  # esto lo verás en los logs de Render
    uri = "mongodb+srv://admin:cajero1234@cluster0.ndweyrc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    cliente = MongoClient(uri, tlsCAFile=certifi.where())
    db = cliente["banco_db"]
    return db

import certifi
print("Certifi path en Render:", certifi.where())