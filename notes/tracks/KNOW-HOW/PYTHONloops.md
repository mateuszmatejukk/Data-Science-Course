---

## 1. `for` Loop

* Służy do iterowania po **sekwencjach** (listy, stringi, range, itp.).
* Składnia:

```python
for variable in sequence:
# blok kodu do wykonania w każdej iteracji
```

**Przykłady:**

Iterowanie po liście:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Wynik:**

```
apple
banana
cherry
```

Iterowanie po zakresie liczb:

```python
for i in range(5):  # 0,1,2,3,4
    print(i)
```

**Wynik:**

```
0
1
2
3
4
```

---

## 2. `while` Loop

* Wykonuje blok kodu **dopóki warunek jest prawdziwy**.
* Składnia:

```python
while condition:
# blok kodu do wykonania
```

**Przykład:**

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

**Wynik:**

```
0
1
2
3
4
```

---

## 3. Kontrola pętli

* `break` – przerywa pętlę całkowicie.
* `continue` – pomija **bieżącą iterację**, przechodzi do następnej.
* `else` – w Pythonie pętla `for` lub `while` może mieć blok `else`, który wykona się **jeśli pętla nie została
  przerwana `break`**.

**Przykład z `break` i `else`:**

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Pętla zakończona bez break")
```

**Wynik:**

```
0
1
2
```

(`else` się nie wykonało, bo był `break`)

---

## 4. Kluczowe punkty

1. `for` → iteruje po sekwencjach lub range.
2. `while` → iteruje dopóki warunek jest True.
3. `break` → natychmiast kończy pętlę.
4. `continue` → pomija bieżącą iterację.
5. Pętle mogą mieć opcjonalny `else`, wykonywany **tylko, gdy nie użyto `break`**.

---

## 5. Szybka ściągawka

| Pętla       | Co robi                                        | Przykład                    | Wynik                            |
|-------------|------------------------------------------------|-----------------------------|----------------------------------|
| for         | iteruje po sekwencji                           | for x in [1,2,3]:           | 1 2 3                            |
| while       | iteruje dopóki warunek jest True               | while x < 3:                | 0 1 2                            |
| break       | przerywa pętlę                                 | if x==2: break              | kończy pętlę wcześniej           |
| continue    | pomija bieżącą iterację                        | if x==2: continue           | przechodzi do następnej iteracji |
| else (loop) | wykona się jeśli pętla zakończy się naturalnie | for x in range(3): ... else | wykonuje else jeśli brak break   |

---


