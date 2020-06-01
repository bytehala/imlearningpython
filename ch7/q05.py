def calculateQuotient(a, b):
    quotient = 0
    try:
        quotient = a/b
    except:
        quotient = -1
    return quotient

print(calculateQuotient('abcd', 2))