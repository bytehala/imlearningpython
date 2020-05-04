numbers = input('Please enter 5 comma separated numbers: ')

nums = numbers.split(',')
sum = 0
for n in nums:
    sum += int(n)

print(f'The sum is {sum}')