---

## 1. String Indexing

* String to sekwencja znaków.
* Każdy znak ma **indeks**:

    * Liczenie od początku: 0, 1, 2, …
    * Liczenie od końca: -1, -2, -3, …

Przykład:

text = "Python"

### Indeksy:

P y t h o n
0 1 2 3 4 5 ← indeksy od początku
-6 -5 -4 -3 -2 -1 ← indeksy od końca

Przykłady użycia:

* text[0] → 'P'
* text[3] → 'h'
* text[-1] → 'n'
* text[-2] → 'o'

---

## 2. String Slicing

* Wyciąganie podłańcucha (substring) ze stringa.
* Składnia: string[start:stop:step]

    * start – indeks początkowy (włącznie)
    * stop – indeks końcowy (wyłącznie)
    * step – co ile znaków pobierać, domyślnie 1

Przykłady:

text = "Python"

text[0:4] → 'Pyth'
text[2:] → 'thon'
text[:4] → 'Pyth'
text[:] → 'Python'
text[-4:-1] → 'tho'
text[::2] → 'Pto'
text[::-1] → 'nohtyP'

---

## 3. Kluczowe punkty

1. Indeksowanie zaczyna się od 0.
2. Indeksy ujemne liczą od końca (-1 = ostatni znak).
3. W slicing’u start włącznie, stop wyłącznie.
4. Pominięcie start → od początku, pominięcie stop → do końca.
5. step może być ujemny → odwraca kolejność.
6. Stringi są **niemodyfikowalne** (immutable).

---

## 4. Szybka ściągawka

| Składnia    | Znaczenie               | Przykład   | Wynik    |
|-------------|-------------------------|------------|----------|
| text[i]     | pojedynczy znak         | text[0]    | 'P'      |
| text[i:j]   | podłańcuch od i do j-1  | text[0:3]  | 'Pyt'    |
| text[i:]    | od i do końca           | text[2:]   | 'thon'   |
| text[:j]    | od początku do j-1      | text[:4]   | 'Pyth'   |
| text[:]     | cały string             | text[:]    | 'Python' |
| text[i:j:k] | co k znaków od i do j-1 | text[::2]  | 'Pto'    |
| text[::-1]  | odwrócenie stringa      | text[::-1] | 'nohtyP' |

