from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Kategoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Kategoria {self.nazwa}>"


class Produkt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    cena = db.Column(db.Float, nullable=False)
    dostepny = db.Column(db.Boolean, default=True)
    kategoria_id = db.Column(db.Integer, db.ForeignKey("kategoria.id"))
    kategoria = db.relationship("Kategoria", backref="produkty")

    def cena_brutto(self):
        return round(self.cena * 1.23, 2)

    def __repr__(self):
        return f"<Produkt {self.nazwa}>"
