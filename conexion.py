from pymongo import MongoClient

def obtener_conexion():
    uri = "mongodb://admin:cajero1234@ac-vphjntx-shard-00-00.ndweyrc.mongodb.net:27017,ac-vphjntx-shard-00-01.ndweyrc.mongodb.net:27017,ac-vphjntx-shard-00-02.ndweyrc.mongodb.net:27017/banco_db?ssl=true&replicaSet=atlas-tdwl2z-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"
    cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)

    try:
        cliente.admin.command('ping')
        print("✅ Conexión exitosa con MongoDB Atlas")
    except Exception as e:
        print("❌ Error en conexión con MongoDB Atlas:", e)

    db = cliente["banco_db"]
    return db
