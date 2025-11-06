# Python CRUD API con Flask e MySQL su Railway

## 🚀 Setup locale
1. Crea un ambiente virtuale:
   ```bash
   python -m venv venv
   source venv/bin/activate  # su Mac/Linux
   venv\Scripts\activate     # su Windows
   ```

2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

3. Crea un file `.env` (solo per test locale):
   ```
   MYSQLHOST=localhost
   MYSQLUSER=root
   MYSQLPASSWORD=tuapassword
   MYSQLDATABASE=railway
   MYSQLPORT=3306
   ```

4. Avvia il server:
   ```bash
   python app.py
   ```

---

## ☁️ Deploy su Railway

1. Crea un nuovo progetto su [Railway.app](https://railway.app)  
2. Aggiungi un servizio **MySQL**  
3. Copia automaticamente le variabili d’ambiente  
4. Aggiungi il servizio **Python** con questo progetto  
5. Railway eseguirà `python app.py` automaticamente.
