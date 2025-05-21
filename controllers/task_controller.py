from colorama import init, Fore, Style
from database.db import SessionLocal
from models.task_model import Task

init(autoreset=True)

# Crear una sesión de la base de datos
db = SessionLocal()

def crear_tarea():
    while True:
        try:
            titulo = input(Fore.BLUE + "📝 Introduce el título de la tarea: ")
            if len(titulo) > 255:
                raise ValueError(Fore.RED + "❌ El título es demasiado largo. (Máx. 255 caracteres).")
            if not titulo.strip():
                raise ValueError(Fore.RED + "❌ El título no puede estar vacío.")
            break
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar el título: {err}")
    
    while True:
        try:
            descripcion = input(Fore.BLUE + "🧾 Introduce la descripción de la tarea: ")
            if len(descripcion) > 500:
                raise ValueError(Fore.RED + "❌ La descripción es demasiado larga. (Máx. 500 caracteres).")
            break
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar la descripción: {err}")
    value = False
    nueva_tarea = Task(title=titulo, description=descripcion, status = value)
    db.add(nueva_tarea)
    db.commit()
    print(Fore.GREEN + f"✅ Tarea '{titulo}' creada exitosamente. ¡Bien hecho! 🎉")

def ver_tareas():
    try:
        tareas = db.query(Task).all()
        if tareas:
            print(Fore.CYAN + "📋 Lista de tareas registradas:")
            for tarea in tareas:
                estado = "✅ Completada" if tarea.status else "❌ No completada"
                print(f"{tarea.id} - {tarea.title}: {tarea.description} [{estado}]")
        else:
            print(Fore.YELLOW + "📭 No hay tareas registradas.")
    except Exception as err:
        print(Fore.RED + f"❌ Ha ocurrido un error inesperado al intentar mostrar las tareas: {err}")
        
def ver_tarea_por_id(id):
    if id:
        idTask = id
    else:
        idTask = obtener_id()
    while True:
        idTask = obtener_id()
        task = db.query(Task).get(idTask)
        if task:
            estado = Fore.GREEN + "✅ Completada" if task.status else Fore.RED + "❌ No completada"
            print(Fore.CYAN + f"🆔 {task.id} -  {task.title}: {task.description} [{estado}]")
            return
        else:
            print(Fore.RED + "❌ ID no encontrado. Comprueba que la tarea exista.")

def actualizar_tarea():
    id_tarea = obtener_id()
    tarea = db.query(Task).get(id_tarea)
    if tarea:
        while True:
            try:
                nuevo_titulo = input(Fore.CYAN + f"📝 Nuevo título (anterior: {tarea.title}): ")
                if nuevo_titulo:  
                    if len(nuevo_titulo) > 255:
                        raise ValueError(Fore.RED + "❌ El título es demasiado largo. (Máx. 255 caracteres).")
                    if not nuevo_titulo.strip():
                        raise ValueError(Fore.RED + "❌ El título no puede estar vacío.")
                    tarea.title = nuevo_titulo
                break  
            except ValueError as err:
                print(Fore.RED + f"{err}")
            except Exception as err:
                print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar el título: {err}")

        while True:
            try:
                nueva_descripcion = input(Fore.CYAN + f"🧾 Nueva descripción (anterior: {tarea.description}): ")
                if nueva_descripcion:  
                    if len(nueva_descripcion) > 500:
                        raise ValueError(Fore.RED + "❌ La descripción es demasiado larga. (Máx. 500 caracteres).")
                    tarea.description = nueva_descripcion
                break
            except ValueError as err:
                print(Fore.RED + f"{err}")
            except Exception as err:
                print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar la descripción: {err}")
        while True:
            try:
                tarea.status = not tarea.status if input("Introduzca algo para cambiar el estado de la tarea: ") else tarea.status
            except Exception as e:
                print(Fore.RED + f"❌ Ocurrió un error inesperado al cambiar el estado: {e}")    
            db.commit()
            print(Fore.GREEN + "✅ Tarea actualizada correctamente. ¡Buen trabajo! 🛠️")
            return
    else:
        print(Fore.RED + "❌ Tarea no encontrada. No se pudo actualizar.")

def eliminar_tarea():
    try:
        id_tarea = obtener_id()
        tarea = db.query(Task).get(id_tarea)
        if tarea:
            db.delete(tarea)
            db.commit()
            print(Fore.GREEN + f"🗑️ Tarea '{tarea.title}' eliminada correctamente.")
            ver_tareas()
        else:
            print(Fore.RED + "❌ Tarea no encontrada. No se pudo eliminar.")
    except Exception as err:
        print(Fore.RED + f"❌ Ha ocurrido un error inesperado al eliminar la tarea: {err}")

def obtener_id():
    id_tarea_str = input(Fore.CYAN + "✏️ Introduce el ID de la tarea: " + Style.RESET_ALL)
    try:
        id_tarea = int(id_tarea_str)
        return id_tarea
    except ValueError:
        print(Fore.RED + "❗ ID inválido. Por favor, introduce un número." + Style.RESET_ALL)
        return