from controllers.user_validators import password_validator, userName_validator
from database.db import SessionLocal
from models.users_model import User
from utils.security import hashPassword, checkPassword
from sqlalchemy.exc import IntegrityError

db = SessionLocal()

def userRegister():
    try:
        userName = userName_validator()
        password = password_validator(True)

        existingUser = db.query(User).filter_by(name=userName).first

        if existingUser: 
            print(f"El nombre de usuario {userName} ya existe, por favor elige otro.")
    
        hashedPassword = hashPassword(password)
        newUser = User(name = userName , password_hash = hashedPassword)
        return newUser
    except IntegrityError as err: 
        db.rollback()
        print(f"El nombre de usuario {userName} ya está en uso o tiene conflicto con la base de datos {err}.")
    except Exception as err:
        db.rollback()
        print(f"Ha ocurrido un error inesperado al registrar al usuario {err}")

def loginUser():
    try:
        print("Iniciando sesión...")
        userName = userName_validator()
        password = password_validator()
        user = db.query(User).filter_by(userName=userName).first
        if user and checkPassword(password, user.password_hash):
            print(f"¡Bienvenido/a! {user.name}")
            return user
        else:
            print("El nombre de usuario o la contraseña son incorrectos.")
            return None
    except Exception as err:
        print("Ha ocurrido un error inesperado al iniciar sesión")


