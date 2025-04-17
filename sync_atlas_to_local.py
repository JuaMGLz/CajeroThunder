from pymongo import MongoClient
import time

# URIs
uri_atlas = "mongodb+srv://admin:cajero1234@cluster0.ndweyrc.mongodb.net/?retryWrites=true&w=majority"
uri_local = "mongodb://localhost:27017"

# Conexiones
cliente_atlas = MongoClient(uri_atlas)
cliente_local = MongoClient(uri_local)

# Bases de datos
db_atlas = cliente_atlas["banco_db"]
db_local = cliente_local["banco_db"]

# Colecciones a sincronizar
colecciones = ["cuentas", "retiros", "clientes"]  # agrega todas las que uses

for coleccion in colecciones:
    print(f"Sincronizando colección: {coleccion}")
    
    # Obtenemos los documentos de Atlas
    docs = list(db_atlas[coleccion].find())
    
    # Eliminamos en local para evitar duplicados
    db_local[coleccion].delete_many({})
    
    # Insertamos en local
    if docs:
        db_local[coleccion].insert_many(docs)

print("✅ Sincronización completada correctamente.")
