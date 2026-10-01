# flask-shop

Sklep internetowy: Flask + SQLAlchemy + SQLite. Projekt szkolny (klasa 4 Technik Programista).

## Technologie

- Python 3.12, Flask 3, Flask-SQLAlchemy
- SQLite, Jinja2, CSS
- Ruff (formatowanie i lint)

## Zasady

1. Nazwy zmiennych, funkcji, klas, tras i plików po angielsku, zgodnie z PEP 8.
2. Przed każdym commitem uruchom `ruff check .` i `ruff format .`.
3. Każdy model i każda funkcja widoku ma docstring; nowe funkcje mają type hints.
4. Nie dodawaj nowych pakietów bez pytania.
5. GET nigdy nie zmienia danych; po każdym POST robimy redirect.
6. Commity po angielsku, według Conventional Commits (`feat:`, `fix:`, `docs:`, ...).
