import mysql.connector  # importa il connettore MySQL per Python
from mysql.connector import Error  # importa l'eccezione Error dal connettore
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT  # importa le variabili di configurazione DB


print(f"Connettendo a MySQL con host={DB_HOST}, user={DB_USER}, db={DB_NAME}")

def create_connection():  # definisce funzione per creare la connessione al DB
    try:  # avvia blocco try per gestire errori di connessione
        conn = mysql.connector.connect(  # crea la connessione al DB con i parametri forniti
            host=DB_HOST,  # host del DB
            user=DB_USER,  # utente DB
            password=DB_PASSWORD,  # password DB
            database=DB_NAME,  # nome del database
            port=DB_PORT,  # porta del DB
        )  # fine creazione connessione
        print(f"✅ Connessione al DB avvenuta con successo: {DB_HOST}:{DB_PORT}")
        return conn  # ritorna l'oggetto connessione se riuscito
    except Error as e:  # cattura eccezioni di tipo Error
        print("❌ Errore connessione DB:", e)  # stampa un messaggio di errore sulla console
        return None  # ritorna None se la connessione fallisce
