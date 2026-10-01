from flask import Flask, abort, redirect, request, url_for

app = Flask(__name__)

# Mini-baza w słowniku (zadanie 5) – zalążek modelu
PRODUKTY = {
    1: "Laptop",
    2: "Mysz",
    3: "Klawiatura",
    4: "Monitor",
    5: "Słuchawki",
}


@app.route("/")
def index():
    return "Hello World! Tu Jan Kowalski, sklep 4TP."


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


# --- Zadanie 5: mini-baza w słowniku ---
@app.route("/element/<int:id>")
def element(id):
    if id not in PRODUKTY:
        abort(404)
    return f"Produkt: {PRODUKTY[id]}"


@app.route("/elementy")
def elementy():
    return "<br>".join(f"{i}. {nazwa}" for i, nazwa in PRODUKTY.items())


# --- Zadanie 6: przekierowanie ---
@app.route("/start")
def start():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
