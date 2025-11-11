# src/api/user_routes.py (ESEMPIO)

from flask import Blueprint, request, jsonify
from src.services.user_services import aggiorna_dati_utente, elimina_utente_by_id,crea_nuovo_utente, get_utenti

# Crea un Blueprint per raggruppare le rotte utente
user_bp = Blueprint('users', __name__, url_prefix='/utenti')

@user_bp.route("", methods=["GET"])
def ottieni_utenti():
    utenti = get_utenti() # Chiama il service per ottenere gli utenti
    return jsonify(utenti),200


@user_bp.route("", methods=["POST"])
def crea_utente():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Chiama la logica di business nel SERVICE
    success, msg = crea_nuovo_utente(username, email, password) 
    
    return jsonify({"message": msg}), 201 if success else 400


@user_bp.route("/<int:user_id>", methods=["PUT"])  # definisce la route per aggiornare un utente identificato da user_id con metodo PUT
def aggiorna(user_id):  # funzione che gestisce l'aggiornamento dell'utente; riceve user_id dalla route
    data = request.get_json()  # legge il corpo della richiesta come JSON
    username = data.get("username")  # estrae il nuovo username (se presente)
    email = data.get("email")  # estrae la nuova email (se presente)
    password = data.get("password")  # estrae la nuova password (se presente)
    success, msg = aggiorna_dati_utente(user_id, username, email, password)  # chiama la funzione che aggiorna il DB
    return jsonify({"message": msg}), 200 if success else 400  # ritorna 200 se aggiornamento avvenuto, altrimenti 400

@user_bp.route("/<int:user_id>", methods=["DELETE"])  # definisce la route per eliminare un utente identificato da user_id con metodo DELETE
def elimina(user_id):  # funzione che gestisce l'eliminazione; riceve user_id dalla route
    success, msg = elimina_utente_by_id(user_id)  # chiama la funzione che elimina l'utente dal DB
    return jsonify({"message": msg}), 200 if success else 400  # ritorna 200 se eliminazione avvenuta, altrimenti 400
