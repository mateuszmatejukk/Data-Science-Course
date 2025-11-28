uwagi = 1
while uwagi != 0:
    print('Podaj dane auta')
    uwagi = 0
    marka = input('Marka: ')
    model = input('Model: ')
    rok_produkcji = int(input('Rok produkcji:'))
    przebieg = int(input('Przebieg:'))
    ostatni_przeglad = int(input('Wpisz przebieg podczas ostatniego przeglądu '))
    if rok_produkcji < 2010:
        uwagi += 1
        print('Wynik negatywny,za niski poziom oleju: 800mm (norma >900mm')
    if przebieg > 200000:
        uwagi += 1
        print('Wynik negatywny, za niskie ciśnienie w oponach: 1.2PSI (norma >2PSI)')
    if przebieg- ostatni_przeglad > 20000:
        uwagi += 1
        print('Wynik negatywny, za dawno był Pan na przeglądzie')

if uwagi == 0:
    print('Wynik pozytywny')
    print(f'Twoje auto to: {marka} {model} wyprodukowane w {rok_produkcji} roku o przebiegu {przebieg} kilometrów')