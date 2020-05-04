message = input('Enter a short message: ')

count = 0
for letter in message:
    if letter == 'a':
        if count < 3:
            print('@', end = '')
        else:
            print('A', end = '')
        count += 1
    else:
        print(letter, end = '')
