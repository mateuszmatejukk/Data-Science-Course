---

````markdown
Wyrażenia regularne (Regex) w Pythonie

Co to są wyrażenia regularne?

Wyrażenia regularne (regex) to wzorce (patterny), które pozwalają wyszukiwać, sprawdzać, dzielić lub zastępować fragmenty tekstu.

Przydają się m.in. do:
- wyszukiwania danych (np. e-maili, numerów telefonów),
- walidacji danych,
- czyszczenia tekstu,
- analizy logów lub plików tekstowych.

W Pythonie do obsługi regexów służy moduł **`re`**.

---

## Import modułu `re`

```python
import re
````

---

## Najważniejsze funkcje modułu `re`

| Funkcja         | Opis                                              | Przykład                                                           |
|-----------------|---------------------------------------------------|--------------------------------------------------------------------|
| `re.match()`    | Sprawdza dopasowanie **tylko na początku** tekstu | `re.match("abc", "abcdef")`                                        |
| `re.search()`   | Szuka wzorca **w dowolnym miejscu** tekstu        | `re.search("abc", "123abcdef")`                                    |
| `re.findall()`  | Zwraca **listę wszystkich dopasowań**             | `re.findall("\d+", "Mam 12 jabłek i 30 gruszek")` → `['12', '30']` |
| `re.finditer()` | Zwraca **iterowalny obiekt** dopasowań            | —                                                                  |
| `re.sub()`      | Zastępuje dopasowany tekst innym                  | `re.sub("\d+", "#", "abc123def")` → `'abc#def'`                    |
| `re.split()`    | Dzieli tekst wg wzorca                            | `re.split("\s+", "raz   dwa trzy")` → `['raz', 'dwa', 'trzy']`     |

---

## Najczęściej używane symbole w regex

| Wzorzec   | Znaczenie                               | Przykład                                |      |       |
|-----------|-----------------------------------------|-----------------------------------------|------|-------|
| `.`       | Dowolny znak (oprócz nowej linii)       | `a.c` → dopasuje `abc`, `axc`           |      |       |
| `^`       | Początek ciągu                          | `^Hello` → dopasuje `"Hello world"`     |      |       |
| `$`       | Koniec ciągu                            | `world$` → dopasuje `"Hello world"`     |      |       |
| `\d`      | Cyfra (0–9)                             | `\d\d` → dopasuje `42`                  |      |       |
| `\w`      | Znak słowa (litera, cyfra, podkreślnik) | `\w+` → `"hello_123"`                   |      |       |
| `\s`      | Spacja, tabulator lub inny biały znak   | `\s+` → `"   "`                         |      |       |
| `[aeiou]` | Jeden z wymienionych znaków             | dopasuje każdą samogłoskę               |      |       |
| `[^0-9]`  | Każdy znak **oprócz cyfr**              | —                                       |      |       |
| `a        | b`                                      | Alternatywa („albo”)                    | `kot | pies` |
| `( )`     | Grupowanie lub przechwytywanie          | `(ab)+` → `"abab"`                      |      |       |
| `?`       | 0 lub 1 wystąpienie                     | `kolou?r` → `"kolor"` lub `"kolour"`    |      |       |
| `*`       | 0 lub więcej wystąpień                  | `go*gle` → `"ggle"`, `"google"`         |      |       |
| `+`       | 1 lub więcej wystąpień                  | `go+gle` → `"google"`, ale nie `"ggle"` |      |       |
| `{m,n}`   | Od *m* do *n* powtórzeń                 | `\d{2,4}` → `99`, `2025`                |      |       |

---

## Przykład: wyszukiwanie adresów e-mail

```
import re

tekst = "Napisz na info@example.com lub support@mojastrona.org"
emaile = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", tekst)
print(emaile)
# Wynik: ['info@example.com', 'support@mojastrona.org']
```

---

## Przykład: walidacja numeru telefonu

```
import re

wzorzec = r"^\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
telefon = "+48 123 456 789"

if re.match(wzorzec, telefon):
    print("Poprawny numer telefonu!")
else:
    print("Niepoprawny numer.")
```

---

## Używaj **surowych łańcuchów** `r"..."`

Zawsze pisz wzorce jako **surowe stringi**, żeby `\` nie był traktowany jako znak specjalny w Pythonie.

Dobry zapis:

```python
re.search(r"\d+", "Wiek: 25")
```

Zły zapis:

```python
re.search("\\d+", "Wiek: 25")
```


