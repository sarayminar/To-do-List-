from colorama import Fore
from sqlalchemy.exc import IntegrityError

from controllers.user_validators import password_validator, userName_validator
from controllers.user_validators import userNameEditor, passwordEditor
from database.db import SessionLocal
from models.users_model import User
from utils.security import hashPassword, checkPassword
from views.user_view import showAllUsers


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def userRegister(db):
    try:
        userName = userName_validator()
        password = password_validator(True)

        existingUser = db.query(User).filter_by(username=userName).first()
        if existingUser:
            print(Fore.YELLOW + f"⚠️ El nombre de usuario {userName} ya existe, por favor elige otro.")

        hashedPassword = hashPassword(password)
        newUser = User(username=userName, password_hash=hashedPassword, is_admin=False)
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
        return newUser
    except IntegrityError as err:
        db.rollback()
        print(
            Fore.RED + f"❌ El nombre de usuario {userName} ya está en uso o tiene conflicto con la base de datos {err}.")
    except Exception as err:
        db.rollback()
        print(Fore.RED + f"❌ Ha ocurrido un error inesperado al registrar al usuario {err}")


def loginUser():
    with SessionLocal() as db:
        try:
            print("Iniciando sesión...")
            userName = userName_validator()
            password = password_validator()
            user = db.query(User).filter_by(username=userName).first()
            if user and checkPassword(password, user.password_hash):
                print(Fore.CYAN + f"👤 ¡Bienvenido/a! {user.username}")
                return user
            else:
                print(Fore.RED + f"❌ El nombre de usuario o la contraseña son incorrectos.")
                return None
        except Exception as err:
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado al iniciar sesión {err}")


def deleteuser():
    with SessionLocal() as db:
        try:
            username = userName_validator(True);
            user = db.query(User).filter(User.username == username).first();
            if not user:
                raise ValueError(Fore.RED + f"❌ El usuario no existe. No se pudo eliminar.");
            if user.is_admin:
                raise PermissionError(Fore.RED + f"❌ No se puede eliminar un usuario administrador");
            db.delete(user);
            db.commit();
            print(Fore.GREEN + f"🗑️ Usuario '{user.username}' eliminado correctamente.")
            getAllUsers()
        except ValueError as err:
            print(Fore.RED + f"❌ {err}")
        except PermissionError as err:
            print(Fore.RED + f"❌ {err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado {err}")


def getAllUsers():
    with SessionLocal() as db:
        try:
            allusers = db.query(User).all();
            showAllUsers(allusers);
        except Exception as err:
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado {err}")


def editUser():
    with SessionLocal() as db:
        try:
            userName = userName_validator()
            user = db.query(User).filter(User.username == userName).first()
            if not user:
                raise ValueError(Fore.RED + f"❌ El usuario '{userName}' no existe. No se puede editar.")
            if user.is_admin:
                raise PermissionError(Fore.RED + f"❌ No se puede editar un usuario administrador directamente aquí.")

            original_username_value = user.username
            user.username = userNameEditor(user.username)

            if user.username != original_username_value:
                existing_user_with_new_name = db.query(User).filter(User.username == user.username).first()
                if existing_user_with_new_name and existing_user_with_new_name.id != user.id:
                    raise ValueError(
                        Fore.RED + f"❌ El nuevo nombre de usuario '{user.username}' ya está en uso. Por favor, elige otro.")
                print(Fore.BLUE + f"👤 Nombre de usuario cambiado a '{user.username}'.")
            else:
                print(Fore.BLUE + "👤 Nombre de usuario sin cambios.")

            new_password_hash_result = passwordEditor()
            if new_password_hash_result is not None:
                user.password_hash = new_password_hash_result
                print(Fore.BLUE + "🔒 Contraseña actualizada correctamente.")
            else:
                print(Fore.BLUE + "🔒 Contraseña sin cambios.")

            if user.username != original_username_value or new_password_hash_result is not None:
                db.commit()
                db.refresh(user)
                print(Fore.GREEN + f"✅ Usuario '{user.username}' actualizado correctamente.")
            else:
                db.rollback()
                print(Fore.BLUE + "ℹ️ No se realizaron cambios en el usuario.")

        except ValueError as err:
            db.rollback()
            print(Fore.RED + f"❌ Error de validación: {err}")
        except PermissionError as err:
            db.rollback()
            print(Fore.RED + f"❌ Error de permisos: {err}")
        except Exception as err:
            db.rollback()
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado al editar el usuario: {err}")
