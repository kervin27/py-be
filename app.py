from flask import Flask, request, jsonify
from db import create_table, aggiungi_utente, leggi_utenti
import os

# -----------------------------
# Creazione tabella (all'avvio)
# -----------------------------
create_table()

# -----------------------------
# Flask API
# -----------------------------
app = Flask(__name__)

@app.route("/utente", methods=["POST"])
def crea_utente():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    if not nome or not email:
        return jsonify({"error": "nome e email obbligatori"}), 400
    success, message = aggiungi_utente(nome, email)
    status = 201 if success else 400
    return jsonify({"message": message}), status

@app.route("/utenti", methods=["GET"])
def ottieni_utenti():
    utenti = leggi_utenti()
    return jsonify([{"id": u[0], "nome": u[1], "email": u[2]} for u in utenti])

# -----------------------------
# Avvio Flask
# -----------------------------
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
