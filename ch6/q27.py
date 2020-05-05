# Factorial in for-loop
# Try except

try:
    number = int(input('Enter a number: '))
    if number < 0:
        print('The number is not positive')
    else: 
        fac = 1
        for i in range(number, 1, -1):
            fac *= i

        print(f'{number}! = {fac}')
except ValueError:
    print('Wrong value')