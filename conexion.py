from pymongo import MongoClient

def obtener_conexion():
    uri = "mongodb://admin:cajero1234@ac-vphjntx-shard-00-00.ndweyrc.mongodb.net:27017,ac-vphjntx-shard-00-01.ndweyrc.mongodb.net:27017,ac-vphjntx-shard-00-02.ndweyrc.mongodb.net:27017/?ssl=true&replicaSet=atlas-5dfc70-shard-0&authSource=admin&retryWrites=true&w=majority"
    cliente = MongoClient(uri)
    db = cliente["banco_db"]
    return db
