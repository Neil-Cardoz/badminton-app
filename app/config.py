import os

DB_USER = os.getenv('POSTGRES_USER', 'root')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'Weinachten01@')
DB_NAME = os.getenv('POSTGRES_DB', 'mydatabase')
DB_HOST = os.getenv('DB_HOST', 'db')  # docker-compose service name

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

