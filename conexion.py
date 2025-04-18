from pymongo import MongoClient
import os

# Obtenemos la URI desde variables de entorno
MONGO_URI = os.environ.get("MONGO_URI")

def obtener_conexion():
    client = MongoClient(MONGO_URI)
    db = client["banco_db"]
    return db

# Validación al iniciar
try:
    client = MongoClient(MONGO_URI)
    client.admin.command('ping')
    print("✅ Conexión exitosa a MongoDB Atlas")
except Exception as e:
    print("❌ Error de conexión:", e)
