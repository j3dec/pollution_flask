import os
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd

from app import app

db = SQLAlchemy(app)


def open_connexion(user, password):
    try:
        conn = psycopg2.connect(user=user, password=password);
        # conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
        print("Base connectée")

    except psycopg2.Error as e:
        print("Erreur lors de la connection à la base de données")
        print(e)
        return None
        # On force autocommit (non applicable ds SQLite3)
    conn.set_session(autocommit=True)
    return conn


def create_db_if_not_exists(conn, dbname):
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT datname FROM pg_database")
            list_db = cur.fetchall()
            list_db = str(list_db)
            if dbname in list_db:
                print(f"La base {dbname} existe déjà")
            else:
                print(f"La base {dbname} n'existe pas")
                # Create table statement
                sqlCreateDatabase = "create database " + dbname + ";"
                # Create a table in PostgreSQL database
                cur.execute(sqlCreateDatabase)
        except psycopg2.Error as e:
            print("Erreur lors de la création de la base de données")
            print(e)
            return
        cur.close()
        print("La base de données a été crée avec succès")


def delete_table(conn, sql_delete):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_delete)
        conn.commit()
    except psycopg2.Error as e:
        print("Erreur lors de la suppression de la table")
        print(e)
        return
    cursor.close()
    print("La table a été supprimée avec succès")


def create_table(conn, sql_create):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create)
        conn.commit()
    except psycopg2.Error as e:
        print("Erreur lors de la création de la table")
        print(e)
        return
    cursor.close()
    print("La table a été crée avec succès")


def insert_data(conn, sql_insert, donnees):
    try:
        cursor = conn.cursor()
        for d in donnees:
            cursor.execute(sql_insert, d)
        conn.commit()
    except psycopg2.Error as e:
        print("Erreur lors de l'insertion des données")
        print(e)
        return
    cursor.close()
    print("Les données ont été insérées avec succès")


def read_data(conn, sql_read):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_read)
        conn.commit()
    except psycopg2.Error as e:
        print("Erreur lors de la lecture des données")
        print(e)
        return None

    print("Les données ont été lues avec succès")
    data = []
    for row in cursor:
        data.append(row)

    cursor.close()

    return data


def creer_colonne(conn, sql_add_column):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_add_column)
        conn.commit()
    except psycopg2.Error as e:
        print("Erreur lors de la création de la colonne")
        print(e)
        return
    cursor.close()
    print("La colonne a été crée avec succès")


user = 'postgres'
password = 'root'
dbname = 'pollutiondb3'

create_db_if_not_exists(open_connexion(user, password), dbname)


engine = db.get_engine()  # db is the one from the question

path = os.getcwd() + "/app/static/csv"
# list_of_files = {}
# for filename in os.listdir(path):
#     list_of_files[filename] = path+filename

# Chemin csv
# path = os.path.dirname(os.path.abspath(__file__))
csv_NO2 = path + '/mesures_NO2.csv'
csv_PM10 = path + '/mesures_PM10.csv'
csv_mesures = path + '/mesures.csv'
csv_station = path + '/station.csv'
# Read CSV with Pandas
with open(csv_PM10, 'r', encoding='utf8') as file:
    df = pd.read_csv(file, delimiter=',')

# Insert to DB
# df.to_sql('polluant',
#           con=engine,
#           index=False,
#           index_label='id',
#           if_exists='replace')
#
with open(csv_station, 'r', encoding='utf8') as file:
    df = pd.read_csv(file, delimiter=',')
df.to_sql('station',
          con=engine,
          index=False,
          index_label='id',
          if_exists='replace')

# Add table rows Mesures
with open(csv_mesures, 'r') as file:
    df = pd.read_csv(file, delimiter=',')
df.to_sql('mesures',
          con=engine,
          index=False,
          index_label='id',
          if_exists='replace')
