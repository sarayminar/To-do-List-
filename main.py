from colorama import init, Fore, Style
from controllers.task_controller import (
    crear_tarea,
    actualizar_tarea,
    eliminar_tarea,
    searchAllTasksForUser,
    searchAllTasksForUserStatus,
    searchAllTasksForUserStatusPriority,
    searchTasksForUserTitle,
    ver_tareas,
)
from controllers.user_controller import (
    loginUser,
    userRegister,
    deleteuser,
    getAllUsers,
    editUser
)
from models.users_model import User
from models.task_model import Task

init(autoreset=True)
user = None


def menu():
    global user
    while True:
        # --- Menu for Not Logged In User ---
        if not user:
            print(Fore.CYAN + "\n📋 --- TO-DO LIST ---")
            print(Fore.BLUE + "1️⃣  Iniciar sesión")
            print(Fore.BLUE + "2️⃣  Crear cuenta")
            print(Fore.RED + "0️⃣  Salir")
            opcion = input(Fore.YELLOW + "👉 Selecciona una opción (0-2): ")

            if opcion == "1":
                print(Fore.BLUE + "\n➡️  Iniciando sesión...")
                user = loginUser()
            elif opcion == "2":
                print(Fore.BLUE + "\n➕ Creando una nueva cuenta...")
                user = userRegister()
            elif opcion == "0":
                print(Fore.MAGENTA + "\n👋  ¡Hasta luego! ¡Que tengas un buen día! 🌟")
                exit()
            else:
                print(
                    Fore.RED + "⚠️  Opción no válida. Por favor, intenta de nuevo con un número del 0 al 2.")

        # --- Menu for Standard User ---
        elif user and not user.is_admin:
            print(Fore.CYAN + "\n📋 --- MENÚ TO-DO LIST ---")
            print(Fore.GREEN + f"👤 Bienvenido: {user.username}")
            print(Fore.YELLOW + "1️⃣  Crear nueva tarea")
            print(
                Fore.YELLOW + "2️⃣  Actualizar una tarea existente")
            print(Fore.YELLOW + "3️⃣  Eliminar una tarea")
            print(Fore.YELLOW + "4️⃣  Ver tus tareas")
            print(Fore.YELLOW + "5️⃣  Ver tus tareas por titulo")
            print(Fore.YELLOW + "6️⃣  Ver tus tareas por estado")
            print(Fore.YELLOW + "7️⃣  Ver tus tareas por estado y prioridad")
            print(Fore.RED + "8️⃣  🚪 Cerrar sesión")
            print(Fore.RED + "0️⃣  Salir")
            opcion = input(Fore.YELLOW + "👉 Selecciona una opción (0-8): ")

            if opcion == "1":
                print(Fore.BLUE + "\n🆕 Creando una nueva tarea...")
                crear_tarea(user.id)
            elif opcion == "2":
                print(Fore.BLUE + "\n🛠️  Actualizando tarea...")
                actualizar_tarea()
            elif opcion == "3":
                print(Fore.BLUE + "\n🗑️  Eliminando tarea...")
                eliminar_tarea(user.is_admin)
            elif opcion == "4":
                print(Fore.BLUE + "\n🔍  Buscando todas tus tareas...")
                searchAllTasksForUser(user.id)
            elif opcion == "5":
                print(Fore.BLUE + "\n🔍  Buscando tarea por título..." )
                searchTasksForUserTitle(user.id)
            elif opcion == "6":
                print(Fore.BLUE + "\n🔍  Buscando tarea por estado...")
                searchAllTasksForUserStatus(user.id)
            elif opcion == "7":
                print(Fore.BLUE + "\n🔍  Buscando tarea por estado y prioridad...")
                searchAllTasksForUserStatusPriority(user.id)
            elif opcion == "8":
                print(Fore.LIGHTYELLOW_EX + "\n🚪  Cerrando sesión...")
                user = None
            elif opcion == "0":
                print(Fore.MAGENTA + "\n👋  ¡Hasta luego! ¡Que tengas un buen día! 🌟")
                exit()
            else:
                print(
                    Fore.RED + "⚠️  Opción no válida. Por favor, intenta de nuevo con un número del 0 al 8.")

        # --- Menu for Admin User ---
        else:  # user.is_admin is True
            print(Fore.RED + "🛡️ === PANEL DE ADMINISTRACIÓN === 🛡️")
            print(Fore.GREEN + f"Bienvenido, Administrador: {user.username}")
            print(Fore.YELLOW + "1️⃣  Ver todas las tareas")
            print(Fore.YELLOW + "2️⃣  Ver todos los usuarios")
            print(Fore.YELLOW + "3️⃣  Eliminar usuario")
            print(Fore.YELLOW + "4️⃣  Eliminar tarea")
            print(Fore.YELLOW + "5️⃣  Editar usuario")
            print(Fore.RED + "6️⃣  🚪 Cerrar sesión de administrador")
            print(Fore.RED + "0️⃣  Salir de la aplicación")
            opcion = input(Fore.MAGENTA + "👉 Elige una opción: ")

            if opcion == '1':
                print(Fore.BLUE + "\n📋 Mostrando todas las tareas...")
                ver_tareas()
            elif opcion == '2':
                print(Fore.BLUE + "\n👥 Mostrando todos los usuarios...")
                getAllUsers()
            elif opcion == '3':
                print(Fore.BLUE + "\n🗑️ Eliminando usuario...")
                deleteuser()
            elif opcion == '4':
                print(Fore.BLUE + "\n🗑️ Eliminando tarea...")
                eliminar_tarea(user.is_admin)
            elif opcion == '5':
                print(Fore.BLUE + "\n✏️ Editando usuario...")
                editUser()
            elif opcion == '6':
                print(Fore.LIGHTYELLOW_EX + "\n🚪  Cerrando sesión de administrador...")
                user = None
            elif opcion == "0":
                print(Fore.MAGENTA + "\n👋  ¡Hasta luego! ¡Que tengas un buen día! 🌟")
                exit()
            else:
                print(
                    Fore.RED + "⚠️  Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()