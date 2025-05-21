from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import os
import sys

# ➡️ Agregar el path del proyecto para que detecte los módulos correctamente
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

# ➡️ Importar Base y el modelo
from database.db import Base
from models.task_model import Task

# ➡️ Configuración de logging
fileConfig(context.config.config_file_name)

# ➡️ Definir los metadatos para las migraciones
target_metadata = Base.metadata

def run_migrations_offline():
    """Ejecuta las migraciones en modo offline."""
    url = context.config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecuta las migraciones en modo online."""
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

# Selección del modo de ejecución
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
