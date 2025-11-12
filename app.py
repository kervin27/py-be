from flask import Flask, request, jsonify  # importa Flask per l'app, request per leggere richieste e jsonify per risposte JSON
from flask_cors import CORS  # importa CORS per abilitare le richieste cross-origin
import os
from src.api.user_routes import user_bp
from src.api.auth_route import auth_bp
from flasgger import Swagger


app = Flask(__name__)  # crea l'istanza dell'app Flask usando il nome del modulo corrente
CORS(app)  # abilita CORS sull'app per permettere chiamate da browser di altri domini



# registra blueprint
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)


swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "La mia API",
        "description": "API con autenticazione JWT",
        "version": "1.0"
    },
    "securityDefinitions": {  # <-- definisci il Bearer token
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Inserisci il token JWT con prefisso 'Bearer '"
        }
    }
}

swagger = Swagger(app, template=swagger_template)


@app.route("/")  # definisce la route radice dell'API (GET di default)
def home():  # funzione che gestisce la route radice
    return jsonify({"message": "✅ API Python CRUD su Railway attiva!"})  # risponde con un messaggio JSON di conferma

if __name__ == "__main__":  # esegue il server solo se lo script è avviato direttamente
    port = int(os.getenv("PORT", 8000))  # legge la variabile d'ambiente PORT o usa 8000 come default
    app.run(host="0.0.0.0", port=port)  # avvia il server Flask su tutte le interfacce e sulla porta specificata
