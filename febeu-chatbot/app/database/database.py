import os
from pathlib import Path
import psycopg


def get_connection():
    password_file=Path(__file__).resolve().parents[3] / "secrets/postgres_password.txt"
    try:
        password_string = password_file.read_text().strip()
    except OSError as error:
        raise RuntimeError("Erro ao ler o ficheiro da password") from error
    try:
        connection = psycopg.connect(
            host="postgresql",
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=password_string,
            port=5432
        )
    except psycopg.Error as error:
        raise RuntimeError("Erro ao conectar ao PostgreSQL") from error
    return (connection)