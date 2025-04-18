from pymongo import MongoClient

def obtener_conexion():
    uri = "mongodb+srv://admin:cajero1234@cluster0.ndweyrc.mongodb.net/?retryWrites=true&w=majority"
    cliente = MongoClient(uri)
    return cliente["banco_db"]

from pymongo import MongoClient

client = MongoClient("mongodb://USER:PASS@mongo:27017/db?authSource=admin")
db = client["db"]
