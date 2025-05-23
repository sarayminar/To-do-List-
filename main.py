# views/main.py

from colorama import init, Fore, Style
from controllers.task_controller import (
    crear_tarea,
    ver_tarea_por_id,
    actualizar_tarea,
    eliminar_tarea,
    searchAllTasksForUser,
    searchAllTasksForUserStatus,
    searchAllTasksForUserStatusPriority
)
from controllers.user_controller import loginUser, userRegister
from models.users_model import User
from models.task_model import Task


init(autoreset=True)

user = None

def menu():
    global user
    while True:
        if user:
            print(Fore.CYAN +  "\n📋 --- MENÚ TO-DO LIST ---")
            print("1️⃣  Crear nueva tarea")
            print("2️⃣  Ver todas las tareas")
            print("2️⃣  Actualizar una tarea existente")
            print("3️⃣  Eliminar una tarea")
            print("4️⃣  Buscar tarea por ID")
            print("5️⃣  Buscar tareas por usuario")
            print("6️⃣  Buscar tareas por usuario y estado")
            print("7️⃣  Buscar tareas por usuario, estado y prioridad")
            print("8️⃣  Cerrar sesión")
            print("0️⃣  Salir")

            opcion = input(Fore.YELLOW + "👉 Selecciona una opción (0-8): ")

            if opcion == "1":
                print(Fore.BLUE + "\n🆕 Creando una nueva tarea...")
                crear_tarea(user.id)
        # elif opcion == "10":
        #     print(Fore.BLUE + "\n📂 Mostrando todas las tareas...")
        #     ver_tareas()
            elif opcion == "2":
                print(Fore.BLUE + "\n🛠️  Actualizando tarea...")
                actualizar_tarea()
            elif opcion == "3":
                print(Fore.BLUE + "\n🗑️  Eliminando tarea...")
                eliminar_tarea()
            elif opcion == "4":
                print(Fore.BLUE + "\n🔍  Buscar tarea por ID...")
                ver_tarea_por_id()
            elif opcion == "5":
                searchAllTasksForUser(user.id)
            elif opcion == "6":
                searchAllTasksForUserStatus(user.id)
            elif opcion == "7":
                searchAllTasksForUserStatusPriority(user.id)
            elif opcion == "0":
                print(Fore.MAGENTA + "\n👋  ¡Hasta luego! ¡Que tengas un buen día! 🌟")
                exit()
            elif opcion == "8":
                user = None
            
        else:
            print(Fore.CYAN +  "\n📋 --- MENÚ TO-DO LIST ---")
            print("1️⃣  Iniciar sesión")
            print("2️⃣  Crear cuenta")
            print("0️⃣  Salir")
        
            opcion = input(Fore.YELLOW + "👉 Selecciona una opción (0-2): ")

            if opcion == "1":
                print(Fore.BLUE + "\n🆕 Creando una nueva tarea...")
                user = loginUser()
            elif opcion == "2":
                print(Fore.BLUE + "\n📂 Mostrando todas las tareas...")
                user = userRegister()
            elif opcion == "0":
                print(Fore.MAGENTA + "\n👋  ¡Hasta luego! ¡Que tengas un buen día! 🌟")
                exit()
            else:
                print(Fore.RED + "⚠️  Opción no válida. Por favor, intenta de nuevo con un número del 0 al 2.")



if __name__ == "__main__":
    menu()