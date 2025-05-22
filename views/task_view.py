
from colorama import init, Fore, Style


def mostrar_todas_tareas(tareas):
    if tareas:
            print(Fore.CYAN + "📋 Lista de tareas registradas:")
            for tarea in tareas:
                estado = "✅ Completada" if tarea.status else "❌ No completada"
                cat = tarea.category if tarea.category else Fore.RED + "Sin categoria";
                print(Fore.CYAN + f"🆔 {tarea.id} - {tarea.title} - Usuario: {tarea.user}: descripcion: {tarea.description}, [{estado}], categoria: [{cat}] prioridad: {tarea.priority}.")
    else:
        print(Fore.YELLOW + "📭 No hay tareas registradas.")

def mostrar_tarea(task):
    estado = Fore.GREEN + "✅ Completada" if task.status else Fore.RED + "❌ No completada"
    cat = task.category if task.category else Fore.RED + "Sin categoria";
    print(Fore.CYAN + f"🆔 {task.id} - {task.title} - Usuario: {task.user}: descripcion: {task.description}, [{estado}], categoria: [{cat}] prioridad: {task.priority}.")
    