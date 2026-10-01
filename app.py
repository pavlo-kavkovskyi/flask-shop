from flask import Flask, redirect, render_template, request, url_for

from models import Kategoria, Produkt, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sklep.db"
db.init_app(app)


with app.app_context():
    db.create_all()
    if not Kategoria.query.first():
        db.session.add_all(
            [Kategoria(nazwa=n) for n in ("laptopy", "akcesoria", "monitory", "inne")]
        )
        db.session.commit()


# ---------- Trasy z materiałów 04-05 ----------
@app.route("/witaj")
def index():
    return render_template("index.html", projekt="Sklep 4TP", imie="Jan Kowalski")


@app.route("/o-nas")
def o_nas():
    return "Jesteśmy klasą 4 Technik Programista. Robimy sklep internetowy."


@app.route("/kontakt")
def kontakt():
    return "Napisz: sklep@example.com"


@app.route("/regulamin")
def regulamin():
    return "Regulamin sklepu: kupujesz, płacisz, odbierasz. Zwrot w 14 dni."


@app.route("/admin")
def admin():
    return "Brak dostępu", 403


@app.route("/api/info")
def api_info():
    return {"nazwa": "flask-shop", "autor": "Jan Kowalski", "wersja": "0.1"}


@app.route("/czesc/<imie>")
def czesc(imie):
    return f"Cześć, {imie}!"


@app.route("/czesc/<imie>/<int:wiek>")
def czesc_wiek(imie, wiek):
    return f"Cześć, {imie}, masz {wiek} lat"


@app.route("/dodaj/<int:a>/<int:b>")
def dodaj_liczby(a, b):
    return f"{a} + {b} = {a + b}"


@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a, b):
    return f"{a} - {b} = {a - b}"


@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a, b):
    return f"{a} * {b} = {a * b}"


@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a / b}"


@app.route("/potega/<int:a>/<int:b>")
def potega(a, b):
    return f"{a} ^ {b} = {a**b}"


@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    if not 1 <= n <= 20:
        return "n musi być z przedziału 1-20", 400
    return "<br>".join(f"{n} x {i} = {n * i}" for i in range(1, 11))


@app.route("/start")
def start():
    return redirect(url_for("lista"))


# ---------- Materiał 07: CRUD na bazie ----------
@app.route("/")
def lista():
    q = request.args.get("q", "").strip()
    tylko_dostepne = request.args.get("tylko_dostepne") == "1"
    zapytanie = Produkt.query
    if tylko_dostepne:
        zapytanie = zapytanie.filter_by(dostepny=True)
    if q:
        zapytanie = zapytanie.filter(Produkt.nazwa.contains(q))
    produkty = zapytanie.order_by(Produkt.nazwa).all()
    return render_template(
        "lista.html", produkty=produkty, q=q, tylko_dostepne=tylko_dostepne
    )


@app.route("/element/<int:id>")
def szczegoly(id):
    p = Produkt.query.get_or_404(id)
    return render_template("element.html", p=p)


@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        p = Produkt(
            nazwa=request.form["nazwa"],
            cena=float(request.form["cena"]),
            kategoria_id=int(request.form["kategoria_id"]),
            dostepny="dostepny" in request.form,
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("lista"))
    return render_template("dodaj.html", kategorie=Kategoria.query.all())


@app.route("/edytuj/<int:id>", methods=["GET", "POST"])
def edytuj(id):
    p = Produkt.query.get_or_404(id)
    if request.method == "POST":
        p.nazwa = request.form["nazwa"]
        p.cena = float(request.form["cena"])
        p.kategoria_id = int(request.form["kategoria_id"])
        p.dostepny = "dostepny" in request.form
        db.session.commit()
        return redirect(url_for("szczegoly", id=p.id))
    return render_template("edytuj.html", p=p, kategorie=Kategoria.query.all())


@app.route("/usun/<int:id>", methods=["POST"])
def usun(id):
    p = Produkt.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for("lista"))


if __name__ == "__main__":
    app.run(debug=True)
