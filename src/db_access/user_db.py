# src/data_access/user_repository.py (o user_db.py)



from binascii import Error
from db import create_connection


def get_all_users_from_db():
    """Esegue la SELECT e restituisce le tuple grezze dal DB."""
    conn = create_connection()
    if not conn:
        # Se la connessione fallisce, solleva un'eccezione
        # o, per semplicità, ritorna una lista vuota come nel tuo codice originale
        return []

    try:
        cursor = conn.cursor()
        # La query SQL rimane qui
        cursor.execute("SELECT id, username, email FROM utenti")
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Errore durante la lettura dal DB: {e}")
        return []
    finally:
        if conn:
            cursor.close()
            conn.close()

def add_user(username: str, email: str, password: str) -> tuple[bool, str]:
    """Esegue l'INSERT diretto nel DB e gestisce gli errori a livello di DB."""
    
    conn = create_connection()
    if not conn:
        # Il Repository segnala che non è riuscito a connettersi.
        return False, "Connessione al DB fallita."

    cursor = conn.cursor()
    try:
        # La logica di INSERT rimane qui, con l'uso di parametri (%s)
        query = "INSERT INTO utenti (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
        conn.commit()
        
        return True, "Utente creato con successo nel database."
        
    except Error as e:
        # Cattura errori specifici del DB (es. email duplicata, errore di sintassi)
        return False, f"Errore DB durante l'inserimento: {str(e)}"
    finally:
        if conn:
            cursor.close()
            conn.close()


def update_user(user_id: int, updates: dict) -> tuple[bool, str]:
    """Esegue l'UPDATE nel DB con i campi forniti nel dizionario 'updates'."""
    
    conn = create_connection()
    if not conn:
        return False, "Connessione al DB fallita."

    if not updates:
        # Nessun campo da aggiornare, ritorno successo senza query
        return True, "Nessun campo fornito per l'aggiornamento."

    # 1. Costruisce dinamicamente la query SET
    set_clauses = [f"{key}=%s" for key in updates.keys()]
    set_query = ", ".join(set_clauses)
    
    # 2. Definisce la query completa
    query = f"UPDATE utenti SET {set_query} WHERE id=%s"
    
    # 3. Definisce i parametri: i valori degli aggiornamenti + l'ID
    params = list(updates.values())
    params.append(user_id) # L'ID va alla fine per la clausola WHERE

    cursor = conn.cursor()
    try:
        cursor.execute(query, tuple(params))
        conn.commit()
        
        # Opzionale: Controlla se una riga è stata effettivamente modificata
        if cursor.rowcount == 0:
            return False, "Nessun utente trovato con questo ID, o nessun dato è cambiato."
        
        return True, "Utente aggiornato nel database."
        
    except Error as e:
        return False, f"Errore DB durante l'aggiornamento: {str(e)}"
    finally:
        if conn:
            cursor.close()
            conn.close()
            
def delete_user(user_id: int) -> tuple[bool, str]:
    """Esegue l'istruzione DELETE nel DB per l'utente specificato dall'ID."""
    
    conn = create_connection()
    if not conn:
        return False, "Connessione al DB fallita."

    cursor = conn.cursor()
    try:
        # La logica SQL (DELETE) rimane qui.
        query = "DELETE FROM utenti WHERE id=%s"
        cursor.execute(query, (user_id,))
        conn.commit()
        
        # Controlla se una riga è stata effettivamente eliminata
        if cursor.rowcount == 0:
            return False, f"Nessun utente trovato con ID: {user_id}."
            
        return True, "Utente eliminato dal database."
        
    except Error as e:
        # Cattura errori specifici del DB (es. chiavi esterne se fosse più complesso)
        return False, f"Errore DB durante l'eliminazione: {str(e)}"
    finally:
        if conn:
            cursor.close()
            conn.close()