# views/main.py

from colorama import init, Fore, Style
from controllers.task_controller import (
    crear_tarea,
    ver_tareas,
    ver_tarea_por_id,
    actualizar_tarea,
    eliminar_tarea,
    searchAllTasksForUser,
    searchAllTasksForUserStatus,
    searchAllTasksForUserStatusPriority
)

init(autoreset=True)

def menu():
    while True:
        print(Fore.CYAN +  "\n📋 --- MENÚ TO-DO LIST ---")
        print("1️⃣  Crear nueva tarea")
        print("2️⃣  Ver todas las tareas")
        print("3️⃣  Actualizar una tarea existente")
        print("4️⃣  Eliminar una tarea")
        print("5️⃣  Buscar tarea por ID")
        print("6️⃣  Buscar tareas por usuario")
        print("7️⃣  Buscar tareas por usuario y estado")
        print("8️⃣  Buscar tareas por usuario, estado y prioridad")
        print("0️⃣  Salir")

        opcion = input(Fore.YELLOW + "👉 Selecciona una opción (0-8): ")

        if opcion == "1":
            print(Fore.BLUE + "\n🆕 Creando una nueva tarea...")
            crear_tarea()
        elif opcion == "2":
            print(Fore.BLUE + "\n📂 Mostrando todas las tareas...")
            ver_tareas()
        elif opcion == "3":
            print(Fore.BLUE + "\n🛠️  Actualizando tarea...")
            actualizar_tarea()
        elif opcion == "4":
            print(Fore.BLUE + "\n🗑️  Eliminando tarea...")
            eliminar_tarea()
        elif opcion == "5":
            print(Fore.BLUE + "\n🔍  Buscar tarea por ID...")
            ver_tarea_por_id()
        elif opcion == "6":
            searchAllTasksForUser()
        elif opcion == "7":
            searchAllTasksForUserStatus()
        elif opcion == "8":
            searchAllTasksForUserStatusPriority()
        elif opcion == "0":
            print(Fore.MAGENTA + "\n👋  ¡Hasta luego! ¡Que tengas un buen día! 🌟")
            exit()
        else:
            print(Fore.RED + "⚠️  Opción no válida. Por favor, intenta de nuevo con un número del 0 al 8.")

if __name__ == "__main__":
    menu()
