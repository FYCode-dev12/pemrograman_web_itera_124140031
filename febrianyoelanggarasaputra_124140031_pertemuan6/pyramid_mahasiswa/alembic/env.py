"""Pyramid bootstrap environment for Alembic."""
from alembic import context
from pyramid.paster import get_appsettings, setup_logging
from sqlalchemy import engine_from_config

from pyramid_mahasiswa.models.meta import Base
from pyramid_mahasiswa.models import Mahasiswa, Matakuliah

config = context.config

setup_logging(config.config_file_name)

settings = get_appsettings(config.config_file_name)
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(url=settings['sqlalchemy.url'])
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    engine = engine_from_config(settings, prefix='sqlalchemy.')

    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata
    )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
