# Wymagania
# długość > 10 znaków
# conajmniej 4 cyfry
# muszą byc i duże i małe litery
# conajmniej jeden znak specjalny (nie cyfra i nie litera)
bledy = 1
while bledy != 0:
    haslo = input('Wpisz haslo:')
    bledy = 0
    numbers = sum(c.isdigit() for c in haslo)
    lower_case = sum(c.islower() for c in haslo)
    upper_case = sum(c.isupper() for c in haslo)
    special_character = sum(not c.isalnum() for c in haslo)
    if len(haslo) < 10:
        bledy += 1
        print('Twoje hasło jest za słabe, długość mniejsza niż 10 znaków')
    if numbers < 4:
        print('Twoje hasło jest za słabe, ma za mało cyfr')
        bledy += 1
    if lower_case == 0:
        print('W twoim haśle muszą występować male litery')
        bledy += 1
    if upper_case == 0:
        print('W twoim haśle muszą występować duże litery')
        bledy += 1
    if special_character == 0:
        print('W twoim haśle musi wystąpić conajmniej jeden znak specjalny')#to liczy tez spacje
        bledy += 1

print('Twoje haslo jest silne')