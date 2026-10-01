from flask import Flask

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
