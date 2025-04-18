from pymongo import MongoClient

def obtener_conexion():
    uri = "mongodb://admin:<db_password>@ac-vphjntx-shard-00-00.ndweyrc.mongodb.net:27017,ac-vphjntx-shard-00-01.ndweyrc.mongodb.net:27017,ac-vphjntx-shard-00-02.ndweyrc.mongodb.net:27017/?ssl=true&replicaSet=atlas-tdwl2z-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"
    cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)
    db = cliente["banco_db"]
    return db
