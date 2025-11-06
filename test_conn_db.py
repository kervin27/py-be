from db import get_db_connection

try:
    conn = get_db_connection()
    print("✅ Connessione avvenuta con successo!")
    conn.close()
except Exception as e:
    print("❌ Errore di connessione:", e)
