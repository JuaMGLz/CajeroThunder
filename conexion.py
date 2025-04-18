def obtener_conexion():
    from pymongo import MongoClient
    uri = "mongodb+srv://admin:cajero1234@cluster0.ndweyrc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    try:
        cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)
        cliente.admin.command('ping')  # Forzar prueba de conexión
        return cliente["banco_db"]
    except Exception as e:
        print("❌ Error de conexión:", e)
        return None
