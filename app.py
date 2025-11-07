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

@app.route("/utenti", methods=["POST"])  # definisce la route per creare un nuovo utente con metodo POST
def crea_utente():  # funzione che gestisce la creazione di un utente
    data = request.get_json()  # legge il corpo della richiesta come JSON e lo assegna a data
    nome = data.get("nome")  # estrae il campo 'nome' dal JSON della richiesta
    email = data.get("email")  # estrae il campo 'email' dal JSON della richiesta
    if not nome or not email:  # controlla che nome e email siano forniti
        return jsonify({"error": "nome e email obbligatori"}), 400  # se mancanti ritorna errore 400 con messaggio JSON
    success, msg = aggiungi_utente(nome, email)  # chiama la funzione per aggiungere l'utente al DB
    return jsonify({"message": msg}), 201 if success else 400  # ritorna 201 se aggiunta avvenuta, altrimenti 400

@app.route("/utenti", methods=["GET"])  # definisce la route per leggere tutti gli utenti con metodo GET
def ottieni_utenti():  # funzione che restituisce la lista degli utenti
    utenti = leggi_utenti()  # legge tutti gli utenti dal DB
    return jsonify([{"id": u[0], "nome": u[1], "email": u[2]} for u in utenti])  # converte i risultati in lista di dizionari e restituisce JSON

@app.route("/utenti/<int:user_id>", methods=["PUT"])  # definisce la route per aggiornare un utente identificato da user_id con metodo PUT
def aggiorna(user_id):  # funzione che gestisce l'aggiornamento dell'utente; riceve user_id dalla route
    data = request.get_json()  # legge il corpo della richiesta come JSON
    nome = data.get("nome")  # estrae il nuovo nome (se presente)
    email = data.get("email")  # estrae la nuova email (se presente)
    success, msg = aggiorna_utente(user_id, nome, email)  # chiama la funzione che aggiorna il DB
    return jsonify({"message": msg}), 200 if success else 400  # ritorna 200 se aggiornamento avvenuto, altrimenti 400

@app.route("/utenti/<int:user_id>", methods=["DELETE"])  # definisce la route per eliminare un utente identificato da user_id con metodo DELETE
def elimina(user_id):  # funzione che gestisce l'eliminazione; riceve user_id dalla route
    success, msg = elimina_utente(user_id)  # chiama la funzione che elimina l'utente dal DB
    return jsonify({"message": msg}), 200 if success else 400  # ritorna 200 se eliminazione avvenuta, altrimenti 400

if __name__ == "__main__":  # esegue il server solo se lo script è avviato direttamente
    port = int(os.getenv("PORT", 8000))  # legge la variabile d'ambiente PORT o usa 8000 come default
    app.run(host="0.0.0.0", port=port)  # avvia il server Flask su tutte le interfacce e sulla porta specificata
