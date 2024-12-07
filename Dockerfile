# Imagine de bază
FROM python:3.9-slim

# Setează directorul de lucru
WORKDIR /app

# Copiază fișierele în container
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expune portul 5000
EXPOSE 5000

# Rulează aplicația
CMD ["python", "app.py"]
