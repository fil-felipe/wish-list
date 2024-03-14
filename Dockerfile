# Pobranie oficjalnego bazowego obrazu Docker Pythona
FROM python:3.10.6

# Ustawienie zmiennych środowiskowych
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Ustawienie katalogu roboczego
WORKDIR /code

# Instalacja zależności
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Skopiowanie projektu Django
COPY . /code/
