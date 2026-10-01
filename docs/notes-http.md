# Notatki: HTTP

## Kody odpowiedzi, które widziałem

| Kod | Nazwa | Gdzie widziałem |
|-----|-------|-----------------|
| 200 | OK | każda działająca strona, np. `/products` |
| 302 | Found | `redirect()` po POST, trasa `/start` |
| 304 | Not Modified | zakładka Network po odświeżeniu (cache) |
| 400 | Bad Request | `/divide/7/0` – dzielenie przez zero |
| 403 | Forbidden | trasa `/admin` |
| 404 | Not Found | `/products/999`, `abort(404)`, `get_or_404` |
| 405 | Method Not Allowed | POST na trasę bez `methods=["POST"]` |
| 500 | Internal Server Error | wyjątek w kodzie, np. `1 / 0` w trasie |

Reguła kciuka: **4xx** – popraw żądanie, **5xx** – popraw serwer.

## Metody HTTP

- **GET** – pobiera zasób; nie zmienia danych (bezpieczna, idempotentna).
- **POST** – tworzy zasób lub wykonuje akcję; nie jest idempotentny.
- **PUT** – zastępuje cały zasób; idempotentny.
- **PATCH** – zmienia część zasobu.
- **DELETE** – usuwa zasób; idempotentny.
- **HEAD** – jak GET, ale zwraca same nagłówki.
- **OPTIONS** – pyta, jakie metody obsługuje serwer (używane m.in. przez CORS).

Formularz HTML zna tylko GET i POST, dlatego usuwanie i edycja to u nas POST na osobny adres.

## Przykład: `abort(404)`

```python
from flask import abort

PRODUCTS = {1: "Laptop", 2: "Mysz"}


@app.route("/items/<int:item_id>")
def item_detail(item_id):
    if item_id not in PRODUCTS:
        abort(404)
    return PRODUCTS[item_id]
```
