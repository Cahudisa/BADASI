from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://Escritor:123456@localhost:27017/redne?authSource=redne")
db = client["redne"]

colec_actual = db["metadatos_EV"]
colec_versiones = db["metadatos_EV_versiones"]

def guardar_o_actualizar(doc):
    trace_id = doc["_id"]
    
    # Buscar si ya existe
    anterior = colec_actual.find_one({"_id": trace_id})

    # === Caso 1: NO EXISTE → Inserción normal ===
    if anterior is None:
        doc["version"] = 1
        colec_actual.insert_one(doc)
        return "insertado"

    # === Caso 2: EXISTE → Guardar versión previa ===
    version_prev = anterior.get("version", 1)
    
    colec_versiones.insert_one({
        "trace_id": trace_id,
        "version": version_prev,
        "fecha": datetime.utcnow().isoformat(),
        "metadata": anterior
    })

    # === Caso 3: Actualizar documento principal ===
    nueva_version = version_prev + 1
    doc["version"] = nueva_version
    
    colec_actual.update_one(
        {"_id": trace_id},
        {"$set": doc}
    )
    
    return "actualizado"




