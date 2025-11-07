import os  # importa il modulo os per leggere variabili d'ambiente

# Configurazione variabili d’ambiente per Railway
DB_HOST = os.getenv("MYSQLHOST")  # legge l'host del DB dalla variabile d'ambiente MYSQLHOST
DB_USER = os.getenv("MYSQLUSER")  # legge l'utente del DB dalla variabile d'ambiente MYSQLUSER
DB_PASSWORD = os.getenv("MYSQLPASSWORD")  # legge la password del DB dalla variabile d'ambiente MYSQLPASSWORD
DB_NAME = os.getenv("MYSQLDATABASE")  # legge il nome del database dalla variabile d'ambiente MYSQLDATABASE
DB_PORT = int(os.getenv("MYSQLPORT", 3306))  # legge la porta del DB o usa 3306 come default, convertita in intero
