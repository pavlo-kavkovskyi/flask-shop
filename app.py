from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)

# Dane tymczasowo w pamięci (lista słowników) – zalążek modelu
PRODUKTY = [
    {"id": 1, "nazwa": "Laptop", "cena": 2999.0, "kategoria": "laptopy", "dostepny": True},
    {"id": 2, "nazwa": "Mysz", "cena": 49.0, "kategoria": "akcesoria", "dostepny": False},
    {"id": 3, "nazwa": "Klawiatura", "cena": 199.0, "kategoria": "akcesoria", "dostepny": True},
    {"id": 4, "nazwa": "Monitor", "cena": 899.0, "kategoria": "monitory", "dostepny": True},
    {"id": 5, "nazwa": "Słuchawki", "cena": 149.0, "kategoria": "akcesoria", "dostepny": False},
]


@app.route("/")
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


# --- Zadanie 1: powitanie ---
@app.route("/czesc/<imie>")
def czesc(imie):
    return f"Cześć, {imie}!"


@app.route("/czesc/<imie>/<int:wiek>")
def czesc_wiek(imie, wiek):
    return f"Cześć, {imie}, masz {wiek} lat"


# --- Zadanie 2: kalkulator ---
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


# --- Zadanie 3: tabliczka mnożenia ---
@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    if not 1 <= n <= 20:
        return "n musi być z przedziału 1-20", 400
    wiersze = [f"{n} x {i} = {n * i}" for i in range(1, 11)]
    return "<br>".join(wiersze)


# --- Zadanie 4: query string ---
@app.route("/produkty")
def produkty():
    kat = request.args.get("kat")
    sort = request.args.get("sort")
    if kat is None and sort is None:
        return "wszystkie, domyślne"
    return f"Kategoria: {kat or 'wszystkie'}, sortowanie: {sort or 'domyślne'}"


# --- Mini-baza (materiał 05) i szczegóły w szablonie (materiał 06) ---
def znajdz_produkt(id):
    return next((p for p in PRODUKTY if p["id"] == id), None)


@app.route("/element/<int:id>")
def element(id):
    p = znajdz_produkt(id)
    if p is None:
        abort(404)
    return render_template("element.html", p=p)


@app.route("/elementy")
def elementy():
    return "<br>".join(f"{p['id']}. {p['nazwa']}" for p in PRODUKTY)


# --- Zadanie 6: przekierowanie ---
@app.route("/start")
def start():
    return redirect(url_for("index"))


# --- Materiał 06: lista, szukaj, dodaj ---
@app.route("/lista")
def lista():
    return render_template("lista.html", produkty=PRODUKTY)


@app.route("/szukaj")
def szukaj():
    q = request.args.get("q", "")
    wyniki = [p for p in PRODUKTY if q.lower() in p["nazwa"].lower()]
    return render_template("szukaj.html", q=q, wyniki=wyniki)


@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        nowy = {
            "id": max((p["id"] for p in PRODUKTY), default=0) + 1,
            "nazwa": request.form["nazwa"],
            "cena": float(request.form["cena"]),
            "kategoria": "inne",
            "dostepny": True,
        }
        PRODUKTY.append(nowy)
        return redirect(url_for("lista"))
    return render_template("dodaj.html")


if __name__ == "__main__":
    app.run(debug=True)
