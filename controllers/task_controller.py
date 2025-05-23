from colorama import init, Fore, Style
from database.db import SessionLocal
from models.task_model import Task
from controllers.task_validators import title_validator, description_validator, user_validator, category_validator, priority_validator, validador_estado_validator, obtener_id, elegir_estado
from views.task_view import mostrar_todas_tareas, mostrar_tarea

init(autoreset=True)

# Crear una sesión de la base de datos
db = SessionLocal()

def crear_tarea():
    titulo = title_validator()
    descripcion = description_validator()
    category = category_validator()
    priority = priority_validator()

    value = False
    nueva_tarea = Task(title=titulo, description=descripcion, status=value, user_id=user_id, category=category, priority=priority)
    db.add(nueva_tarea)
    db.commit()
    print(Fore.GREEN + f"✅ Tarea '{titulo}' creada exitosamente. ¡Bien hecho! 🎉")
    ver_tarea_por_id(nueva_tarea.id)

# def ver_tareas(user_id):
#     try:
#         tareas = db.query(Task).all()
#         mostrar_todas_tareas(tareas)
#     except Exception as err:
#         print(Fore.RED + f"❌ Ha ocurrido un error inesperado al intentar mostrar las tareas: {err}")

def ver_tarea_por_id(id = None):
    if id:
        idTask = id
    else:
        idTask = obtener_id()

    while True:
        task = db.query(Task).get(idTask)
        if task:
            mostrar_tarea(task)
            break
        else:
            print(Fore.RED + "❌ ID no encontrado. Comprueba que la tarea exista.")

def actualizar_tarea():
    id_tarea = obtener_id()
    tarea = db.query(Task).get(id_tarea)
    if tarea:
        
        tarea.title = title_validator(tarea)
        tarea.description = description_validator(tarea)
        tarea.status = validador_estado_validator(tarea)
        tarea.category = category_validator(tarea) 
        tarea.priority = priority_validator(tarea)   
         
        db.commit()
        print(Fore.GREEN + "✅ Tarea actualizada correctamente. ¡Buen trabajo! 🛠️")
        ver_tarea_por_id(id_tarea)
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
            # ver_tareas()
        else:
            print(Fore.RED + "❌ Tarea no encontrada. No se pudo eliminar.")
    except Exception as err:
        print(Fore.RED + f"❌ Ha ocurrido un error inesperado al eliminar la tarea: {err}")

def searchAllTasksForUser(user_id):
    while True:
        try:
            tasks = db.query(Task).filter(Task.user_id == user_id).all()
            mostrar_todas_tareas(tasks)
            return
        except Exception as err:
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado {err}")


def searchAllTasksForUserStatus(user_id):
    while True:
        try:
            tasks = db.query(Task).filter(Task.user_id == user_id).filter(Task.status == elegir_estado()).all()
            mostrar_todas_tareas(tasks)
            return
        except Exception as err:
            print(Fore.RED +  f"❌ Ha ocurrido un error inesperado {err}")

    
def searchAllTasksForUserStatusPriority(user_id):
    while True:
        try:
            tasks = db.query(Task).filter(Task.user_id == user_id).filter(Task.status == elegir_estado()).filter(Task.priority == priority_validator()).all()
            mostrar_todas_tareas(tasks)
            return
        except Exception as err:
            print(Fore.RED + f"❌ Ha ocurrido un error inesperado {err}")

    
