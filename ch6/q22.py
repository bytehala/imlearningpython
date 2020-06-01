first = int(input('First number: '))
second = int(input('Second number: '))

if first > second:
    temp = first
    first = second
    second = temp

product = 1
for i in range(first, second+1):
    if i != 0:
        product *= i
    if product < -500 or product > 500:
        print('Exceeded')
        break
    

print(product)