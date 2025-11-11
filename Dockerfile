# Usa un'immagine ufficiale Python leggera
FROM python:3.11-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia tutto il contenuto della root nel container
COPY . /app

# Installa le dipendenze se hai un requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando per avviare l'app Python
CMD ["python", "app.py"]
