# Basis-Image mit Python
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Quellcode ins Image kopieren
COPY . .

# Exponiere Port 5000 für Flask
EXPOSE 5000

# Befehl zum Starten der App
CMD ["python", "main.py"]
