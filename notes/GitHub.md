## Podstawy GitHub

1. **Visibility**
2. **README (opis)**
3. **.gitignore** – pliki, które nie są śledzone w repozytorium
4. **License**

🔹 *JetBrains Toolbox*
🔹 *Zapewnić dostęp użytkownikom*

---

## Git – podstawowe pojęcia

* **commit** – zapisanie zmian
* **branch / branch master** – gałęzie projektu
* **merge / pull request** – łączenie gałęzi
* **git add** – dodanie plików do commita

---

## Klonowanie i praca z repozytorium

```bash
git clone <repo_url>
git checkout <branch_name>
```

* Możliwość wersji równoległych projektu (branch).
* **merge** – łączenie gałęzi.
* **pull request (PR)** – propozycja zmian w repozytorium.

---

## Git lokalnie

* Do zarządzania kodem lokalnie:

  ```bash
  git pull
  ```
* **CTRL + T** (skrót w terminalu).

---

## Commit i pliki

* **Universal files**
* Każdy commit powinien mieć opis (np. `.env`, `password` – nie commitować!).
* **Initial commit** – pierwszy commit.
* Zmiany zapisujemy w terminalu.
* Ostatecznie wysyłamy je na GitHub.

---

## Setup – konfiguracja

1. Wejść do folderu z repozytorium.

2. Sprawdzić status:

   ```bash
   git status
   ```

3. Historia commitów:

   ```bash
   git log
   ```

   * ID commita
   * autor
   * data

4. Ustawienie remote:

   ```bash
   git remote add origin <repo_url>
   ```

---

## Połączenie z GitHub

* Przez **browser (szybko)**
* Lub przez **token (GitHub → wygenerować → wkleić)**

---

## Dodatkowe

* **git diff** – podgląd zmian przed commitem.
* Testy dokumentacji – opis w commitach.

---

