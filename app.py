from flask import Flask, request, jsonify
from db import create_table, aggiungi_utente, leggi_utenti, aggiorna_utente, elimina_utente
import os

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    return jsonify({"message": "✅ API Python CRUD su Railway attiva!"})

@app.route("/utenti", methods=["POST"])
def crea_utente():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    if not nome or not email:
        return jsonify({"error": "nome e email obbligatori"}), 400
    success, msg = aggiungi_utente(nome, email)
    return jsonify({"message": msg}), 201 if success else 400

@app.route("/utenti", methods=["GET"])
def ottieni_utenti():
    utenti = leggi_utenti()
    return jsonify([{"id": u[0], "nome": u[1], "email": u[2]} for u in utenti])

@app.route("/utenti/<int:user_id>", methods=["PUT"])
def aggiorna(user_id):
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    success, msg = aggiorna_utente(user_id, nome, email)
    return jsonify({"message": msg}), 200 if success else 400

@app.route("/utenti/<int:user_id>", methods=["DELETE"])
def elimina(user_id):
    success, msg = elimina_utente(user_id)
    return jsonify({"message": msg}), 200 if success else 400

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
