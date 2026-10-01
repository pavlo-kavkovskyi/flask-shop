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
