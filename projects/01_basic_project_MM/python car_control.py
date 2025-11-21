print('Podaj dane auta')
marka = input('Marka: ')
model = input('Model: ')
rok_produkcji = int(input('Rok produkcji:'))
przebieg = int(input('Przebieg:'))

uwagi = ''
if rok_produkcji < 2010:
    uwagi += 'Za niski poziom oleju: 800mm (norma >900mm)'
else:
    print('Poziom oleju w porządku: 950 mm (norma >900mm)')
if przebieg > 200000:
    uwagi += 'Za niskie ciśnienie w oponach: 1.2PSI (norma >2PSI)'
else:
    print('Ciśnienie opon w porządku: 2.1PSI')
print(f'Twoje auto to: {marka} {model} wyprodukowane w {rok_produkcji} roku o przebiegu {przebieg} kilometrów')
if uwagi == '':
    print('Wynik pozytywny')
else:
    print('Wynik negatynwy')
    print(uwagi)

