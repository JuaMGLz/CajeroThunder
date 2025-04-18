from pymongo import MongoClient

def obtener_conexion():
    uri = "mongodb+srv://admin:cajero1234@cluster0.ndweyrc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)
    db = cliente["banco_db"]
    return db
