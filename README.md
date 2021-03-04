Dans le terminal exécuter les commandes suivantes : 

````python
pip install -r requirements.txt
set FLASK_APP = pollution.py
flask run
````

Adapter dans le fichier config.py :

```python
# Pas besoin de créer la base de donnée dans pgAdmin tout ce fait dans le fichier database.py
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5432/nom_db'
```

Pour l'instant aucun contenu dans le pages html, on crée seulement la DB, tables et insertion des csv