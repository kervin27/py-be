from flask import Blueprint, request, jsonify
from flasgger import swag_from

from src.docs.user_doc import doc_login_utente, doc_registra_utente, doc_rotta_protetta
from src.services.auth_services import authenticate_user, create_access_token, register_user, verify_token

auth_bp = Blueprint("auth", __name__, template_folder="templates", url_prefix='/auth')

# Funzione per ottenere l'utente corrente dal token JWT
def get_current_user():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None
    token = auth_header.split(" ")[1]
    return verify_token(token)

# Registrazione
@auth_bp.route("/register", methods=["POST"])
@swag_from(doc_registra_utente())
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"message": "Missing fields"}), 400

    success, msg = register_user(username, email, password)
    return jsonify({"message": msg}), 200 if success else 400  # ritorna 200 se successo, altrimenti 400

# Login
@auth_bp.route("/login", methods=["POST"])
@swag_from(doc_login_utente())
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    user = authenticate_user(username, password)
    if not user:
        return jsonify({"message": "Username o password non corretti"}), 401

    # user è un dict, quindi accesso tramite chiave
    token = create_access_token(data={"sub": user["username"]})

    # opzionale: puoi restituire anche l'id dell'utente
    return jsonify({
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user["id"],
            "username": user["username"],
            "email": user["email"]
        }
    }), 200


# Rotta protetta
@auth_bp.route("/protected", methods=["GET"])
@swag_from(doc_rotta_protetta())
def protected_route():
    current_user = get_current_user()
    if not current_user:
        return jsonify({"message": "Token mancante o non valido"}), 401
    return jsonify({"message": f"Ciao {current_user}, sei autenticato!"})
