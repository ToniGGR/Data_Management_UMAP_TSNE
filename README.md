# Data_Management_UMAP_TSNE
Data Management Project comparing T-SNE and UMAP Algorithm to visualize music data

# README

## Installation

Dieses Projekt wurde auf einem Linux-basierten System entwickelt, daher ist die folgende Anleitung speziell für Linux-Umgebungen geeignet.

### Installation von PostgreSQL
Zur Installation von PostgreSQL kann folgender Befehl ausgeführt werden:
```sh
sudo apt-get install postgresql
```

### Installation von PGVector
Um die Erweiterung PGVector für PostgreSQL zu nutzen, wird zunächst ein Docker-Image heruntergeladen und dann ein Docker-Container erstellt:
```sh
docker pull ankane/pgvector
sudo docker run -e POSTGRES_PASSWORD=PW -p 5432:5432 ankane/pgvector
```
Danach kann die Erweiterung in PGAdmin hinzugefügt werden.

### Klonen des GitHub-Repositories
Das Projekt kann mit folgendem Befehl geklont werden:
```sh
git clone https://github.com/ToniGGR/Data_Management_UMAP_TSNE.git
```

### Installation von PGAdmin
Zur Installation von PGAdmin werden folgende Schritte ausgeführt:
```sh
sudo mkdir /var/lib/pgadmin
sudo mkdir /var/log/pgadmin
sudo chown $USER /var/lib/pgadmin
sudo chown $USER /var/log/pgadmin
python3 -m venv pgadmin4
source pgadmin4/bin/activate
pip install pgadmin4
pgadmin4
```

### Einrichten eines virtuellen Environments
Ein virtuelles Environment wird mit folgendem Befehl erstellt:
```sh
python -m venv venv
```
Das Environment kann dann mit:
```sh
source venv/bin/activate
```
gestartet werden.

### Installation der Bibliotheken
Alle erforderlichen Bibliotheken können durch die Datei `requirements.txt` mit folgendem Befehl installiert werden:
```sh
pip install -r /path/to/requirements.txt
```

### Einrichten der Benutzer-Credentials
Eine `.env`-Datei muss erstellt werden und folgende Struktur aufweisen:
```ini
postgres_user='your_user'
postgres_pw='your_pw'
```

## Datengrundlage
Die Datengrundlage besteht aus einem von Kaggle heruntergeladenen Datensatz, der als CSV-Datei gespeichert wurde und im Verzeichnis `/data` abgelegt ist.

## Datenbankkonfiguration
Damit die Datenbank korrekt eingerichtet werden kann, muss die PGVector-Erweiterung installiert und in PGAdmin aktiviert sein. Die erforderliche Datenbank `project_vector` wird durch das folgende Python-Skript mit den notwendigen Tabellen gefüllt:
```sh
python code/fill_table.py
```
**Wichtig:** PGAdmin darf erst gestartet und mit der Datenbank verbunden werden, nachdem das Skript durchgelaufen ist.

## Jupyter Notebooks
Nach der Einrichtung der Datenbank können die folgenden Notebooks im Verzeichnis `code/` ausgeführt werden:
- `UMAP.ipynb`
- `TSNE.ipynb`

Erst nach dem erfolgreichen Durchlauf beider Notebooks können die Daten im `Analysis.ipynb` Notebook analysiert werden.

