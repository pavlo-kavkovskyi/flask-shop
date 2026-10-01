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
