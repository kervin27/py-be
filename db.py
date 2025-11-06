#Gestisce la connessione al database:

# db.py (versione corretta per Railway)

import mysql.connector
import os # <-- Aggiungi questo per leggere le variabili di sistema

def get_db_connection():
    # 1. Leggi le credenziali direttamente dalle variabili d'ambiente di Railway.
    #    Controlla la dashboard di Railway per i nomi esatti delle variabili (es. MYSQL_HOST vs DB_HOST).
    
    DB_HOST = os.environ.get('MYSQLHOST') 
    DB_USER = os.environ.get('MYSQLUSER')
    DB_PASSWORD = os.environ.get('MYSQLPASSWORD')
    DB_NAME = os.environ.get('MYSQLDATABASE')
    DB_PORT = os.environ.get('MYSQLPORT', 3306) # Usa 3306 come default se non specificato

    # 2. Connetti usando i valori letti
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        return conn
    except mysql.connector.Error as err:
        # Questo stamperà l'errore esatto nei log di Railway, aiutando la diagnostica!
        print(f"Errore di connessione al database: {err}") 
        # Rilanciare l'errore è spesso meglio per far capire al container che qualcosa non va
        raise