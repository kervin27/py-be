from flask import Flask, request, jsonify  # importa Flask per l'app, request per leggere richieste e jsonify per risposte JSON
from flask_cors import CORS  # importa CORS per abilitare le richieste cross-origin
from db import create_table, aggiungi_utente, leggi_utenti, aggiorna_utente, elimina_utente  # importa funzioni per gestire il DB
import os  # importa il modulo os per leggere variabili d'ambiente

app = Flask(__name__)  # crea l'istanza dell'app Flask usando il nome del modulo corrente
CORS(app)  # abilita CORS sull'app per permettere chiamate da browser di altri domini

create_table()  # crea la tabella nel DB all'avvio se non esiste

@app.route("/")  # definisce la route radice dell'API (GET di default)
def home():  # funzione che gestisce la route radice
    return jsonify({"message": "✅ API Python CRUD su Railway attiva!"})  # risponde con un messaggio JSON di conferma

if __name__ == "__main__":  # esegue il server solo se lo script è avviato direttamente
    port = int(os.getenv("PORT", 8000))  # legge la variabile d'ambiente PORT o usa 8000 come default
    app.run(host="0.0.0.0", port=port)  # avvia il server Flask su tutte le interfacce e sulla porta specificata
