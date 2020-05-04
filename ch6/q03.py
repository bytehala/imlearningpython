num = int(input('Enter a number: '))
if num > 0:
    print(num)
elif num == 0:
    print('You entered 0')
else:
    num *= -1
    print(num)