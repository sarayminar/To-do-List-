# database/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de conexión (ajusta la contraseña si es diferente a '1234')
DATABASE_URL = "postgresql+pg8000://postgres:123456@localhost/todo_db"
#DATABASE_URL = "postgresql+pg8000://postgres:clancy21@localhost/todo_db" #Saray

# Motor de conexión
engine = create_engine(DATABASE_URL)

# Sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


