# flask-shop

Sklep internetowy w Flasku – projekt z zajęć (klasa 4 Technik Programista).

## Uruchomienie

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Aplikacja: http://localhost:5000

## Trasy (materiał 05)

| Adres (przykład) | Opis |
|------------------|------|
| `/czesc/Ania` | powitanie; `/czesc/Ania/17` – z wiekiem, `/czesc/Ania/abc` → 404 (konwerter `int`) |
| `/dodaj/2/3`, `/odejmij/7/2`, `/pomnoz/3/4`, `/potega/2/10` | kalkulator |
| `/podziel/7/2` | dzielenie; `/podziel/7/0` → 400 |
| `/tabliczka/7` | tabliczka mnożenia; `n` poza 1–20 → 400 |
| `/produkty?kat=laptopy&sort=cena` | query string; bez parametrów: „wszystkie, domyślne” |
| `/element/2` | element ze słownika; `/element/99` → 404 (`abort`) |
| `/elementy` | lista wszystkich elementów |
| `/start` | redirect 302 na `/` |

## Struktura folderów

```text
flask-shop/
├── app.py            <- konfiguracja + kontrolery (trasy)
├── models.py         <- modele SQLAlchemy (Produkt, Kategoria)
├── templates/        <- szablony Jinja2 (widoki)
├── static/           <- style.css
├── instance/sklep.db <- baza SQLite (poza repozytorium)
├── mvc.md
├── requirements.txt
└── README.md
```

## Warstwy MVC → pliki

| Warstwa MVC | U nas | Plik |
|-------------|-------|------|
| Model | klasy `db.Model` + metody z logiką (`cena_brutto`) | `models.py` |
| View | szablony Jinja2 | `templates/*.html` |
| Controller | funkcje z `@app.route` | `app.py` |

## Trasy (materiał 06)

| Metoda | Adres | Opis |
|--------|-------|------|
| GET | `/` | strona główna (szablon z `projekt` i `imie`) |
| GET | `/lista` | tabela produktów, niedostępne wyróżnione; pusta lista → komunikat |
| GET | `/element/<id>` | szczegóły; brak id → 404 |
| GET | `/szukaj?q=` | wyszukiwarka po nazwie, liczba wyników |
| GET/POST | `/dodaj` | formularz dodawania; po POST redirect (302) na `/lista` |

## Trasy (materiał 07 – baza danych)

| Metoda | Adres | Opis |
|--------|-------|------|
| GET | `/` | lista z bazy, posortowana po nazwie; `?q=` szuka, `?tylko_dostepne=1` filtruje |
| GET | `/element/<id>` | szczegóły; brak → 404 (`get_or_404`) |
| GET/POST | `/dodaj` | dodawanie, po POST redirect |
| GET/POST | `/edytuj/<id>` | edycja, po POST redirect na szczegóły |
| POST | `/usun/<id>` | usuwanie (POST, nie link GET), po POST redirect |

## Test CRUD

Komendy do wykonania w `flask shell` (venv aktywny). Przebieg sesji wklej poniżej:

```python
from models import db, Produkt, Kategoria
k = Kategoria.query.first()
db.session.add_all([Produkt(nazwa="Laptop", cena=2999.99, kategoria=k),
                    Produkt(nazwa="Mysz", cena=49, kategoria=k),
                    Produkt(nazwa="Monitor", cena=899, kategoria=k)])
db.session.commit()
Produkt.query.all()                       # read
p = Produkt.query.get(1); p.cena = 2799   # update
db.session.commit()
db.session.delete(Produkt.query.get(2))   # delete
db.session.commit()
```

```text
(tu wklej wynik z własnego terminala)
```

## Zepsuj i napraw (zadanie 6, materiał 04)

Celowa literówka `retrun` zamiast `return`. Python nie uruchomił aplikacji
i wypisał w terminalu:

```text
  File "app.py", line 5
    retrun "Hello"
           ^^^^^^^
SyntaxError: invalid syntax
```

To błąd składni – wykryty, zanim kod w ogóle ruszył, więc debugger w przeglądarce
się nie uruchomił (nie ma strony do wyświetlenia). Po poprawieniu na `return` wszystko działa.

## Autor

Jan Kowalski, 4TP
