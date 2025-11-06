from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from db import get_db_connection
import os


app = Flask(__name__)
CORS(app)
swagger = Swagger(app)


@app.route('/utenti', methods=['POST'])
def crea_utente():
    """
    Crea un nuovo utente
    ---
    tags:
      - Utenti
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - nome
            - email
          properties:
            nome:
              type: string
            email:
              type: string
    responses:
      201:
        description: Utente creato con successo
    """
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO utenti (nome, email) VALUES (%s, %s)", (nome, email))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Utente creato con successo'}), 201


@app.route('/utenti', methods=['GET'])
def lista_utenti():
    """
    Restituisce la lista di tutti gli utenti
    ---
    tags:
      - Utenti
    responses:
      200:
        description: Lista utenti
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM utenti")
    utenti = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(utenti)


@app.route('/utenti/<int:id>', methods=['PUT'])
def aggiorna_utente(id):
    """
    Aggiorna un utente esistente
    ---
    tags:
      - Utenti
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID dell'utente
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            email:
              type: string
    responses:
      200:
        description: Utente aggiornato con successo
    """
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE utenti SET nome=%s, email=%s WHERE id=%s", (nome, email, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Utente aggiornato con successo'})


@app.route('/utenti/<int:id>', methods=['DELETE'])
def elimina_utente(id):
    """
    Elimina un utente
    ---
    tags:
      - Utenti
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID dell'utente da eliminare
    responses:
      200:
        description: Utente eliminato con successo
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM utenti WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Utente eliminato con successo'})
