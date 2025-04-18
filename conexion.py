from pymongo import MongoClient

def obtener_conexion():
    uri = "mongodb+srv://admin:cajero1234@cluster0.ndweyrc.mongodb.net/banco_db?retryWrites=true&w=majority"
    cliente = MongoClient(uri)
    return cliente

import os
from pymongo import MongoClient

uri = os.getenv("MONGO_URI")
cliente = MongoClient(uri)
db = cliente["banco_db"]
