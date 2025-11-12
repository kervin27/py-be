def doc_ottieni_utenti():  # documentazione per la rotta GET /utenti
    return {
        "tags": ["Utenti"],  # categoria della rotta
        "summary": "Ottieni lista di tutti gli utenti",  # titolo breve
        "description": "Restituisce la lista completa degli utenti registrati",  # descrizione dettagliata,
        "security": [{"Bearer": []}],  # indica che la rotta richiede autenticazione Bearer
        "responses": {
            "200": {
                "description": "Lista di utenti recuperata con successo",  # descrizione del successo
                "examples": {
                    "application/json": [
                        {"id": 1, "username": "Alice", "email": "alice@example.com"},  # esempio utente 1
                        {"id": 2, "username": "Bob", "email": "bob@example.com"}  # esempio utente 2
                    ]
                }
            }
        }
    }


def doc_crea_utente():  # documentazione per la rotta POST /utenti
    return {
        "tags": ["Utenti"],  # categoria della rotta
        "summary": "Crea un nuovo utente",  # titolo breve
        "description": "Aggiunge un nuovo utente al database con username, email e password",  # descrizione dettagliata
        "security": [{"Bearer": []}],  # indica che la rotta richiede autenticazione Bearer
        "parameters": [  # parametri del body della richiesta
            {
                "name": "body",  # nome del parametro
                "in": "body",  # posizione del parametro (nel corpo)
                "required": True,  # parametro obbligatorio
                "schema": {  # schema JSON del body
                    "type": "object",  # è un oggetto
                    "properties": {  # proprietà dell'oggetto
                        "username": {"type": "string", "example": "charlie"},  # username stringa
                        "email": {"type": "string", "example": "charlie@example.com"},  # email stringa
                        "password": {"type": "string", "example": "securepass123"}  # password stringa
                    },
                    "required": ["username", "email", "password"]  # tutti i campi sono obbligatori
                }
            }
        ],
        "responses": {
            "201": {
                "description": "Utente creato con successo",  # successo creazione
                "examples": {
                    "application/json": {"message": "Utente aggiunto!"}  # risposta di successo
                }
            },
            "400": {
                "description": "Errore nella creazione (parametri mancanti o duplicati)",  # errore validazione
                "examples": {
                    "application/json": {"message": "username, email e password obbligatori"}  # esempio errore
                }
            }
        }
    }


def doc_aggiorna_utente():  # documentazione per la rotta PUT /utenti/<user_id>
    return {
        "tags": ["Utenti"],  # categoria della rotta
        "summary": "Aggiorna un utente esistente",  # titolo breve
        "description": "Modifica i dati (username, email, password) di un utente specifico",  # descrizione dettagliata
        "security": [{"Bearer": []}],  # indica che la rotta richiede autenticazione Bearer
        "parameters": [  # parametri della richiesta
            {
                "name": "user_id",  # nome del parametro
                "in": "path",  # parametro nell'URL path
                "required": True,  # obbligatorio
                "type": "integer",  # tipo intero
                "example": 1  # esempio valore
            },
            {
                "name": "body",  # corpo della richiesta
                "in": "body",  # posizione nel body
                "required": True,  # obbligatorio
                "schema": {  # schema JSON del body
                    "type": "object",  # è un oggetto
                    "properties": {  # proprietà dell'oggetto
                        "username": {"type": "string", "example": "charlie_updated"},  # nuovo username
                        "email": {"type": "string", "example": "charlie_new@example.com"},  # nuova email
                        "password": {"type": "string", "example": "newpass456"}  # nuova password
                    },
                    "required": ["username", "email", "password"]  # tutti i campi sono obbligatori
                }
            }
        ],
        "responses": {
            "200": {
                "description": "Utente aggiornato con successo",  # successo aggiornamento
                "examples": {
                    "application/json": {"message": "Utente aggiornato!"}  # risposta di successo
                }
            },
            "400": {
                "description": "Errore nell'aggiornamento",  # errore aggiornamento
                "examples": {
                    "application/json": {"message": "Errore durante l'aggiornamento"}  # esempio errore
                }
            }
        }
    }


def doc_elimina_utente():  # documentazione per la rotta DELETE /utenti/<user_id>
    return {
        "tags": ["Utenti"],  # categoria della rotta
        "summary": "Elimina un utente",  # titolo breve
        "description": "Rimuove un utente dal database in base al suo ID",  # descrizione dettagliata
        "security": [{"Bearer": []}],  # indica che la rotta richiede autenticazione Bearer
        "parameters": [  # parametri della richiesta
            {
                "name": "user_id",  # nome del parametro
                "in": "path",  # parametro nell'URL path
                "required": True,  # obbligatorio
                "type": "integer",  # tipo intero
                "example": 1  # esempio valore
            }
        ],
        "responses": {
            "200": {
                "description": "Utente eliminato con successo",  # successo eliminazione
                "examples": {
                    "application/json": {"message": "Utente eliminato!"}  # risposta di successo
                }
            },
            "400": {
                "description": "Errore nell'eliminazione",  # errore eliminazione
                "examples": {
                    "application/json": {"message": "Errore durante l'eliminazione"}  # esempio errore
                }
            }
        }
    }

def doc_registra_utente():
    return {
        "tags": ["Autenticazione"],
        "summary": "Registra un nuovo utente",
        "description": "Crea un nuovo account utente con username, email e password",
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string", "example": "newuser"},
                        "email": {"type": "string", "example": "newuser@example.com"},
                        "password": {"type": "string", "example": "securepassword123"}
                    },
                    "required": ["username", "email", "password"]
                }
            }
        ],
        "responses": {
            "201": {
                "description": "Utente registrato con successo",
                "examples": {
                    "application/json": {"message": "Utente registrato!"}
                }
            },
            "400": {
                "description": "Errore nella registrazione",
                "examples": {
                    "application/json": {"message": "Errore durante la registrazione"}
                }
            }
        }
    }
def doc_login_utente():
    return {
        "tags": ["Autenticazione"],
        "summary": "Login utente",
        "description": "Autentica un utente e restituisce un token di accesso",
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string", "example": "existinguser"},
                        "password": {"type": "string", "example": "userpassword123"}
                    },
                    "required": ["username", "password"]
                }
            }
        ],
        "responses": {
            "200": {
                "description": "Login riuscito",
                "examples": {
                    "application/json": {"access_token": "jwt_token_here", "token_type": "bearer", "user": {
                    "email": "pippo@example.com",
                    "id": 2,
                    "username": "pippo"
                 }}
                }
            },
            "401": {
                "description": "Credenziali non valide",
                "examples": {
                    "application/json": {"message": "Credenziali non valide"}
                }
            }
        }
    }
def doc_rotta_protetta():
    return {
        "tags": ["Autenticazione"],
        "summary": "Rotta protetta",
        "description": "Esempio di rotta che richiede autenticazione tramite token JWT",
        "parameters": [
            {
                "name": "Authorization",
                "in": "header",
                "required": True,
                "type": "string",
                "example": "Bearer jwt_token_here"
            }
        ],
        "responses": {
            "200": {
                "description": "Accesso riuscito alla rotta protetta",
                "examples": {
                    "application/json": {"message": "Ciao user, sei autenticato!"}
                }
            },
            "401": {
                "description": "Token non valido o mancante",
                "examples": {
                    "application/json": {"message": "Token non valido o mancante"}
                }
            }
        }
    }