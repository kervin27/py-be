import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

# -----------------------------
# Connessione al database
# -----------------------------
def create_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        return conn
    except Error as e:
        print("Errore durante la connessione al DB:", e)
        return None

# -----------------------------
# Creazione tabella utenti
# -----------------------------
def create_table():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS utenti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()

# -----------------------------
# Funzioni CRUD
# -----------------------------
def aggiungi_utente(nome, email):
    conn = create_connection()
    if not conn:
        return False, "Connessione al DB fallita"
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO utenti (nome, email) VALUES (%s, %s)", (nome, email))
        conn.commit()
        return True, "Utente aggiunto!"
    except Error as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()

def leggi_utenti():
    conn = create_connection()
    if not conn:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utenti")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
