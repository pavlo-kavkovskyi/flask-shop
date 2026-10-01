from flask import Flask, abort, redirect, render_template, request, url_for

from models import Category, Product, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
db.init_app(app)

with app.app_context():
    db.create_all()
    if not Category.query.first():
        db.session.add_all(
            [Category(name=n) for n in ("laptopy", "akcesoria", "monitory", "inne")]
        )
        db.session.commit()


# ---------- Routes from materials 04-05 ----------
@app.route("/")
def index():
    return render_template("index.html", project="Sklep 4TP", user_name="Jan Kowalski")


@app.route("/about-us")
def about_us():
    return "Jesteśmy klasą 4 Technik Programista. Robimy sklep internetowy."


@app.route("/contact")
def contact():
    return "Napisz: sklep@example.com"


@app.route("/terms")
def terms():
    return "Regulamin sklepu: kupujesz, płacisz, odbierasz. Zwrot w 14 dni."


@app.route("/admin")
def admin():
    return "Brak dostępu", 403


@app.route("/api/info")
def api_info():
    return {"name": "flask-shop", "author": "Jan Kowalski", "version": "0.1"}


@app.route("/hello/<name>")
def hello(name):
    return f"Cześć, {name}!"


@app.route("/hello/<name>/<int:age>")
def hello_age(name, age):
    return f"Cześć, {name}, masz {age} lat"


@app.route("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    return f"{a} + {b} = {a + b}"


@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    return f"{a} - {b} = {a - b}"


@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    return f"{a} * {b} = {a * b}"


@app.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a / b}"


@app.route("/power/<int:a>/<int:b>")
def power(a, b):
    return f"{a} ^ {b} = {a**b}"


@app.route("/multiplication-table/<int:n>")
def multiplication_table(n):
    if not 1 <= n <= 20:
        return "n musi być z przedziału 1-20", 400
    return "<br>".join(f"{n} x {i} = {n * i}" for i in range(1, 11))


@app.route("/start")
def start():
    return redirect(url_for("product_list"))


# ---------- Material 07: CRUD ----------
def read_product_form():
    """Czyta pola formularza; przy złych danych kończy żądaniem 400."""
    try:
        name = request.form["name"].strip()
        price = float(request.form["price"].replace(",", "."))
        category_id = int(request.form["category_id"])
    except (KeyError, ValueError):
        abort(400)
    if not name or price < 0:
        abort(400)
    return name, price, category_id, "is_available" in request.form


@app.route("/products")
def product_list():
    q = request.args.get("q", "").strip()
    only_available = request.args.get("only_available") == "1"
    query = Product.query
    if only_available:
        query = query.filter_by(is_available=True)
    if q:
        query = query.filter(Product.name.contains(q))
    products = query.order_by(Product.name).all()
    return render_template(
        "products/list.html", products=products, q=q, only_available=only_available
    )


@app.route("/products/add", methods=["GET", "POST"])
def product_add():
    if request.method == "POST":
        name, price, category_id, is_available = read_product_form()
        product = Product(
            name=name, price=price, category_id=category_id, is_available=is_available
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("product_list"))
    return render_template(
        "products/form.html", product=None, categories=Category.query.all()
    )


@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("products/detail.html", product=product)


@app.route("/products/<int:product_id>/edit", methods=["GET", "POST"])
def product_edit(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        (
            product.name,
            product.price,
            product.category_id,
            product.is_available,
        ) = read_product_form()
        db.session.commit()
        return redirect(url_for("product_detail", product_id=product.id))
    return render_template(
        "products/form.html", product=product, categories=Category.query.all()
    )


@app.route("/products/<int:product_id>/delete", methods=["POST"])
def product_delete(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("product_list"))


if __name__ == "__main__":
    app.run(debug=True)
