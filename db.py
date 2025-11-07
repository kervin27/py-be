import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

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
        print("❌ Errore connessione DB:", e)
        return None

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

def aggiorna_utente(user_id, nome, email):
    conn = create_connection()
    if not conn:
        return False, "Connessione al DB fallita"
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE utenti SET nome=%s, email=%s WHERE id=%s", (nome, email, user_id))
        conn.commit()
        return True, "Utente aggiornato!"
    except Error as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()

def elimina_utente(user_id):
    conn = create_connection()
    if not conn:
        return False, "Connessione al DB fallita"
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM utenti WHERE id=%s", (user_id,))
        conn.commit()
        return True, "Utente eliminato!"
    except Error as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()
