from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

VAT_RATE = 0.23
VAT_MULTIPLIER = 1 + VAT_RATE


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Category {self.name}>"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", backref="products")

    def gross_price(self):
        return round(self.price * VAT_MULTIPLIER, 2)

    def __repr__(self):
        return f"<Product {self.name}>"
