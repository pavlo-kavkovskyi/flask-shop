# flask-shop

Sklep internetowy w Flasku (Flask + SQLAlchemy + SQLite) – projekt z zajęć, klasa 4 Technik Programista.

## Technologie

- Python 3.12, Flask 3, Flask-SQLAlchemy
- SQLite
- Jinja2, CSS

## Uruchomienie

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Aplikacja: http://localhost:5000

## Struktura

```text
app.py            – konfiguracja i widoki (kontrolery)
models.py         – modele SQLAlchemy (Product, Category)
templates/        – szablony Jinja2 (base.html, index.html, products/*.html)
static/           – CSS
instance/shop.db  – baza SQLite (poza repozytorium)
mvc.md            – notatki MVC/MTV
```

### Warstwy MVC → pliki

| Warstwa MVC | U nas | Plik |
|-------------|-------|------|
| Model | klasy `db.Model` + metody z logiką (`gross_price`) | `models.py` |
| View | szablony Jinja2 | `templates/**/*.html` |
| Controller | funkcje z `@app.route` | `app.py` |

## Trasy

| Metoda | Adres | Opis | Możliwe kody |
|--------|-------|------|--------------|
| GET | `/` | strona główna | 200 |
| GET | `/about-us`, `/contact`, `/terms` | teksty statyczne | 200 |
| GET | `/admin` | brak dostępu | 403 |
| GET | `/api/info` | JSON: name, author, version | 200 |
| GET | `/hello/<name>`, `/hello/<name>/<int:age>` | powitanie; `age` nie-liczba → 404 | 200, 404 |
| GET | `/add`, `/subtract`, `/multiply`, `/divide`, `/power` + `/<int:a>/<int:b>` | kalkulator | 200, 400 (dzielenie przez 0), 404 |
| GET | `/multiplication-table/<int:n>` | tabliczka; `n` poza 1–20 → 400 | 200, 400 |
| GET | `/start` | redirect na `/products` | 302 |
| GET | `/products` | lista z bazy; `?q=`, `?only_available=1` | 200 |
| GET/POST | `/products/add` | dodawanie; po POST redirect | 200, 302, 400 |
| GET | `/products/<id>` | szczegóły | 200, 404 |
| GET/POST | `/products/<id>/edit` | edycja; po POST redirect na szczegóły | 200, 302, 400, 404 |
| POST | `/products/<id>/delete` | usuwanie; po POST redirect | 302, 404, 405 (GET) |

## Test CRUD

Komendy do wykonania w `flask shell` (venv aktywny). Przebieg sesji wklej poniżej:

```python
from models import db, Product, Category
c = Category.query.first()
db.session.add_all([Product(name="Laptop", price=2999.99, category=c),
                    Product(name="Mysz", price=49, category=c),
                    Product(name="Monitor", price=899, category=c)])
db.session.commit()
Product.query.all()                       # read
p = Product.query.get(1); p.price = 2799  # update
db.session.commit()
db.session.delete(Product.query.get(2))   # delete
db.session.commit()
```

```text
(tu wklej wynik z własnego terminala)
```

## Zepsuj i napraw

Celowa literówka `retrun` zamiast `return`. Python nie uruchomił aplikacji
i wypisał w terminalu:

```text
  File "app.py", line 5
    retrun "Hello"
           ^^^^^^^
SyntaxError: invalid syntax
```

To błąd składni wykryty, zanim kod ruszył, więc debugger w przeglądarce się nie pojawił
(nie było strony do pokazania). Po poprawieniu na `return` wszystko działa.

## Autor

Jan Kowalski, 4TP

## Kody odpowiedzi HTTP (zadanie 4, materiał 08)

Tabela adres → metoda → kod. Wartości sprawdź w F12 → Network.

| Adres | Metoda | Kod | Dlaczego |
|-------|--------|-----|----------|
| `/products` | GET | 200 | działająca strona |
| `/start` | GET | 302 | `redirect()` na `/products` (potem drugie żądanie 200) |
| `/products/999` | GET | 404 | `get_or_404` – nie ma takiego produktu |
| `/about-us` | POST | 405 | trasa istnieje, ale bez `methods=["POST"]` |
| `/divide/7/0` | GET | 400 | dzielenie przez zero – złe żądanie |
| `/admin` | GET | 403 | zwracamy 403 celowo |
| `/boom` (tymczasowa trasa z `1 / 0`) | GET | 500 | wyjątek w kodzie serwera – po sprawdzeniu trasę usuń |

Dla 500 dopisz na chwilę trasę `@app.route("/boom")` z `return str(1 / 0)`, odśwież, zobacz
traceback, potem ją usuń (naprawa = usunięcie błędnego kodu).

## Bezpieczny GET (zadanie 5)

W projekcie żaden GET nie zmienia danych: dodawanie, edycja i usuwanie idą przez POST.
To ważne, bo roboty indeksujące, podglądy linków w komunikatorach i prefetch przeglądarki
wysyłają GET bez pytania – link `<a href="/usun/5">` mógłby wtedy skasować produkt.

## Ruff (zadanie 2)

```text
ruff check .   – znalazł: (wpisz liczbę i rodzaje problemów)
ruff format .  – (wpisz, czy coś zmienił)
```

## Definition of Done

- [ ] Aplikacja uruchamia się z czystego klonu: `pip install -r requirements.txt`, `python app.py` *(do sprawdzenia na czystym klonie)*
- [x] Nazwy zmiennych, funkcji, klas, tras – po angielsku, zgodnie z PEP 8
- [ ] `ruff check .` nie zgłasza błędów, `ruff format .` nic nie zmienia *(do uruchomienia lokalnie)*
- [x] Każda funkcja widoku i każdy model ma docstring
- [x] Nowe funkcje mają type hints
- [x] Żaden GET nie zmienia danych (usuwanie, dodawanie = POST)
- [x] Po każdym POST jest redirect
- [x] Nieistniejący zasób daje 404, złe dane 400 – nie 500
- [x] `.gitignore` obejmuje `venv/`, `instance/`, `*.db`, `__pycache__/`, `.env`
- [x] README: co to, jak uruchomić, struktura, tabela tras
- [x] Commity małe, po angielsku, według konwencji
- [ ] Umiesz wyjaśnić każdą linię – także tę, którą napisał LLM *(Twoja odpowiedzialność)*
