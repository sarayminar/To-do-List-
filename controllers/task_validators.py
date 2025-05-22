from colorama import Fore


def title_validator():
    while True:
        try:
            titulo = input(Fore.BLUE + "📝 Introduce el título de la tarea: ")
            if not titulo.strip():
                raise ValueError(Fore.RED + "❌ El alias/nombre no puede estar vacío.")
            if titulo.isdigit():
                raise ValueError(Fore.RED + "❌ El título no puede ser un valor numérico.")
            if len(titulo) > 255:
                raise ValueError(Fore.RED + "❌ El título es demasiado largo. (Máx. 255 caracteres).")
            return titulo;
        except ValueError as err:
            print(Fore.RED + f"{err}")
        except Exception as err:
            print(Fore.RED + f"❌ Ocurrió un error inesperado al procesar el título: {err}")