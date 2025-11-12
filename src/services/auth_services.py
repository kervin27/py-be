from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from flask import abort
from src.db_access.auth_db import get_user_by_username, get_user_by_email, create_user

# --- Password hashing ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
MAX_PASSWORD_LENGTH = 72  # limite massimo per bcrypt

def hash_password(password: str) -> str:
    """Crea l'hash della password (bcrypt accetta max 72 byte)."""
    if not password:
        abort(400, "La password è obbligatoria")

    if len(password) > MAX_PASSWORD_LENGTH:
        abort(400, f"La password non può superare {MAX_PASSWORD_LENGTH} caratteri")

    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """Verifica che la password fornita corrisponda all'hash salvato."""
    return pwd_context.verify(password, hashed)

# --- JWT settings ---
SECRET_KEY = "il_tuo_segreto_super_sicuro"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- JWT creation ---
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """Crea un token JWT firmato con scadenza."""
    to_encode = data.copy()
    if "sub" not in to_encode:
        abort(400, "Il token deve contenere la chiave 'sub'")

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp": expire,
        "iat": datetime.now(timezone.utc)
    })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- User authentication ---
def authenticate_user(username: str, password: str):
    """Autentica un utente verificando username e password."""
    user_exists, user_data = get_user_by_username(username)
    if not user_exists:
        return None

    if not verify_password(password, user_data["password"]):
        return None

    return user_data

# --- User registration ---
def register_user(username: str, email: str, password: str):
    user_exists, _ = get_user_by_username(username)
    if user_exists:
        abort(400, "Username già registrato")

    email_exists, _ = get_user_by_email(email)
    if email_exists:
        abort(400, "Email già registrata")

    hashed_pw = hash_password(password)
    success, result = create_user(username, email, hashed_pw)

    if not success:
        abort(500, result)

    return result  # ← qui ritorni il dict con l'id


# --- Token verification ---
def verify_token(token: str):
    """Verifica la validità del token JWT e restituisce l'username."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            abort(401, "Token non valido")
        return username
    except JWTError:
        abort(401, "Token non valido")
