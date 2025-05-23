from controllers.user_validators import password_validator, userName_validator
from database.db import SessionLocal
from models.users_model import User
from utils.security import hashPassword, checkPassword
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

db = SessionLocal()

def userRegister():
    try:
        userName = userName_validator()
        password = password_validator(True)

        existingUser = db.query(User).filter_by(username=userName).first()
        print(existingUser)


        if existingUser: 
            print(f"El nombre de usuario {userName} ya existe, por favor elige otro.")
    
        hashedPassword = hashPassword(password)
        newUser = User(username = userName , password_hash = hashedPassword)
        db.add(newUser)
        db.commit()
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
        user = db.query(User).filter_by(username=userName).first()
        if user and checkPassword(password, user.password_hash):
            print(f"¡Bienvenido/a! {user.username}")
            return user
        else:
            print("El nombre de usuario o la contraseña son incorrectos.")
            return None
    except Exception as err:
        print(f"Ha ocurrido un error inesperado al iniciar sesión {err}")


