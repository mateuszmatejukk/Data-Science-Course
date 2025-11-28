import random

print("This program generates a random integer from 1 to a number entered by you and let you guess it")
x = int(input("Please enter the maximum integer number: "))
a = random.randint(1, x)  # losuje 1 do x
while True:
    b = input(f'Give a number from 1 to {x} or press "Q" to exit ')
    if b.upper() == "Q":
        print(f'You exit, my number was {a}')
        break
    elif b.isdigit():
        b = int(b)  # str na int
        if 1 <= b <= x:
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
