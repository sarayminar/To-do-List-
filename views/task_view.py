
from colorama import init, Fore, Style
import os

init(autoreset=True)

def mostrar_todas_tareas(tareas):
    if tareas:
            print(Fore.CYAN + "📋 Lista de tareas registradas:")
            for tarea in tareas:
                estado = Fore.GREEN +  "✅ Completada" if tarea.status else Fore.RED + "❌ No completada"
                cat = tarea.category if tarea.category else Fore.RED + "Sin categoria";
                print(Fore.CYAN + f"🆔 {tarea.id} - {tarea.title} - Usuario: {tarea.user}: descripcion: {tarea.description}, categoria: [{cat}], prioridad: {tarea.priority}, fecha de creación [{tarea.createDate.strftime("%Y-%m-%d %H:%M:%S")}], fecha de edición [{tarea.lastEditDate.strftime("%Y-%m-%d %H:%M:%S")}], [{estado}].")
    else:
        print(Fore.YELLOW + "📭 No hay tareas registradas.")

def mostrar_tarea(task):
    estado = Fore.GREEN + "✅ Completada" if task.status else Fore.RED + "❌ No completada"
    cat = task.category if task.category else Fore.RED + "Sin categoria";
    print(Fore.CYAN + f"🆔 {task.id} - {task.title} - Usuario: {task.user}: descripcion: {task.description}, categoria: [{cat}], prioridad: {task.priority}, fecha de creación [{task.createDate.strftime("%Y-%m-%d %H:%M:%S")}], fecha de edición [{task.lastEditDate.strftime("%Y-%m-%d %H:%M:%S")}], [{estado}].")
    
def limpiar_pantalla():
    os.system ('cls' if os.name == 'nt' else 'clear')