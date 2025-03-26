from logging import exception
import pandas as pd
import numpy as np
import psycopg2 as pg
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import matplotlib.pyplot as plt
from dotenv import dotenv_values
from pyfiglet import Figlet

f = Figlet(font="slant")

df = pd.read_csv("./data/master_data/data.csv")

config = dotenv_values("./.env")

try:

    # Connect to the PostgreSQL database
    conn = pg.connect(
        host="localhost",
        dbname="postgres",
        user=config["postgres_user"],
        password=config["postgres_pw"],
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS project_vector")
    cur.execute("CREATE DATABASE project_vector")
    cur.close()
    conn.close()

    conn = pg.connect(
        host="localhost",
        database="project_vector",
        user=config["postgres_user"],
        password=config["postgres_pw"],
    )
    cur = conn.cursor()
    # Erstelle die pgvector-Erweiterung und Tabelle
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    cur.execute(
        f"""
        CREATE TABLE IF NOT EXISTS my_vectors (
            id SERIAL PRIMARY KEY,
            vector vector({len(df.columns)}) 
        )
    """
    )
    conn.commit()
    cur.execute("delete from my_vectors")
    conn.commit()

    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO my_vectors (vector) VALUES (%s)",
            ([float(x) for x in row.values],),
        )

    print(f.renderText("Data is loaded into Postgres"))
    conn.commit()
    cur.close()
    conn.close()

    print("Daten erfolgreich gespeichert!")


except pg.OperationalError as operationalerror:
    print(operationalerror.__str__())
