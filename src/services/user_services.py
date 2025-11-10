import mysql.connector  # importa il connettore MySQL per Python
from mysql.connector import Error  # importa l'eccezione Error dal connettore
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT
from db import create_connection
from src.db_access.user_db import add_user, delete_user, get_all_users_from_db, update_user  # importa le variabili di configurazione DB


def create_table():  # definisce funzione per creare la tabella se non esiste
    conn = create_connection()  # crea o ottiene la connessione al DB
    if conn:  # controlla che la connessione sia valida
        cursor = conn.cursor()  # crea un cursore per eseguire comandi SQL
        # sostituisce 'nome' con 'username' e aggiunge 'password'
        cursor.execute("CREATE TABLE IF NOT EXISTS utenti (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL);")  # esegue comando SQL per creare la tabella utenti se non esiste
        conn.commit()  # applica le modifiche al DB
        cursor.close()  # chiude il cursore
        conn.close()  # chiude la connessione


##################


def get_utenti():
    """Recupera gli utenti dal repository e li formatta per l'API."""
    
    # 1. Chiama il Repository per ottenere i dati grezzi (lista di tuple)
    raw_users = get_all_users_from_db()

    # 2. LOGICA DI BUSINESS / MAPPATURA
    
    # Prepara il risultato come lista di dizionari (come facevi nel Controller)
    utenti_formattati = []
    for user_tuple in raw_users:
        # Assumiamo l'ordine: (id, username, email)
        utenti_formattati.append({
            "id": user_tuple[0], 
            "username": user_tuple[1], 
            "email": user_tuple[2]
        })
        
    return utenti_formattati



def crea_nuovo_utente(username: str, email: str, password: str) -> tuple[bool, str]:
    """
    Gestisce la logica di business e delega l'inserimento al Repository.
    """
    
    # 1. LOGICA DI BUSINESS/VALIDAZIONE (dovrebbe avvenire qui!)
    if not username or not email or not password:
        return False, "username, email e password obbligatori"
        
    # ESEMPIO: Aggiunta di logica di validazione mancante
    if "@" not in email or "." not in email:
        return False, "Formato email non valido."
        
    # ESEMPIO: Preparazione/Trasformazione dei dati (Cruciale!)
    # **IMPORTANTE:** Qui dovresti hashare la password prima di inviarla al DB!
    # hashed_password = hash_password_function(password) 
    hashed_password = password # Per ora usiamo quella non hashata, ma andrebbe sistemato!
    
    # 2. Chiama il Repository con i dati puliti e pronti
    success, msg = add_user(username, email, hashed_password)
    
    # 3. Restituisce il risultato finale all'API
    if success:
        return True, "Utente creato con successo!"
    else:
        # Passa il messaggio di errore DB (es. email già esistente)
        return False, msg

def aggiorna_dati_utente(user_id: int, username: str = None, email: str = None, password: str = None) -> tuple[bool, str]:
    """
    Gestisce la logica di business e prepara i dati per l'aggiornamento.
    """
    
    # 1. PREPARAZIONE DEI DATI: Crea un dizionario solo con i campi che hanno un valore.
    updates = {}
    
    if username:
        # LOGICA DI VALIDAZIONE USERNAME: qui puoi aggiungere controlli sulla lunghezza, ecc.
        updates['username'] = username
        
    if email:
        # LOGICA DI VALIDAZIONE EMAIL: qui puoi verificare il formato dell'email.
        updates['email'] = email
        
    if password:
        # LOGICA CRUCIALE DI BUSINESS: Hashing della password prima dell'aggiornamento!
        # hashed_password = hash_password_function(password) 
        updates['password'] = password # SOSTITUIRE con l'hash

    if not updates:
        return False, "Nessun dato valido fornito per l'aggiornamento."

    # 2. Chiama il Repository con l'ID e il dizionario di aggiornamento
    success, msg = update_user(user_id, updates)
    
    # 3. Restituisce il risultato
    if success:
        return True, "Utente aggiornato con successo!"
    else:
        # Passa il messaggio di errore dal DB (es. email duplicata)
        return False, msg

def elimina_utente_by_id(user_id: int) -> tuple[bool, str]:
    """
    Gestisce la logica di business pre-eliminazione e delega al Repository.
    """
    
    # 1. LOGICA DI VALIDAZIONE
    if user_id <= 0:
        return False, "ID utente non valido."
        
    # ESEMPIO: Se ci fosse una logica per controllare se l'utente ha ordini attivi, andrebbe qui.
    
    # 2. Chiama il Repository
    success, msg = delete_user(user_id)
    
    # 3. Restituisce il risultato
    if success:
        return True, "Utente eliminato con successo!"
    else:
        # Passa il messaggio di errore dal DB (es. utente non trovato)
        return False, msg    

 