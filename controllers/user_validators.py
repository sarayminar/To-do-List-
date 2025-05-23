
def userName_validator():
    while True:
        try:
            userName = input("Introduce tu nombre de usuario: ")
            if not userName.strip():
                raise ValueError ("No puedes introducir un nombre vacío.")
            if userName.isdigit():
                raise ValueError("No puedes introducir un valor numérico.")
            if len(userName) > 50:
                raise ValueError("No pude tener más de 50 caracteres.")
            return userName
        except ValueError as err:
            print(f" {err}") 
        except Exception as err:
            print(f"Ha ocurrido un error inesperado {err}")


def password_validator(bool=None):
    while True:
        try:
            password = input("Introduce tu contraseña: ")
            if not password.strip():
                raise ValueError ("No puedes introducir una contraseña vacío.")
            if len(password) < 6:
                raise ValueError("No puedes introducir una contraseña menor de 6 caracteres")
            if bool:
                confirmedPassword = input("Introduce de nuevo tu contraseña: ")
                if password != confirmedPassword:
                    raise ValueError("Las contraseñas deben ser iguales. Inténtalo de nuevo.")             
            return password
        except ValueError as err:
            print(f" {err}") 
        except Exception as err:
            print(f"Ha ocurrido un error inesperado {err}")