import getpass
from utils.security import hashPassword
from colorama import Fore, Style, init
import os
import sys

init(autoreset=True)

def userName_validator(for_deletion=False):
    """
    Validates a username input, customizing prompts and messages based on context.

    Args:
        for_deletion (bool): True if the username is being requested for deletion.
                             False for new registration or login.
    """
    while True:
        try:
            if for_deletion:
                userName = input(
                    Fore.YELLOW + "🗑️ Introduce el nombre de usuario a eliminar: ").strip()
            else:
                userName = input(Fore.YELLOW + "👤 Introduce el nombre de usuario: ").strip()

            if not userName:  # Simplified check for empty string after strip()
                raise ValueError(Fore.RED + f"❌ El nombre de usuario no puede estar vacío. Por favor, introduce un valor.")

            if userName.isdigit():
                raise ValueError(
                    Fore.RED + f"❌ El nombre de usuario no puede ser solo números. Debe contener letras o caracteres especiales.")

            if len(userName) > 50:
                raise ValueError(Fore.RED + f"❌ El nombre de usuario no puede tener más de 50 caracteres.")

            return userName
        except ValueError as err:
            print(Fore.RED + f"❌ Error de validación: {err}" + Style.RESET_ALL)
        except Exception as err:
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado durante la validación: {err}" + Style.RESET_ALL)


def password_validator(confirm_password=False):
    """
    Validates a password input, including confirmation for new passwords.
    """
    print(
        Fore.MAGENTA + f"DEBUG: password_validator llamado con confirm_password={confirm_password}" + Style.RESET_ALL)  # DEBUG
    while True:
        try:
            print(Fore.CYAN + "➡️  El programa está esperando tu contraseña. Escríbela y pulsa Enter.")

            if os.name == 'nt' and getPasswordForNtSystems is not None:
                password = getPasswordForNtSystems(Fore.YELLOW + "🔒 Introduce la contraseña: ")
            else:
                password = getpass.getpass(Fore.YELLOW + "🔒 Introduce la contraseña: ")

            password = password.strip()

            print(
                Fore.MAGENTA + f"DEBUG: Primera contraseña obtenida. Longitud: {len(password)}" + Style.RESET_ALL)  # DEBUG

            if not password:
                raise ValueError("La contraseña no puede estar vacía.")

            if len(password) < 8:
                raise ValueError("La contraseña debe tener al menos 8 caracteres.")

            if len(password) > 128:
                raise ValueError("La contraseña no puede tener más de 128 caracteres.")

            print(
                Fore.MAGENTA + f"DEBUG: Primera contraseña validada. confirm_password es {confirm_password}" + Style.RESET_ALL)  # DEBUG

            if confirm_password:  # <--- Si este bloque no se ejecuta, el problema está aquí
                print(Fore.MAGENTA + "DEBUG: Entrando en el bloque de confirmación." + Style.RESET_ALL)  # DEBUG

                print(Fore.CYAN + "➡️  Confirma tu contraseña. Escríbela de nuevo y pulsa Enter.")

                if os.name == 'nt' and getPasswordForNtSystems is not None:
                    confirmedPassword = getPasswordForNtSystems(Fore.YELLOW + "🔒 Confirma la contraseña: ")
                else:
                    confirmedPassword = getpass.getpass(Fore.YELLOW + "🔒 Confirma la contraseña: ")

                confirmedPassword = confirmedPassword.strip()

                print(
                    Fore.MAGENTA + f"DEBUG: Contraseña de confirmación obtenida. Longitud: {len(confirmedPassword)}" + Style.RESET_ALL)  # DEBUG

                if password != confirmedPassword:
                    raise ValueError("Las contraseñas no coinciden. Inténtalo de nuevo.")

                print(Fore.MAGENTA + "DEBUG: Las contraseñas coinciden." + Style.RESET_ALL)  # DEBUG

            print(Fore.MAGENTA + "DEBUG: Saliendo de password_validator con éxito." + Style.RESET_ALL)  # DEBUG
            return password  # <--- Si llega aquí sin pedir confirmación, confirm_password es False
        except ValueError as err:
            print(Fore.RED + f"❌ Error de validación: {err}")
            print(Fore.MAGENTA + "DEBUG: Error de validación, reintentando..." + Style.RESET_ALL)  # DEBUG
        except Exception as err:
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado durante la validación: {err}")
            print(Fore.MAGENTA + "DEBUG: Error inesperado, reintentando..." + Style.RESET_ALL)  # DEBUG


def userNameEditor(oldUserName):
    """
    Edits a username, allowing the user to keep the old one by pressing Enter.

    Args:
        oldUserName (str): The current username.
    """
    while True:
        try:
            newUserName = input(
                Fore.YELLOW + f"👤 Introduce el nuevo nombre de usuario (actual: '{oldUserName}', pulsa Enter para no cambiar): ").strip()

            # If the user pressed Enter without typing, return the old username
            if not newUserName:
                return oldUserName

            if newUserName.isdigit():
                raise ValueError(
                    Fore.RED + f"❌ El nombre de usuario no puede ser solo números. Debe contener letras o caracteres especiales.")

            if len(newUserName) > 50:
                raise ValueError(Fore.RED + f"❌ El nombre de usuario no puede tener más de 50 caracteres.")

            return newUserName
        except ValueError as err:
            print(Fore.RED + f"❌ Error de validación: {err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado: {err}")


def passwordEditor():
    """
    Allows a user to set a new password, with confirmation.
    Returns the hashed new password, or None if the user chose not to change.
    """
    while True:
        try:
            newPassword_input = getpass.getpass(
                Fore.YELLOW + "🔒 Introduce la nueva contraseña (dejar vacío para no cambiar): ").strip()

            if not newPassword_input:  # User chose not to change password
                print(Fore.BLUE + "Contraseña sin cambios.")
                return None

            if len(newPassword_input) < 8:
                raise ValueError(Fore.RED + f"❌ La contraseña debe tener al menos 8 caracteres.")

            confirmNewPassword_input = getpass.getpass(
                Fore.YELLOW + "🔒 Confirma la nueva contraseña: ").strip()

            if newPassword_input == confirmNewPassword_input:
                hashedNewPassword = hashPassword(newPassword_input)  # Hash the confirmed new password
                print(Fore.GREEN + "Contraseña actualizada con éxito.")
                return hashedNewPassword
            else:
                raise ValueError(Fore.RED + f"❌ Las contraseñas no coinciden. Inténtalo de nuevo.")
        except ValueError as err:
            print(Fore.RED + f"❌ Error de validación: {err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado al procesar la contraseña: {err}")

def getPasswordForNtSystems(prompt="🔒 Introduce la contraseña: "):
    import msvcrt
    print(Fore.YELLOW + prompt, end='', flush=True)
    password_chars = []
    while True:
        char = msvcrt.getch()
        if char == b'\r' or char == b'\n': # Enter
            print()
            break
        elif char == b'\x08' or char == b'\x7f': # Backspace o DEL
            if password_chars:
                password_chars.pop()
                sys.stdout.write('\b \b')
                sys.stdout.flush()
        elif len(char) == 1 and (char.isalnum() or (32 <= ord(char) <= 126)):
            password_chars.append(char.decode('utf-8'))
            sys.stdout.write('*')
            sys.stdout.flush()
    return "".join(password_chars)