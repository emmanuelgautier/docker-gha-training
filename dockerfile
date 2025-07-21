# Utiliser la dernière version stable de Python avec l'image slim (optimisée)
FROM python:slim

# Définir un dossier de travail non root (bonnes pratiques de sécurité)
WORKDIR /app

# Copier uniquement les fichiers nécessaires
COPY requirements.txt .

# Installer les dépendances en limitant les caches
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l’application
COPY . .

# Lancer l’application
CMD ["python", "app/main.py"]