FROM python:3.11-slim

# Mise à jour et installation d'awscli
RUN apt-get update -y && apt-get install -y awscli

WORKDIR /app

COPY . /app/
# 4️⃣ Installer les dépendances Python
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
