
low = 0
high = 0
for i in range(0, 10):
    num = int(input('Enter a number: '))
    if i == 0:
        low = num
        high = num
    if num < low:
        low = num
    if num > high:
        high = num
    
print(f'High: {high} Low: {low}')