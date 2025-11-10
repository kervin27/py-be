# src/api/user_routes.py (ESEMPIO)

from flask import  Flask, request, jsonify
from src.services.user_services import aggiorna_utente, elimina_utente,crea_nuovo_utente, get_all_utenti
from flasgger import Swagger

# Crea un Blueprint per raggruppare le rotte utente
app = Flask(__name__)  # crea l'istanza dell'app Flask usando il nome del modulo corrente
swagger = Swagger(app)

@app.route("/utenti", methods=["POST"])
def crea_utente():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Chiama la logica di business nel SERVICE
    success, msg = crea_nuovo_utente(username, email, password) 
    
    return jsonify({"message": msg}), 201 if success else 400

@app.route("/utenti", methods=["GET"])
def ottieni_utenti():
    utenti = get_all_utenti() # Chiama il service
    return jsonify([{"id": u[0], "username": u[1], "email": u[2]} for u in utenti])



@app.route("/utenti/<int:user_id>", methods=["PUT"])  # definisce la route per aggiornare un utente identificato da user_id con metodo PUT
def aggiorna(user_id):  # funzione che gestisce l'aggiornamento dell'utente; riceve user_id dalla route
    data = request.get_json()  # legge il corpo della richiesta come JSON
    username = data.get("username")  # estrae il nuovo username (se presente)
    email = data.get("email")  # estrae la nuova email (se presente)
    password = data.get("password")  # estrae la nuova password (se presente)
    success, msg = aggiorna_utente(user_id, username, email, password)  # chiama la funzione che aggiorna il DB
    return jsonify({"message": msg}), 200 if success else 400  # ritorna 200 se aggiornamento avvenuto, altrimenti 400

@app.route("/utenti/<int:user_id>", methods=["DELETE"])  # definisce la route per eliminare un utente identificato da user_id con metodo DELETE
def elimina(user_id):  # funzione che gestisce l'eliminazione; riceve user_id dalla route
    success, msg = elimina_utente(user_id)  # chiama la funzione che elimina l'utente dal DB
    return jsonify({"message": msg}), 200 if success else 400  # ritorna 200 se eliminazione avvenuta, altrimenti 400
