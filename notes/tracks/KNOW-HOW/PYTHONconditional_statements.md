---

## 1. `if` Statement

* Służy do wykonywania kodu **tylko, jeśli warunek jest prawdziwy**.
* Składnia:

```python
if condition:
# blok kodu wykonywany, gdy condition == True
```

**Przykład:**

```python
x = 10
if x > 5:
    print("x jest większe niż 5")
```

**Wynik:**

```
x jest większe niż 5
```

---

## 2. `else` Statement

* Wykonuje kod **jeśli poprzedni warunek w `if` jest fałszywy**.
* Składnia:

```python
if condition:
# blok, gdy condition == True
else:
# blok, gdy condition == False
```

**Przykład:**

```python
x = 3
if x > 5:
    print("x jest większe niż 5")
else:
    print("x nie jest większe niż 5")
```

**Wynik:**

```
x nie jest większe niż 5
```

---

## 3. `elif` Statement

* Skrót od **else if** – sprawdza dodatkowe warunki, jeśli wcześniejsze `if`/`elif` były fałszywe.
* Składnia:

```python
if condition1:
# blok 1
elif condition2:
# blok 2
else:
# blok 3
```

**Przykład:**

```python
x = 5
if x > 10:
    print("x > 10")
elif x == 5:
    print("x równa się 5")
else:
    print("x < 10 i x != 5")
```

**Wynik:**

```
x równa się 5
```

---

## 4. Kluczowe punkty

1. **Bloki kodu są wcięte** (indentacja jest obowiązkowa).
2. `elif` jest opcjonalne – możesz mieć wiele `elif`.
3. `else` jest opcjonalne – ale może służyć jako "catch-all".
4. Warunki muszą być typu **bool** (True/False) – można używać operatorów porównania i logicznych:

    * Porównania: `==, !=, >, <, >=, <=`
    * Logiczne: `and, or, not`

---

## 5. Szybka ściągawka

| Konstrukcja | Co robi                                         | Przykład         | Wynik                     |
|-------------|-------------------------------------------------|------------------|---------------------------|
| if          | sprawdza warunek                                | if x > 5:        | wykonuje blok, jeśli True |
| elif        | sprawdza kolejny warunek, jeśli poprzedni False | elif x == 5:     | wykonuje blok, jeśli True |
| else        | wykonuje blok, jeśli wszystkie poprzednie False | else:            | wykonuje blok             |
| Operatory   | używane w warunkach                             | x > 5 and x < 10 | True lub False            |

---

