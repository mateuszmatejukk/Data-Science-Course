
# Wymagania
# długość > 10 znaków
# conajmniej 4 cyfry
# muszą byc i duże i małe litery
# conajmniej jeden znak specjalny (nie cyfra i nie litera)
haslo = input('Wpisz haslo:')
bledy = ''
numbers = sum(c.isdigit() for c in haslo)
lower_case = sum(c.islower() for c in haslo)
upper_case = sum(c.isupper() for c in haslo)
special_character = sum(c.isalnum() for c in haslo)
if len(haslo) < 10:
    bledy += 'Twoje hasło jest za słabe, długość mniejsza niż 10 znaków'
elif numbers <= 4:
    bledy += 'Twoje hasło jest za słabe, ma za mało cyfr'
elif lower_case == 0 and upper_case == 0:
    bledy += 'W twoim haśle muszą występować i duże i małe litery'
elif special_character == 0:
    bledy += 'W twoim haśle musi wystąpić conajmniej jeden znak specjalny'
elif bledy == '':
    print('Twoje haslo jest silne')
else:
    print('Twoje hasło jest za słabe')
    print(bledy)

