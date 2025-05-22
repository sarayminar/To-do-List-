from colorama import Fore

# Funcion crear_tarea()
def title_validator(tarea = None):
    while True:
        try:
            if tarea :
                titulo = input(Fore.CYAN + f"📝 Nuevo título (anterior: {tarea.title}): ")
            else:
                titulo = input(Fore.BLUE + "📝 Introduce el título de la tarea: ")
            if not titulo.strip():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede estar vacío.")
            if titulo.isdigit():
                raise ValueError(Fore.RED + "❌ El título no puede ser un valor numérico.")
            if len(titulo) > 255:
                raise ValueError(Fore.RED + "❌ El título es demasiado largo. (Máx. 255 caracteres).")
            return titulo 
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar el título: {err}")


def description_validator(tarea = None):
    while True:
        try:
            if tarea:
                descripcion = input(Fore.CYAN + f"🧾 Nueva descripción (anterior: {tarea.description}): ")
            else:
                descripcion = input(Fore.BLUE + "🧾 Introduce la descripción de la tarea (Opcional): ")
            if descripcion.isdigit():
                raise ValueError(Fore.RED + "❌ La descripción no puede ser un valor numérico.")
            if len(descripcion) > 500:
                raise ValueError(Fore.RED + "❌ La descripción es demasiado larga. (Máx. 500 caracteres).")
            return descripcion
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar la descripción: {err}")

def user_validator(bool):
    while True:
        try:
            if bool:
                user = input(Fore.BLUE + "🧾 Introduce tu alias/nombre: ")
            else:
                user = input(Fore.BLUE + "🧾 Introduce el alias/nombre a buscar: ")
            if not user.strip():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede estar vacío.")
            if user.isdigit():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede ser un valor numérico.")
            if len(user) > 50:
                raise ValueError(Fore.RED + "❌ El alias/nombre es demasiado largo. (Máx. 50 caracteres).")
            return user
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar el alias/nombre: {err}")

def category_validator(tarea = None):
    while True:
        try:
            if tarea:
                category = input(f"Nueva categoria (anterior: {tarea.category}): ")
            else:
                category = input(Fore.BLUE + "🧾 Introduce una categoria (opcional): ")
            if category.isdigit():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede ser un valor numérico.")
            if len(category) > 25:
                raise ValueError(Fore.RED + "❌ La categoria es demasiado larga. (Máx. 25 caracteres).")
            return category
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar la categoria: {err}")

def priority_validator(tarea = None):
    while True:
        try:
            if tarea:
                priority = input(f"Nueva prioridad (anterior: {tarea.category}): ")
            else:
                priority = input(Fore.BLUE + "🧾 Introduce la prioridad: ")
            if not priority.strip():
                raise ValueError(Fore.RED + "❌ La prioridad no puede estar vacía.")
            if priority.isdigit():
                raise ValueError(Fore.RED + "❌ La prioridad no puede ser un valor numérico.")
            if len(priority) > 25:
                raise ValueError(Fore.RED + "❌ La prioridad es demasiado larga. (Máx. 25 caracteres).")
            return priority
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar la prioridad: {err}")


def validador_estado_validator(tarea = None):
    while True:
            try:
                status = not tarea.status if input(
                    "Introduzca algo para cambiar el estado de la tarea: ") else tarea.status
                return status
            except Exception as e:
                print(Fore.RED + f"❌ Ocurrió un error inesperado al cambiar el estado: {e}")


def obtener_id(bool = None):
    id_tarea_str = input(Fore.CYAN + "✏️ Introduce el ID de la tarea: ")
    try:
        id_tarea = int(id_tarea_str)
        return id_tarea
    except ValueError:
        print(Fore.RED + "❗ ID inválido. Por favor, introduce un número.")
        return
    
def elegir_estado():
    try:
        status = input("Introduzca el estado que se busca: ").lower()
        if status == "completada":
            return True
        elif status == "no completada": 
            return False
        else:
            raise ValueError(f"Valor no válido de estado")
    except ValueError as err:
        print(err)
    except Exception as err:
        print(f"Error no controlado {err}")