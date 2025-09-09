

## Cookiecutter – instalacja i użycie
```bash
# Instalacja cookiecutter
pip install cookiecutter
# lub dla Pythona 3
pip3 install cookiecutter

# Utworzenie projektu z szablonu
python -m cookiecutter https://github.com/mateuszdorobek/cookiecutter-data-science-course
# lub
python3 -m cookiecutter https://github.com/mateuszdorobek/cookiecutter-data-science-course
````

## Git – sprawdzenie

```bash
# Windows
where git
# macOS/Linux
which git
```

## Interpreter i środowisko (venv/Conda)

* **Interpreter** → konkretna instalacja Pythona
* **Środowisko (venv/Conda)** → izolowana „piaskownica” z własnymi paczkami
* **Brak interpretera („No interpreter”)**:

  * Otwórz: `File → Settings → Project: <nazwa> → Python Interpreter`
  * Wybierz istniejący interpreter albo **Add Interpreter** → Virtualenv / Conda
* Interpreter można zmieniać później w tym samym miejscu

## Terminal i aktywacja środowiska

* Rodzaj terminala: `File → Settings → Tools → Terminal (Shell path)` (PowerShell / Command Prompt / Bash)
* PyCharm zwykle auto-aktywuje środowisko, ale można aktywować ręcznie:

```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

* Sprawdzenie:

```bash
python -V
# Windows
where python
# macOS/Linux
which python
```

## Instalacja bibliotek (pip)

* Pojedyncza paczka:

```bash
python -m pip install pandas
```

* Instalacja przez GUI: **Python Packages** (Shift+Shift → wpisz „Python Packages”)
* Pip doinstaluje zależności automatycznie
* Jeśli paczki trafiają do złego Pythona → upewnij się, że środowisko jest aktywne i używaj `python -m pip`

## Plik requirements.txt

```bash
# Instalacja wszystkiego z pliku
python -m pip install -r requirements.txt

# Utworzenie/aktualizacja pliku
python -m pip freeze > requirements.txt

# Aktualizacja paczek
python -m pip install -U -r requirements.txt
```

## Widok Project – kolory i „Mark Directory As”

* **Mark Directory As** (prawy klik na folderze):

  * *Sources Root* — kod źródłowy
  * *Tests* — testy
  * *Resource Root* — zasoby
  * *Excluded* — wykluczone z indeksowania
* Kolory folderów zmieniają się w panelu Project
* **External Libraries** → zewnętrzne zależności Pythona
* Szare elementy → wykluczone / nieindeksowane

## Szybkie wyszukiwanie (akcje, pakiety, Jupyter)

* **Search Everywhere**: `Shift + Shift` → np. „Jupyter”, „Python Packages”
* **Find Action**: `Ctrl + Shift + A` → dowolna akcja/ustawienie
* **Settings**: `Ctrl + Alt + S`
* Notebooki `.ipynb` w PyCharmie używają tego samego środowiska co projekt

## Mini-checklista przed uruchomieniem

*  Interpreter ustawiony (brak „No interpreter”)
*  Środowisko aktywne w terminalu (prefiks `(venv)`)
*  Paczki zainstalowane (`pip install -r requirements.txt` / GUI)
*  Folder z kodem = *Sources Root*
* **Run Configuration** wskazuje poprawny plik/skrypt i interpreter


