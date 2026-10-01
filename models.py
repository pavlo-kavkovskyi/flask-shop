"""Modele bazy danych aplikacji sklepu (SQLAlchemy)."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# VAT 23% – stawka podstawowa; obniżone stawki na razie nieobsługiwane
VAT_RATE = 0.23
VAT_MULTIPLIER = 1 + VAT_RATE


class Category(db.Model):
    """Kategoria produktów (np. laptopy). Jedna kategoria – wiele produktów."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"<Category {self.name}>"


class Product(db.Model):
    """Produkt w sklepie.

    Cena przechowywana jako netto; brutto liczy gross_price().
    Produkt niedostępny (is_available=False) nie znika z bazy,
    tylko jest oznaczony na liście.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", backref="products")

    def gross_price(self) -> float:
        """Zwraca cenę brutto (netto + 23% VAT), zaokrągloną do groszy."""
        return round(self.price * VAT_MULTIPLIER, 2)

    def __repr__(self) -> str:
        return f"<Product {self.name}>"
