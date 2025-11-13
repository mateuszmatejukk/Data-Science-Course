---

## 1. `split()`

* Rozdziela string na **listę podłańcuchów** według separatora.
* Składnia: `string.split(separator, maxsplit)`

    * `separator` – znak lub ciąg znaków, po którym dzielimy string (domyślnie spacja `" "`).
    * `maxsplit` – maksymalna liczba podziałów (opcjonalne).

**Przykłady:**

text = "apple,banana,cherry"

* Domyślny separator (spacja):

```python
"Hello world".split() → ['Hello', 'world']
```

* Separator przecinek `,`:

```python
text.split(',') → ['apple', 'banana', 'cherry']
```

* Ograniczenie liczby podziałów:

```python
text.split(',', 1) → ['apple', 'banana,cherry']
```

---

## 2. `join()`

* Łączy elementy listy **w jeden string**, wstawiając separator między elementami.
* Składnia: `separator.join(iterable)`

**Przykłady:**

fruits = ['apple', 'banana', 'cherry']

* Separator przecinek:

```python
','.join(fruits) → 'apple,banana,cherry'
```

* Separator spacja:

```python
' '.join(fruits) → 'apple banana cherry'
```

* Separator znak `-`:

```python
'-'.join(fruits) → 'apple-banana-cherry'
```

---

## 3. Kluczowe punkty

1. `split()` → string → lista
2. `join()` → lista → string
3. Separator w `split()` znika, separator w `join()` jest wstawiany między elementami.
4. Jeśli separator nie jest podany w `split()`, dzieli po **białych znakach**.
5. `join()` działa tylko na **iterable**, którego elementy są **stringami**.

---

## 4. Szybka ściągawka

| Metoda          | Co robi                        | Przykład                    | Wynik             |
|-----------------|--------------------------------|-----------------------------|-------------------|
| `split()`       | dzieli string na listę         | `"a b c".split()`           | `['a', 'b', 'c']` |
| `split(sep)`    | dzieli po separatorze          | `"a,b,c".split(',')`        | `['a', 'b', 'c']` |
| `split(sep, n)` | dzieli maksymalnie n razy      | `"a,b,c".split(',', 1)`     | `['a', 'b,c']`    |
| `join()`        | łączy listę elementów w string | `','.join(['a', 'b', 'c'])` | `'a,b,c'`         |
| `join()`        | z innym separatorem            | `' '.join(['a', 'b', 'c'])` | `'a b c'`         |

---


