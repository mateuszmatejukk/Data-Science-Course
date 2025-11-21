print(f'This is basic console calculator on chosen float two numbers', end="\n")
a = float(input('Please write first number: '))  # dziala dla zmiennoprzecinkowych
b = float(input('Please write second number: '))
print("")
print('Press "1" to add\nPress "2" to subtract\nPress "3" to multiply\nPress "4" to divide\nPress "Q" to exit')
print("")
while True:
    c = input('Please choose what you want to do with them: ')
    if c.upper() == "Q":  # wiec q tez ok
        print('Exiting calculator')
        break
    elif c == '1':
        print(f'Result is: {a + b}')
    elif c == '2':
        print(f'Result is: {a - b}')
    elif c == '3':
        print(f'Result is: {a * b}')
    elif c == '4':
        if b == 0:
            print('We do not divide by zero!')
        else:
            print(f'Result is: {a / b}')
    else:
        print('You chose wrong operation')
    print('-' * 30)
