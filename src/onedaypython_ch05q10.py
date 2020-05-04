places = {
    'Chicago': 'USA',
    'Los Angeles': 'USA',
    'New York': 'USA',
    'Osaka': 'Japan',
    'Tokyo': 'Japan',
    'Shanghai': 'China',
    'Moscow': 'Russia',
    'Paris': 'France',
    'London': 'England',
    'Seoul': 'South Korea'
}

print(places.keys())

city = input('Please enter a city from the list above: ')
print(f'{city} is in {places[city]}')