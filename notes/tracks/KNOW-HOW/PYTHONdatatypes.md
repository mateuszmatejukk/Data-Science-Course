# 🔹 Podstawowe typy w Pythonie

### Typy proste

* **`int`** – liczby całkowite

  ```python
  type(5)       # int
  ```

* **`float`** – liczby zmiennoprzecinkowe

  ```python
  type(0.5)     # float
  type(.5)      # float   # brak różnicy zapisu
  ```

* **`bool`** – wartości logiczne

  ```python
  type(True)    # bool
  type(False)   # bool
  ```

* **`None`** – brak wartości

  ```python
  type(None)    # NoneType
  ```

* **`str`** – napisy (łańcuchy znaków)

  ```python
  type("tekst") # str
  ```

---

# 🔹 Struktury danych (kontenery)

### Lista (`list`)

* Kolekcja elementów **edytowalna** (można zmieniać, dodawać, usuwać).
* Definicja:

  ```python
  my_list = [1, 2, 5]
  ```
* Może zawierać różne typy:

  ```python
  mixed = [1, "tekst", True, 3.14]
  ```

### Krotka (`tuple`)

* Podobna do listy, ale **niemodyfikowalna**.
* Definicja:

  ```python
  my_tuple = (1, 2, 5)
  ```

### Słownik (`dict`)

* Zbiór par **klucz → wartość**.
* Definicja:

  ```python
  my_dict = {"a": 1, "b": 2}
  ```

### Zbiór (`set`)

* Kolekcja **unikalnych elementów**.
* Definicja:

  ```python
  my_set = {1, 2, 2, 3}
  print(my_set)  # {1, 2, 3}
  ```

---

# 🔹 Funkcje

* W Pythonie **funkcje są obiektami** – można je przypisywać do zmiennych i przekazywać dalej.
* Definicja funkcji:

  ```python
  def add(a, b):
      return a + b

  wynik = add(2, 3)
  print(wynik)  # 5
  ```

---

# 🔹 Jupyter Notebook

### Kernel

* **Kernel** = "silnik" obliczeniowy.
* Zapamiętuje wartości zmiennych i uruchamia kod.
* Czasem trzeba zrobić **Restart Kernel + Run all cells**.

### Tryby pracy

* **Edit mode** – edycja treści komórki (zielona ramka).
* **Command mode** – operacje na komórkach (niebieska ramka).

### Format komórek

* **Kod** (`Code`)
* **Tekst** (`Markdown`)
* **Wyniki obliczeń**

---

# 🔹 Dodatkowe uwagi

* Notebooki mogą się **komunikować** i zapisywać wyniki między sobą.
* Istnieją różne interfejsy pracy: **terminal, UI, SSH**.
* Warto znać **parsowanie** i różnice w strukturach danych.

---
