---

## 1. Priorytet operatorów

Python wykonuje operacje zgodnie z **priorytetem (precedence)** i **kierunkiem (associativity)**.

### Najwyższy priorytet → najpierw wykonywane

1. **Nawiasy** `( )`

    * Zawsze wykonują się najpierw.

   ```python
   (2 + 3) * 4  # wynik 20, a nie 14
   ```

2. **Indeksowanie, wywołania funkcji, wycinanie (slicing)** `[ ]` / `()` / `[:]`

3. **Potęgowanie** `**`

    * Kierunek: **prawo → lewo**

   ```python
   2 ** 3 ** 2  # 2 ** (3 ** 2) = 2 ** 9 = 512
   ```

4. **Jednoargumentowe operatory**: `+x`, `-x`, `~x` (negacja bitowa)

5. **Mnożenie, dzielenie, modulo, dzielenie całkowite**: `*`, `/`, `//`, `%`

6. **Dodawanie i odejmowanie**: `+`, `-`

7. **Przesunięcia bitowe**: `<<`, `>>`

8. **Operatory bitowe AND**: `&`

9. **Operatory bitowe XOR i OR**: `^`, `|`

10. **Operatory porównania**: `==`, `!=`, `>`, `<`, `>=`, `<=`

11. **Operator logiczny NOT**: `not`

12. **Operator logiczny AND**: `and`

13. **Operator logiczny OR**: `or`

14. **Operator przypisania**: `=`, `+=`, `-=`, `*=`, `/=`, `**=` itd.

* Kierunek: **prawo → lewo**

---

## 2. Kluczowe punkty

1. Nawiasy **przebijają wszystko** – używaj ich, żeby uniknąć nieporozumień.
2. Operatory **potęgowania** są **prawo-lewo**.
3. Operatory **aritmetyczne** i **logiczne** mają różne priorytety.
4. Przy wątpliwościach używaj nawiasów – kod staje się czytelniejszy.

---

## 3. Przykłady

```python
x = 2 + 3 * 4
print(x)  # 14, bo * ma wyższy priorytet niż +

y = (2 + 3) * 4
print(y)  # 20, nawias zmienia kolejność

z = 2 ** 3 ** 2
print(z)  # 512, bo potęgowanie jest prawo → lewo

a = True or False and False
print(a)  # True, bo and ma wyższy priorytet niż or
```

---

## 4. Szybka ściągawka priorytetów (od najwyższego)

| Priorytet | Operatory / Akcje                      |   |
|-----------|----------------------------------------|---|
| 1         | `( )` nawiasy                          |   |
| 2         | `[]`, `[:]`, `()` (index, slice, call) |   |
| 3         | `**` potęgowanie                       |   |
| 4         | `+x, -x, ~x` (unary)                   |   |
| 5         | `* / // %`                             |   |
| 6         | `+ -`                                  |   |
| 7         | `<< >>`                                |   |
| 8         | `&`                                    |   |
| 9         | `^`                                    |   |
| 10        | `                                      | ` |
| 11        | `==, !=, >, <, >=, <=`                 |   |
| 12        | `not`                                  |   |
| 13        | `and`                                  |   |
| 14        | `or`                                   |   |
| 15        | `=, +=, -=, *=, /=, **=`               |   |

