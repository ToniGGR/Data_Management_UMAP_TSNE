# Data_Management_UMAP_TSNE
Data Management Project comparing T-SNE and UMAP Algorithm to visualize music data

# README

## Table of Contents
1. [Installation](#installation)
   - [Installing PostgreSQL](#installing-postgresql)
   - [Installing PGVector](#installing-pgvector)
   - [Cloning the GitHub Repository](#cloning-the-github-repository)
   - [Installing PGAdmin](#installing-pgadmin)
   - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
   - [Installing Dependencies](#installing-dependencies)
   - [Configuring User Credentials](#configuring-user-credentials)
2. [Data Source](#data-source)
3. [Database Configuration](#database-configuration)
4. [Jupyter Notebooks](#jupyter-notebooks)

## Installation

This project was developed on a Linux-based system, so the following instructions are specifically for Linux environments.

### Installing PostgreSQL
To install PostgreSQL, run the following command:
```sh
sudo apt-get install postgresql
```

### Installing PGVector
To use the PGVector extension for PostgreSQL, first download the Docker image and then create a Docker container:
```sh
docker pull ankane/pgvector
sudo docker run -e POSTGRES_PASSWORD=PW -p 5432:5432 ankane/pgvector
```
After that, the extension can be added in PGAdmin.

### Cloning the GitHub Repository
The project can be cloned using the following command:
```sh
git clone https://github.com/ToniGGR/Data_Management_UMAP_TSNE.git
```

### Installing PGAdmin
To install PGAdmin, execute the following steps:
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

### Setting Up a Virtual Environment
A virtual environment can be created using:
```sh
python -m venv venv
```
Activate it with:
```sh
source venv/bin/activate
```

### Installing Dependencies
All required dependencies can be installed using the `requirements.txt` file with:
```sh
pip install -r /path/to/requirements.txt
```

### Configuring User Credentials
A `.env` file must be created with the following structure:
```ini
postgres_user='your_user'
postgres_pw='your_pw'
```

## Data Source
The dataset used is downloaded from Kaggle, saved as a CSV file, and placed in the `/data` directory.

## Database Configuration
To set up the database, the PGVector extension must be installed and activated in PGAdmin. The required database `project_vector` is initialized and populated by running the following Python script:
```sh
python code/fill_table.py
```
**Important:** PGAdmin should only be started and connected to the database after the script has completed execution.

## Jupyter Notebooks
After setting up the database, the following notebooks in the `code/` directory can be executed:
- `UMAP.ipynb`
- `TSNE.ipynb`

Only after successfully running both notebooks should the data be analyzed in `Analysis.ipynb`.

