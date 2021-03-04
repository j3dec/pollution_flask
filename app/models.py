from app.database import db


class Mesures(db.Model):
    __tablename__ = 'mesures'

    id = db.Column(db.Integer, primary_key=True)
    niveau = db.Column(db.String(100), nullable=False)
    etat = db.Column(db.String(100), )
    date = db.Column(db.Date(), nullable=False)
    code_station = db.Column(db.Integer, db.ForeignKey('station.code'), nullable=False)
    id_polluant = db.Colulmn(db.Integer, db.ForeignKey('polluant.id'), nullable=False)

    def __init__(self, niveau, etat, date, code_station, id_polluant):
        self.niveau = niveau
        self.etat = etat
        self.date = date
        self.code_station = code_station
        self.id_polluant = id_polluant

    def __str__(self):
        return f'relevé du {self.date}'


class Polluant(db.Model):
    __tablename__ = 'polluant'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)

    def __init__(self, id, nom):
        self.id = id
        self.nom = nom

    def __str__(self):
        return f'{self.nom}'


class Station(db.Model):
    __tablename__ = 'station'
    code = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), unique=True)
    zone = db.Column(db.String(100), unique=True)
    departement = db.Column(db.String(100), unique=False)
    typologie= db.Column(db.String(100))
    x_reglementaire = db.Column(db.Float(50))
    y_reglementaire = db.Column(db.Float(50))

    def __init__(self, code, nom, zone, departement, typologie, x_reglementaire, y_reglementaire):
        self.code = code
        self.nom = nom
        self.zone = zone
        self.departement = departement
        self.typologie = typologie
        self.x_reglementaire = x_reglementaire
        self.y_reglementaire = y_reglementaire

    def __str__(self):
        return "%s" % self.nom
