from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Parámetros de conexión
usuario = "admin"
password = "cajero1234"
host = "localhost"
puerto = 27017
base_datos = "banco_db"

uri = f"mongodb://{usuario}:{password}@{host}:{puerto}/?authSource=admin"

# Función para verificar la existencia de una cuenta
def verificar_cuenta(num_cuenta):
    try:
        client = MongoClient(uri)
        db = client[base_datos]
        cuenta = db.cuentas.find_one({"num_cuenta": num_cuenta})
        if cuenta:
            cliente = db.clientes.find_one({"id_cliente": cuenta["id_cliente"]})
            return {"ok": True, "cuenta": cuenta, "cliente": cliente}
        return {"ok": False}
    except ConnectionFailure as e:
        return {"ok": False, "error": str(e)}

# Prueba con un número de cuenta de ejemplo
verificar_cuenta("547218395")