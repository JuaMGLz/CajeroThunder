from pymongo import MongoClient

def obtener_conexion():
    try:
        uri = "mongodb+srv://admin:cajero1234@cluster0.ndweyrc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        cliente = MongoClient(uri)
        db = cliente["banco_db"]  # Asegúrate de que este sea tu nombre real de base
        return db
    except Exception as e:
        print("❌ Error de conexión con MongoDB Atlas:", e)
        return None

import certifi
print("Certifi path en Render:", certifi.where())