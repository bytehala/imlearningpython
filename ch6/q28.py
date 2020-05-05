proLang = ['Python', 'Java', 'C', 'C++', 'C#', 'PHP', 'Javascript']

index = int(input('What index? '))
try:
    print(proLang[index])
except IndexError:
    print('Out of range')
except Exception as e:
    print(e)