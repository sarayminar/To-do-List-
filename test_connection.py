# test_connection.py
from database.db import SessionLocal

try:
    # Intenta crear una sesión
    session = SessionLocal()
    print("✅ Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"❌ Error al conectar: {e}")
finally:
    session.close()
