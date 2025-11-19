# Przegląd auta
## Requirements 

- Dodawanie danych auta (marka, model, rok, przebieg)
- Sprawdzenie statusu oleju i przeglądu (ile tysięcy kilometów przejechanych bez wymiany)

```
python car_control.py
PODAJ DANE AUTA
Marka
> Opel
Model
> Zafira
...

WYNIK: POZYTYWNY
---- albo -----

WYNIK: Negatywny
- Za niski poziom oleju: 800mm (norma >900mm)
- Za niskie ciśnienie w oponach: 1.2PSI (norma >2PSI)
```

# Ocena mocy hasła

```python
MIN_PASS_LEN = 10

...

```

- dlugosc > 10 znakow
- conajmniej 4 cyfry
- musza byc i duze i male litery
- conajmniej jeden znak specjalny (nie cyfra i nie litera)

```
> python pass_checker.py
WPISZ HASLO:
wymagania:
- dlugosc > 10 znakow
- conajmniej 4 cyfry
- musza byc i duze i male litery
- conajmniej jeden znak specjalny (nie cyfra i nie litera)
> dupa123
HASLO ZA SLABE:
- dlugosc mniejsza niz 10 znakow
```