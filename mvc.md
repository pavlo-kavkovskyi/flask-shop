# Notatki MVC / MTV

Domena projektu: **sklep internetowy**.

## Zadanie 1: Podział na warstwy

| Warstwa | Elementy |
|---------|----------|
| Model | `Produkt`, `Koszyk`, obliczanie rabatu / ceny brutto |
| Widok | strona listy produktów, strona koszyka, e-mail z potwierdzeniem zamówienia |
| Kontroler | obsługa `/produkty`, `/koszyk/dodaj`, `/zamow` |

## Zadanie 2: Gdzie jest błąd?

1. **Szablon HTML wykonuje zapytanie SQL** – widok robi robotę modelu (pobieranie danych). Dane powinien pobrać kontroler przez model i przekazać gotowe do szablonu.
2. **Funkcja `/zamow` ma 150 linii** (stan magazynu, VAT, PDF, mail) – kontroler robi robotę modelu (reguły biznesowe) i widoku (PDF, mail). Kontroler ma być cienki.
3. **Klasa `Produkt` ma metodę `wyswietl_jako_html()`** – model robi robotę widoku. Model nie wie, że istnieje HTML.

## Zadanie 3: Przepływ żądania `POST /koszyk/dodaj` (produkt nr 7)

```text
PRZEGLĄDARKA
  | 1. POST /koszyk/dodaj  (produkt_id=7)
  v
CONTROLLER (funkcja koszyk_dodaj)
  | 2. daj mi produkt nr 7 i dodaj go do koszyka
  v
MODEL -- 3. SELECT ... WHERE id=7 --> BAZA DANYCH
  |        (sprawdza dostępność, zapisuje pozycję koszyka: INSERT)
  | 4. obiekt Produkt(nazwa='Mysz') + zaktualizowany Koszyk
  v
CONTROLLER
  | 5. redirect na stronę koszyka (wzorzec PRG), potem GET /koszyk
  v
VIEW (szablon koszyka + dane z modelu = gotowa strona)
  | 6. HTML
  v
PRZEGLĄDARKA
```

- **Kontroler**: odbiera POST, czyta `produkt_id`, woła model, robi redirect.
- **Model**: pyta bazę o produkt nr 7, sprawdza dostępność, zapisuje pozycję.
- **Widok** (po redirectcie): dostaje obiekt koszyka z listą pozycji i wyświetla go.

## Zadanie 4: Słownik

| Framework | Model | Widok (prezentacja) | Kontroler |
|-----------|-------|---------------------|-----------|
| Django | `models.py` | `templates/*.html` | `views.py` + `urls.py` |
| ASP.NET Core | `Models/` | `Views/*.cshtml` | `Controllers/*Controller.cs` |
| Flask | klasy `db.Model` (SQLAlchemy), sam piszesz | szablony Jinja2 w `templates/` | funkcje z `@app.route` |

> Uwaga: `View` w Django to `Controller` z MVC.
