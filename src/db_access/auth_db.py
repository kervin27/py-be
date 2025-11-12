import mysql.connector
from mysql.connector import Error
from db import create_connection  # Assicurati che create_connection ritorni un oggetto connection valido

def get_user_by_username(username: str) -> tuple[bool, dict]:
    conn = create_connection()
    if not conn:
        return False, {}
    
    try:
        cursor = conn.cursor()
        query = "SELECT id, username, email, password FROM auth_users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        print("DEBUG result:", result)
        if result:
            user_data = {"id": result[0], "username": result[1], "email": result[2], "password": result[3]}
            return True, user_data
        return False, {}
    except Error as e:
        print(f"Errore DB: {str(e)}")
        return False, {}
    finally:
        cursor.close()
        conn.close()

def get_user_by_email(email: str) -> tuple[bool, dict]:
    conn = create_connection()
    if not conn:
        return False, {}
    
    try:
        cursor = conn.cursor()
        query = "SELECT id, username, email, password FROM auth_users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if result:
            user_data = {"id": result[0], "username": result[1], "email": result[2], "password": result[3]}
            return True, user_data
        return False, {}
    except Error as e:
        print(f"Errore DB: {str(e)}")
        return False, {}
    finally:
        cursor.close()
        conn.close()

def create_user(username: str, email: str, hashed_password: str) -> tuple[bool, dict | str]:
    conn = create_connection()
    if not conn:
        return False, "Connessione al DB fallita."
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO auth_users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, hashed_password))
        conn.commit()
        user_id = cursor.lastrowid
        return True, {"id": user_id, "message": "Utente creato con successo."}
    except Error as e:
        return False, f"Errore DB durante l'inserimento: {str(e)}"
    finally:
        cursor.close()
        conn.close()
