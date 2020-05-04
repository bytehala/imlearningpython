testScore = int(input('Enter score: '))


if testScore >= 70 and testScore <= 100:
    print('Á')
elif testScore >= 60 and testScore <=69:
    print('B')
elif testScore >= 50 and testScore <= 59:
    print('C')
elif testScore >= 0 and testScore < 50:
    print('Fail')
else:
    print('Invalid')