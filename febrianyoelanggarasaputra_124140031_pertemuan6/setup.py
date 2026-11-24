import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'alembic',
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2-binary',
]

setup(
    name='pyramid_mahasiswa',
    version='0.0',
    description='pyramid_mahasiswa RESTful API',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Febrian Yoel Anggara Saputra',
    author_email='febrian.124140031@student.itera.ac.id',
    url='',
    keywords='web pyramid pylons rest api',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = pyramid_mahasiswa:main',
        ],
        'console_scripts': [
            'initialize_pyramid_mahasiswa_db = pyramid_mahasiswa.scripts.initialize_db:main',
        ],
    },
)
