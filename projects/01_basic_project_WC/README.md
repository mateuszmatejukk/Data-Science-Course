# Losowanie Liczb i zgadywanie

Losowanie liczb 1-10 i możliwość zgadywania prze użytkownika jaka się wylosowała i info czy ZGADŁ czy NIE.

biblioteka wbudowana random

```python
import random

x = random.randint()  # to nie jest tak
```

Case 1

```
> DrawingNumbers.py
> This program generates a random number and let you guess it
> Give a number from 1 to 10 or press 'Q' to exit
> 8
> This number is too big try again!
> 5
> Congratulations, you guessed it!
```

Case 2

```
> python sciprt.py
WYLOSOWAŁEM LICZBĘ - ZGADNIJ JAK (1-10) - naciśnij "Q" aby zakończyć:
> 3
NIE
> 5
NIE
> Q
You exit, my number was 7
```

# Kalkulator

```
>Calculator.py
WYBIERZ OPERACJE
  1) dodawanie
  2) ojemowanie
  3) mnozenie
  4) dzielenie
  Q) wyjście
...

> 5
PODAJ MI DWA ELEMENTY DO "dzielenie":
> 9
> 0
NIE DZIEL CHOLERO PRZEZ ZERO!
PODAJ MI DWA ELEMENTY DO "dzielenie":
> 4
> 2
WYNIK: 2.0
WYBIERZ OPERACJE
  1) dodawanie
  2) ojemowanie
  3) mnozenie
  4) dzielenie
  Q) wyjście
```

# QUIZ - Milionerzy

[//]: # (TODO: napisz wymagania - przykładową interakcję)

- odpowiadasz na pytanie albo pasujesz
- (opt) 50/50 pytań
- najpierw zrób te wcześniejsze.

> Millionaires.py

Case 1

```
>Pytanie 1.: W ilu stopnia Celsjusza woda wrze?
> a) 90
> b) 95
> c) 100
> d) 105
> Czy chcesz skorzysta z 50/50?
> nie
> W takim razie czekam na odpowiedz
> c
> Gratulacje! Wygrałeś 1 000 zł
> Grasz dalej czy zabierasz wygraną 
> gram 
> Grasz o gwarantowane 2 000 zł. 
> Pytanie 2.: W którym roku miała miejsce bitwa pod Waterloo?
> a) 1795
> b) 1815
> c) 1813
> d) 1805
> Czy chcesz skorzysta z 50/50?
> nie
> W takim razie czekam na odpowiedz
> d
> Grasz o 5 000 zł. 
> Pytanie 3.: W którym roku miała miejsce bitwa pod Grunwaldem?
> a) 996
> b) 1515
> c) 1410
> d) 1485
> Czy chcesz skorzysta z 50/50?
> nie
> c
> Gratulacje! Wygrałeś 5 000 zł
> Grasz o 10 000 zł. 
> Pytanie 4.: W którym roku wybuchła 2. wojna światowa?
> a) 1945
> b) 1933
> c) 1936
> d) 1939
> Czy chcesz skorzysta z 50/50?
> nie
> c
> Zła odpowiedz! Wygrałeś 2 000 zł!
```

Case 2

```
>Pytanie 1.: W ilu stopnia Celsjusza woda wrze?
> a) 90
> b) 95
> c) 100
> d) 105
> c
> Gratulacje! Wygrałeś 1 000 zł
> Grasz dalej czy zabierasz wygraną 
> gram 
> Grasz o gwarantowane 2 000 zł. 
> Pytanie 2.: W którym roku miała miejsce bitwa pod Waterloo?
> a) 1795
> b) 1815
> c) 1813
> d) 1805
> > Czy chcesz skorzysta z 50/50?
> tak
> a) 1795
> b) 1815
> a
> Zła odpowiedz! Przegrywasz!
```