from logging.config import fileConfig

from sqlalchemy import pool

from alembic import context

from app.database.base import Base

from app.database.connection import DATABASE_URL

import app.models

from app.models.evolution_memory import EvolutionMemory

from app.models.memory_system_state import MemorySystemState



# Alembic Config
config = context.config



# Use application database configuration
config.set_main_option(

    "sqlalchemy.url",

    DATABASE_URL

)



# Logging
if config.config_file_name is not None:

    fileConfig(

        config.config_file_name

    )



# Metadata

target_metadata = Base.metadata





def run_migrations_offline() -> None:

    """
    Run migrations in offline mode.
    """


    url = config.get_main_option(

        "sqlalchemy.url"

    )


    context.configure(

        url=url,

        target_metadata=target_metadata,

        literal_binds=True,

        dialect_opts={

            "paramstyle": "named"

        },

    )


    with context.begin_transaction():

        context.run_migrations()





def run_migrations_online() -> None:

    """
    Run migrations in online mode.
    """


    from sqlalchemy import create_engine


    connectable = create_engine(

        DATABASE_URL,

        poolclass=pool.NullPool

    )


    with connectable.connect() as connection:


        context.configure(

            connection=connection,

            target_metadata=target_metadata

        )


        with context.begin_transaction():

            context.run_migrations()





if context.is_offline_mode():

    run_migrations_offline()

else:

    run_migrations_online()