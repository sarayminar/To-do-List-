# 📋 To-do-List- CLI Application

![Python Version](https://img.shields.io/badge/Python-3.13.3-blue)
![Database](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)
![Type](https://img.shields.io/badge/Type-CLI-green)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## 📝 Descripción del Proyecto

`To-do-List-` es una aplicación de gestión de tareas basada en la línea de comandos (CLI) que permite a los usuarios gestionar sus listas de tareas de manera eficiente. La aplicación soporta roles de usuario y administrador, ofreciendo funcionalidades específicas para cada tipo de cuenta. Utiliza PostgreSQL como base de datos, SQLAlchemy como ORM y `alembic` para la gestión de migraciones.

## ✨ Características

### Funcionalidades Generales
* **Sistema de Autenticación:** Registro y inicio de sesión para usuarios.
* **Control de Acceso por Roles:** Distinción entre usuarios normales y administradores con menús y permisos específicos.
* **Interfaz de Consola Interactiva:** Navegación y operación a través de comandos de texto en la terminal.
* **Salida con Colores:** Utiliza `colorama` para una experiencia de usuario más visual y legible en la terminal.

### Funcionalidades para Usuarios Normales (No Administradores)
* **Crear tareas:** Añadir nuevas tareas a su lista personal.
* **Actualizar tareas:** Modificar los detalles de tareas existentes.
* **Eliminar tareas:** Borrar tareas de su lista.
* **Ver tareas:**
    * Ver todas sus tareas.
    * Filtrar y ver tareas por título.
    * Filtrar y ver tareas por estado (completadas/pendientes).
    * Filtrar y ver tareas por estado y prioridad.
* **Cerrar sesión:** Salir de la cuenta actual.
* **Salir de la aplicación:** Terminar la ejecución del programa.

### Funcionalidades para Administradores
* **Ver todas las tareas:** Acceso a todas las tareas de todos los usuarios del sistema.
* **Ver todos los usuarios:** Listar todos los usuarios registrados en la aplicación.
* **Eliminar usuarios:** Borrar cuentas de usuario del sistema.
* **Eliminar tareas:** Borrar cualquier tarea del sistema.
* **Editar usuarios:** Modificar datos de usuarios existentes (nombre de usuario, contraseña).
* **Cerrar sesión de administrador:** Salir de la sesión de administrador.
* **Salir de la aplicación:** Terminar la ejecución del programa.

## 🛠️ Tecnologías Utilizadas

* **Python**: `3.13.3`
* **PostgreSQL**: Base de datos relacional.
* **SQLAlchemy**: ORM (Object-Relational Mapper) para interactuar con la base de datos.
* **Alembic**: Herramienta de migraciones de base de datos para SQLAlchemy.
* **pg8000**: Driver de PostgreSQL para Python.
* **colorama**: Para añadir colores y estilos a la salida de la terminal.
* **bcrypt**: Para el hash seguro de contraseñas.
* **getpass / msvcrt.getch**: Para ocultar la entrada de contraseñas en la terminal.

## 🚀 Instalación y Configuración

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### Prerrequisitos

* **Python 3.13.3** (versión compatible o superior).
* **PostgreSQL**: Asegúrate de tener un servidor PostgreSQL instalado y en ejecución.

### 1. Clonar el Repositorio (si aplica)

Si el proyecto está en un repositorio Git:
```bash
git clone <URL_DEL_REPOSITORIO>
cd To-do-List- # O el nombre de tu directorio raíz del proyecto

## 2. Configurar el Entorno Virtual

Es altamente recomendable usar un entorno virtual para gestionar las dependencias del proyecto.

### Bash

```bash
python -m venv venv
```

**Activar el entorno virtual**

- En Windows:
```bash
.env\Scriptsctivate
```

- En macOS/Linux:
```bash
source venv/bin/activate
```

---

## 3. Instalar Dependencias

Con el entorno virtual activado, instala las librerías necesarias usando pip:

### Bash

```bash
pip install -r requirements.txt
```

Si no tienes el `requirements.txt` o prefieres instalarlas manualmente:

```bash
pip install sqlalchemy>=2.0 alembic>=1.12 pg8000>=1.29 colorama>=0.4.6 bcrypt>=4.3.0
```

---

## 4. Configurar la Base de Datos

### Crear la Base de Datos en PostgreSQL

Asegúrate de tener una base de datos creada en tu servidor PostgreSQL (ej. `todo_db`).

### SQL

```sql
CREATE DATABASE todo_db;
```

### Configurar la Conexión a la DB

Dentro de tu código (probablemente en `database.py` o similar), asegúrate de que la cadena de conexión a tu base de datos PostgreSQL esté correctamente configurada. Por ejemplo:

### Python

```python
DATABASE_URL = "postgresql+pg8000://user:password@host:port/todo_db"
# Asegúrate de reemplazar 'user', 'password', 'host', 'port' con tus credenciales.
# Considera usar variables de entorno para las credenciales en producción.
```

### Ejecutar Migraciones con Alembic

Navega a la raíz de tu proyecto (donde debería estar `alembic.ini`) y ejecuta los siguientes comandos para crear las tablas de la base de datos:

### Bash

```bash
alembic revision --autogenerate -m "create tasks and users table"
alembic upgrade head
```

Esto creará las tablas `users` y `tasks` en tu base de datos.

---

## 5. Crear un Usuario Administrador Inicial

Para poder acceder al panel de administración, necesitarás un usuario con permisos de administrador. Puedes crearlo directamente en la base de datos usando una herramienta como pgAdmin o la CLI de `psql`.

Abre una sesión de Python interactiva en la raíz de tu proyecto con tu entorno virtual activado:

### Bash

```bash
python
```

Genera un hash para la contraseña de tu administrador usando tu función `hashPassword`:

### Python

```python
from utils.security import hashPassword # Ajusta la ruta si es diferente

admin_password = "TuContraseñaAdminSegura" # <-- ELIGE UNA CONTRASEÑA FUERTE
hashed_admin_password = hashPassword(admin_password)
print(hashed_admin_password)
```

Copia la cadena que se imprime (será algo como `b'$2b$12$...'`). Recuerda eliminar la `b'` inicial si aparece al copiar.

Inserta el usuario administrador en tu base de datos usando la siguiente sentencia SQL en pgAdmin o `psql`:

### SQL

```sql
INSERT INTO users (username, password_hash, is_admin, "createDate")
VALUES (
	'admin', -- Puedes elegir otro nombre de usuario, si quieres
	'PEGAR_AQUI_LA_CONTRASEÑA_HASHADA', -- <-- ¡Pega la hash que copiaste aquí, sin la 'b'!
	TRUE,
	NOW()
);
```

---

## 🚀 Uso de la Aplicación

- Asegúrate de que tu entorno virtual esté activado.
- Asegúrate de que tu servidor PostgreSQL esté en ejecución.
- Ejecuta el script principal:

### Bash

```bash
python main.py
```

La aplicación te presentará un menú de inicio donde podrás registrarte, iniciar sesión o salir. Una vez que inicies sesión como usuario normal o administrador, se te mostrarán las opciones de menú correspondientes a tu rol.

**¡Disfruta gestionando tus tareas con To-do-List-!**