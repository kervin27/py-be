import os  # importa il modulo os per leggere variabili d'ambiente
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

ENV = os.getenv("ENV", "local")  # default "local"

if ENV == "production":
    DB_HOST = os.getenv("MYSQLHOST")
    DB_USER = os.getenv("MYSQLUSER")
    DB_PASSWORD = os.getenv("MYSQLPASSWORD")
    DB_NAME = os.getenv("MYSQLDATABASE")
    DB_PORT = int(os.getenv("MYSQLPORT", 3306))
else:  # locale
    DB_HOST = os.getenv("LOCAL_DB_HOST", "127.0.0.1")
    DB_USER = os.getenv("LOCAL_DB_USER", "habado_user")
    DB_PASSWORD = os.getenv("LOCAL_DB_PASSWORD", "root")
    DB_NAME = os.getenv("LOCAL_DB_NAME", "habado_local_db")
    DB_PORT = int(os.getenv("LOCAL_DB_PORT", 3307))
