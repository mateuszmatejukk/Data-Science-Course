import random

print("This program generates a random integer from 1 to 10 and let you guess it")
a = random.randint(1, 10)  # losuje 1 z 1-10
while True:
    b = input("Give a number from 1 to 10 or press 'Q' to exit")
    if b.upper() == "Q":
        print(f'You exit, my number was {a}')
        break
    elif b.isdigit():
        b = int(b)  # zamiana z tekstu na liczbe calkowita
        if 1 <= b <= 10:
            if b == a:
                print("Congratulations, you guessed it!")
                break
            elif b > a:
                print("This number is too big try again!")
            else:
                print("This number is too small try again!")
        else:
            print('This number is too big try again!\nTry again!')
    else:
        print("You did enter wrong symbol!")
