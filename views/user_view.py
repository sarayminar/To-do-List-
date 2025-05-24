from colorama import init, Fore, Style
import os

init(autoreset=True)

def showAllUsers(users):
    if users:
            print(Fore.CYAN + "📋 Lista de usuarios registrados:")
            for user in users:
                admin = Fore.RED + "🛡️ Administrador" if user.is_admin else Fore.GREEN +  "👤 Estandar"
                print(Fore.CYAN + f"🆔 {user.id} - Usuario: {user.username}  , rol {admin}");
    else:
        print(Fore.YELLOW + "📭 No hay usuarios registrados.")