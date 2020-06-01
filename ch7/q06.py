def absoluteValue(value):
    try:
        num = float(value)
        if num >= 0:
            return num
        else:
            return num * -1
    except:
        return -1

print(absoluteValue(-1))
print(absoluteValue(11))
print(absoluteValue(0))
print(absoluteValue('aaaa'))