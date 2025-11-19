import random

print("This program generates a random number and let you guess it")
a = random.randint(1, 10)

b = int(input(print("Podaj liczbę z przedziału 1-10:")))
if b == a:
    print("Congratulations, you won!")
elif b > a:
    print("This is too big try again!")
else:
    print("This is too small try again!")
