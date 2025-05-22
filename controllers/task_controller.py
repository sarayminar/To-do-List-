from datetime import datetime

from colorama import init, Fore, Style
from database.db import SessionLocal
from models.task_model import Task
from controllers.task_validators import title_validator

init(autoreset=True)

# Crear una sesión de la base de datos
db = SessionLocal()

def crear_tarea():

    titulo = title_validator();

    while True:
        try:
            descripcion = input(Fore.BLUE + "🧾 Introduce la descripción de la tarea (Opcional): ")
            if descripcion.isdigit():
                raise ValueError(Fore.RED + "❌ La descripción no puede ser un valor numérico.")
            if len(descripcion) > 500:
                raise ValueError(Fore.RED + "❌ La descripción es demasiado larga. (Máx. 500 caracteres).")
            break
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar la descripción: {err}")

    while True:
        try:
            user = input(Fore.BLUE + "🧾 Introduce tu alias/nombre: ")
            if not user.strip():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede estar vacío.")
            if user.isdigit():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede ser un valor numérico.")
            if len(descripcion) > 50:
                raise ValueError(Fore.RED + "❌ El alias/nombre es demasiado largo. (Máx. 50 caracteres).")
            break
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar el alias/nombre: {err}")

    while True:
        try:
            category = input(Fore.BLUE + "🧾 Introduce una categoria (opcional): ")
            if category.isdigit():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede ser un valor numérico.");
            if len(category) > 25:
                raise ValueError(Fore.RED + "❌ La categoria es demasiado larga. (Máx. 25 caracteres).");
            break
        except ValueError as err:
            print(Fore.RED + f"{err}");
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar la categoria: {err}");

    while True:
        try:
            priority = input(Fore.BLUE + "🧾 Introduce la prioridad: ")
            if not priority.strip():
                raise ValueError(Fore.RED + "❌ La prioridad no puede estar vacía.")
            if priority.isdigit():
                raise ValueError(Fore.RED + "❌ La prioridad no puede ser un valor numérico.");
            if len(priority) > 25:
                raise ValueError(Fore.RED + "❌ La prioridad es demasiado larga. (Máx. 25 caracteres).");
            break
        except ValueError as err:
            print(Fore.RED + f"{err}");
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar la prioridad: {err}");

    value = False
    nueva_tarea = Task(title=titulo, description=descripcion, status=value, user=user, category=category, priority=priority);
    db.add(nueva_tarea)
    db.commit()
    print(Fore.GREEN + f"✅ Tarea '{titulo}' creada exitosamente. ¡Bien hecho! 🎉")
    ver_tarea_por_id(nueva_tarea.id);

def ver_tareas():
    try:
        tareas = db.query(Task).all()
        if tareas:
            print(Fore.CYAN + "📋 Lista de tareas registradas:")
            for tarea in tareas:
                estado = "✅ Completada" if tarea.status else "❌ No completada"
                cat = tarea.category if tarea.category else Fore.RED + "Sin categoria";
                print(Fore.CYAN + f"🆔 {tarea.id} - {tarea.title} - Usuario: {tarea.user}: descripcion: {tarea.description}, [{estado}], categoria: [{cat}] prioridad: {tarea.priority}.")
        else:
            print(Fore.YELLOW + "📭 No hay tareas registradas.")
    except Exception as err:
        print(Fore.RED + f"❌ Ha ocurrido un error inesperado al intentar mostrar las tareas: {err}")

def ver_tarea_por_id(id):
    if id:
        idTask = id;
    else:
        idTask = obtener_id()

    while True:
        task = db.query(Task).get(idTask)
        if task:
            estado = Fore.GREEN + "✅ Completada" if task.status else Fore.RED + "❌ No completada"
            cat = task.category if task.category else Fore.RED + "Sin categoria";
            print(Fore.CYAN + f"🆔 {task.id} - {task.title} - Usuario: {task.user}: descripcion: {task.description}, [{estado}], categoria: [{cat}] prioridad: {task.priority}.")
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
                    if not nuevo_titulo.strip():
                        raise ValueError(Fore.RED + "❌ El título no puede estar vacío.")
                    if len(nuevo_titulo) > 255:
                        raise ValueError(Fore.RED + "❌ El título es demasiado largo. (Máx. 255 caracteres).")
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
                tarea.status = not tarea.status if input(
                    "Introduzca algo para cambiar el estado de la tarea: ") else tarea.status
            except Exception as e:
                print(Fore.RED + f"❌ Ocurrió un error inesperado al cambiar el estado: {e}")

        while True:
            try:
                newCategory = input(f"Nueva categoria (anterior: {tarea.category}): ")
                if newCategory:
                    if len(newCategory) > 25:
                        raise ValueError(Fore.RED + "❌ La categoria es demasiado larga. (Máx. 25 caracteres).")
                    tarea.category = newCategory;
                    break;
            except ValueError as err:
                print(Fore.RED + f"{err}")
            except Exception as err:
                print(Fore.RED + f"❌ Ocurrió un error inesperado al cambiar la categoria: {err}");

            while True:
                try:
                    newPriority = input(f"Nueva prioridad (anterior: {tarea.category}): ")
                    if newPriority:
                        if not newPriority.strip():
                            raise ValueError(Fore.RED + "❌ La prioridad no puede estar vacía.")
                        if len(newPriority) > 25:
                            raise ValueError(Fore.RED + "❌ La prioridad es demasiado larga. (Máx. 25 caracteres).")
                        tarea.priority = newPriority;
                        break;
                except ValueError as err:
                    print(Fore.RED + f"{err}")
                except Exception as err:
                    print(Fore.RED + f"❌ Ocurrió un error inesperado al cambiar la prioridad: {err}");
            db.commit()
            print(Fore.GREEN + "✅ Tarea actualizada correctamente. ¡Buen trabajo! 🛠️")
            ver_tarea_por_id(id_tarea);
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

"""def searchAllTasksForUser():
    while True:
        try:
            userSearch = input(Fore.BLUE + "🧾 Introduce el alias/nombre por el que quieras buscar: ")
            if not userSearch.strip():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede estar vacío.")
            if userSearch.isdigit():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede ser un valor numérico.")
            if len(userSearch) > 50:
                raise ValueError(Fore.RED + "❌ El alias/nombre es demasiado largo. (Máx. 50 caracteres).")
            break
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar el alias/nombre: {err}")
    tasks = db.query(Task).filter(Task.user.ilike(userSearch)).all();"""