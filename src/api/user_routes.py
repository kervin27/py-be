# src/api/user_routes.py (ESEMPIO)

from flask import Blueprint, request, jsonify  # importa Blueprint, request e jsonify da Flask
from src.api.auth_route import get_current_user
from src.docs.user_doc import doc_ottieni_utenti, doc_crea_utente, doc_aggiorna_utente, doc_elimina_utente  # importa tutte le documentazioni Swagger
from src.services.user_services import aggiorna_dati_utente, elimina_utente_by_id, crea_nuovo_utente, get_utenti  # importa i servizi
from flasgger import swag_from  # importa swag_from per applicare la documentazione

# Crea un Blueprint per raggruppare le rotte utente
user_bp = Blueprint('users', __name__, url_prefix='/utenti')  # Blueprint con prefisso /utenti

@user_bp.route("", methods=["GET"])  # rotta GET /utenti
@swag_from(doc_ottieni_utenti())  # applica la documentazione Swagger per GET
def ottieni_utenti():  # funzione che restituisce la lista degli utenti

    current_user = get_current_user()
    if not current_user:
        return jsonify({"error": "Token mancante o non valido"}), 401

    utenti = get_utenti()  # chiama il service per ottenere gli utenti
    return jsonify(utenti), 200  # ritorna la lista in JSON con status 200

@user_bp.route("", methods=["POST"])  # rotta POST /utenti
@swag_from(doc_crea_utente())  # applica la documentazione Swagger per POST
def crea_utente():  # funzione che crea un nuovo utente
    data = request.get_json()  # legge il JSON dal corpo della richiesta
    username = data.get("username")  # estrae il campo username
    email = data.get("email")  # estrae il campo email
    password = data.get("password")  # estrae il campo password
    success, msg = crea_nuovo_utente(username, email, password)  # chiama il service per creare l'utente
    return jsonify({"message": msg}), 201 if success else 400  # ritorna 201 se successo, altrimenti 400

@user_bp.route("/<int:user_id>", methods=["PUT"])  # rotta PUT /utenti/<user_id>
@swag_from(doc_aggiorna_utente())  # applica la documentazione Swagger per PUT
def aggiorna(user_id):  # funzione che aggiorna un utente
    data = request.get_json()  # legge il JSON dal corpo della richiesta
    username = data.get("username")  # estrae il nuovo username
    email = data.get("email")  # estrae la nuova email
    password = data.get("password")  # estrae la nuova password
    success, msg = aggiorna_dati_utente(user_id, username, email, password)  # chiama il service per aggiornare
    return jsonify({"message": msg}), 200 if success else 400  # ritorna 200 se successo, altrimenti 400

@user_bp.route("/<int:user_id>", methods=["DELETE"])  # rotta DELETE /utenti/<user_id>
@swag_from(doc_elimina_utente())  # applica la documentazione Swagger per DELETE
def elimina(user_id):  # funzione che elimina un utente
    success, msg = elimina_utente_by_id(user_id)  # chiama il service per eliminare l'utente
    return jsonify({"message": msg}), 200 if success else 400  # ritorna 200 se successo, altrimenti 400
