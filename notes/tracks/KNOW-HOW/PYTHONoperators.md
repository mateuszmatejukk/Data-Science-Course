---

# 1) Operatory arytmetyczne

| Operator   | Opis                          | Przykład      | Wynik |
| ---------- | ----------------------------- | ------------- | ----- |
| `+`        | dodawanie                     | `3 + 2`       | `5`   |
| `-`        | odejmowanie                   | `7 - 4`       | `3`   |
| `*`        | mnożenie                      | `6 * 4`       | `24`  |
| `/`        | dzielenie (zwraca `float`)    | `7 / 2`       | `3.5` |
| `//`       | dzielenie całkowite (podłoga) | `7 // 2`      | `3`   |
| `%`        | reszta z dzielenia            | `7 % 2`       | `1`   |
| `**`       | potęgowanie                   | `2 ** 3`      | `8`   |
| `-x`, `+x` | unarne minus/plus             | `-5`          | `-5`  |
| `()`       | nawiasy (priorytet)           | `(2 + 3) * 4` | `20`  |

**Przykłady:**

```python
a, b = 7, 2
print(a / b)  # 3.5
print(a // b)  # 3
print(a % b)  # 1
print((-7) // 2)  # -4  (podłoga w dół)
print(2 ** 10)  # 1024

print(2 + 3 * 4)  # 14  (najpierw mnożenie)
print((2 + 3) * 4)  # 20  (nawiasy zmieniają priorytet)
print(7.0 // 2)  # 3.0 (floor division działa też dla floatów)
print(7 // -2)  # -4
print(7 % -2)  # -1  (reszta ma znak dzielnika)
print(-7 % 2)  # 1
print(2 ** -3)  # 0.125 (ujemny wykładnik -> float)
print(-2 ** 3)  # -8    (potęgowanie przed unarnym minusem)
print((-2) ** 2)  # 4

```

---

# 2) Operatory logiczne: `and`, `or`, `not`

### Tabela prawdy dla `a`, `b` (bool)

| a     | b     | `a and b` | `a or b` | `not a` |
|-------|-------|-----------|----------|---------|
| False | False | False     | False    | True    |
| False | True  | False     | True     | True    |
| True  | False | False     | True     | False   |
| True  | True  | True      | True     | False   |

> `and` / `or` zwracają **ostatnio ewaluowany operand** (short-circuit), nie zawsze `bool`.

**Przykłady:**

```python
a, b = True, False
print(a and b)  # False
print(a or b)  # True
print(not a)  # False

print("" or "domyślna")  # "domyślna" ("" jest fałszywe)
print([] and 123)  # []        (pierwszy operand fałszywy)
print(10 and "ok")  # "ok"      (10 jest prawdziwe)

# Priorytety: not > and > or
print(True or False and False)  # True
print((True or False) and False)  # False

# Krótkie spięcie + domyślna wartość
name = ""
greeting = (name and "Cześć, " + name) or "Cześć!"
print(greeting)  # "Cześć!"

a, b, c = True, True, False
print(a and b and c)  # False
print(a or b or c)  # True
```

---

# 3) Operatory relacyjne (porównania)

`==`, `!=`, `<`, `<=`, `>`, `>=` — zwracają `bool`. Można **łańcuchować**: `1 < x < 5`.

**Przykłady:**

```python
print(3 == 3)  # True
print(3 != 4)  # True
print(2 < 5)  # True
print(5 >= 5)  # True

x = 3
print(1 < x < 5)  # True

# napisy porównywane leksykograficznie (Unicode)
print("ala" < "ola")  # True
print("Ala" < "ala")  # True  ('A' < 'a')

# Krotki porównują się element po elemencie:
print((1, 2) < (1, 3))  # True
print((1, 2, 9) > (1, 2))  # True

# Porównywanie nieporównywalnych typów:
try:
    1 < "1"
except TypeError as e:
    print(type(e).__name__)  # TypeError

# Uwaga na NaN:
nan1 = float("nan")
nan2 = float("nan")
print(nan1 == nan2)  # False
print(nan1 != nan2)  # True
```

---

# 4) Operatory przypisania

Podstawowy: `=`

Złożone: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, a także bitowe: `&=`, `|=`, `^=`, `<<=`, `>>=`.

**Przykłady:**

```python
x = 10
x += 5  # 15
x *= 2  # 30
x //= 4  # 7
x %= 3  # 1
x **= 5  # 1

# różnice dla typów mutowalnych/niemutowalnych
lst = [1, 2]
lst += [3]  # modyfikuje listę w miejscu -> [1, 2, 3]

tup = (1, 2)
tup += (3,)  # tworzy NOWY obiekt krotki -> (1, 2, 3)

# += na mutowalnych vs. "x = x + ...":
x = [1, 2];
y = x
x += [3]  # modyfikuje w miejscu
print(x, y)  # [1, 2, 3] [1, 2, 3]

x = [1, 2];
y = x
x = x + [3]  # tworzy nowy obiekt
print(x, y)  # [1, 2, 3] [1, 2]

# Słowniki (3.9+): unia/aktualizacja
d = {"a": 1}
d |= {"b": 2}
print(d)  # {'a': 1, 'b': 2}

# Zbiory:
s = {1, 2}
s |= {2, 3}  # unia
s &= {2, 3}  # przecięcie
s ^= {2}  # różnica symetryczna
print(s)  # {3}

# Operator przypisania-wyrażenia (walrus :=)
items = [1, 2, 3]
if (n := len(items)) > 2:
    print(n)  # 3
```

---

# 5) Operatory tożsamości: `is`, `is not`

Sprawdzają, czy dwie referencje wskazują **ten sam obiekt**. Używaj głównie do porównań z `None` i innymi singletonami.

**Przykłady:**

```python
x = None
print(x is None)  # True  (zalecany sposób)

a = [1, 2];
b = [1, 2]
print(a == b)  # True  (wartości równe)
print(a is b)  # False (różne obiekty)

# Nie używaj "is" do liczb/napisów — interning może mylić:
m = 256;
n = 256
print(m == n)  # True
# m is n -> może zależeć od implementacji; unikaj
```

---

# 6) Operatory przynależności (membership): `in`, `not in`

Sprawdzają obecność elementu w sekwencji/kolekcji/zbiorze lub klucz w słowniku.

**Przykłady:**

```python
print(3 in [1, 2, 3])  # True
print("a" in "Python")  # False
print("Py" in "Python")  # True (podciąg)
print("th" in "Python")  # True
print(5 not in [1, 2, 3])  # True

print(3 in range(10))  # True
print(3 in range(0, 10, 2))  # False (0,2,4,6,8)

print(2 in {1, 2, 3})  # True

d = {"x": 1, "y": 2}
print("x" in d)  # True  (sprawdza klucze)
print(1 in d.values())  # True
print(("x", 1) in d.items())  # True

pairs = [("py", 3), ("js", 2)]
print(("py", 3) in pairs)  # True
```

---

# 7) Operatory bitowe: `&`, `|`, `^`, `~`, `<<`, `>>`

**Przykłady:**

```python
print(5 & 3)  # 1   (0101 & 0011 = 0001)
print(5 | 2)  # 7   (0101 | 0010 = 0111)
print(5 ^ 1)  # 4   (0101 ^ 0001 = 0100)
print(~5)  # -6  (bitowa negacja: -(n+1))
print(1 << 3)  # 8   (przesunięcie w lewo)
print(8 >> 2)  # 2   (przesunięcie w prawo)

# Flagi uprawnień:
READ, WRITE, EXEC = 1 << 0, 1 << 1, 1 << 2
perm = READ | WRITE
print(bool(perm & EXEC))  # False
perm |= EXEC
print(bool(perm & EXEC))  # True
```

---

# 8) Dobre praktyki i pułapki

* Do porównania z `None` używaj **`is` / `is not`** (nie `==`).
* Priorytety: **`not` > `and` > `or`** — wątpliwości? Dodaj nawiasy.

