import mysql.connector  # importa il connettore MySQL per Python
from mysql.connector import Error  # importa l'eccezione Error dal connettore
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT  # importa le variabili di configurazione DB

def create_connection():  # definisce funzione per creare la connessione al DB
    try:  # avvia blocco try per gestire errori di connessione
        conn = mysql.connector.connect(  # crea la connessione al DB con i parametri forniti
            host=DB_HOST,  # host del DB
            user=DB_USER,  # utente DB
            password=DB_PASSWORD,  # password DB
            database=DB_NAME,  # nome del database
            port=DB_PORT  # porta del DB
        )  # fine creazione connessione
        return conn  # ritorna l'oggetto connessione se riuscito
    except Error as e:  # cattura eccezioni di tipo Error
        print("❌ Errore connessione DB:", e)  # stampa un messaggio di errore sulla console
        return None  # ritorna None se la connessione fallisce

def create_table():  # definisce funzione per creare la tabella se non esiste
    conn = create_connection()  # crea o ottiene la connessione al DB
    if conn:  # controlla che la connessione sia valida
        cursor = conn.cursor()  # crea un cursore per eseguire comandi SQL
        cursor.execute("CREATE TABLE IF NOT EXISTS utenti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL UNIQUE);")  # esegue comando SQL per creare la tabella utenti se non esiste
        conn.commit()  # applica le modifiche al DB
        cursor.close()  # chiude il cursore
        conn.close()  # chiude la connessione

def aggiungi_utente(nome, email):  # funzione per inserire un nuovo utente
    conn = create_connection()  # apre la connessione al DB
    if not conn:  # verifica se la connessione è fallita
        return False, "Connessione al DB fallita"  # ritorna errore se connessione non valida
    cursor = conn.cursor()  # crea un cursore per eseguire l'INSERT
    try:  # blocco try per gestire errori durante l'INSERT
        cursor.execute("INSERT INTO utenti (nome, email) VALUES (%s, %s)", (nome, email))  # esegue l'INSERT con parametri per evitare SQL injection
        conn.commit()  # applica la transazione
        return True, "Utente aggiunto!"  # ritorna successo e messaggio
    except Error as e:  # cattura errori di tipo Error
        return False, str(e)  # ritorna False e il messaggio di errore
    finally:  # sempre eseguito per pulire risorse
        cursor.close()  # chiude il cursore
        conn.close()  # chiude la connessione

def leggi_utenti():  # funzione per leggere tutti gli utenti
    conn = create_connection()  # apre la connessione al DB
    if not conn:  # se la connessione fallisce
        return []  # ritorna lista vuota
    cursor = conn.cursor()  # crea un cursore per la SELECT
    cursor.execute("SELECT * FROM utenti")  # esegue la query per ottenere tutti gli utenti
    results = cursor.fetchall()  # preleva tutti i risultati della query
    cursor.close()  # chiude il cursore
    conn.close()  # chiude la connessione
    return results  # ritorna i risultati letti dal DB

def aggiorna_utente(user_id, nome, email):  # funzione per aggiornare un utente esistente
    conn = create_connection()  # apre la connessione al DB
    if not conn:  # se la connessione fallisce
        return False, "Connessione al DB fallita"  # ritorna errore
    cursor = conn.cursor()  # crea un cursore per l'UPDATE
    try:  # blocco try per gestire errori
        cursor.execute("UPDATE utenti SET nome=%s, email=%s WHERE id=%s", (nome, email, user_id))  # esegue l'UPDATE con parametri
        conn.commit()  # applica la transazione
        return True, "Utente aggiornato!"  # ritorna successo e messaggio
    except Error as e:  # cattura errori
        return False, str(e)  # ritorna False e il messaggio di errore
    finally:  # pulizia sempre eseguita
        cursor.close()  # chiude il cursore
        conn.close()  # chiude la connessione

def elimina_utente(user_id):  # funzione per eliminare un utente
    conn = create_connection()  # apre la connessione al DB
    if not conn:  # se la connessione fallisce
        return False, "Connessione al DB fallita"  # ritorna errore
    cursor = conn.cursor()  # crea un cursore per il DELETE
    try:  # blocco try per gestire errori
        cursor.execute("DELETE FROM utenti WHERE id=%s", (user_id,))  # esegue il DELETE usando parametro
        conn.commit()  # applica la transazione
        return True, "Utente eliminato!"  # ritorna successo e messaggio
    except Error as e:  # cattura errori
        return False, str(e)  # ritorna False e il messaggio di errore
    finally:  # pulizia sempre eseguita
        cursor.close()  # chiude il cursore
        conn.close()  # chiude la connessione
