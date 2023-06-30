countries = ['USA', 2, True, 2, 'Ghana', 'Malta']
cities = list(('Plovdiv', 'Hull'))

cities.append('Mezdra')
cities.insert(0, 'lemon')
countries.remove(True)

countries.extend(cities)

del countries[0]

print(countries)
print(countries.index(2))
print(countries.count(2))

print(len(countries))

print(type(countries))
print(type(countries[-1]))
print(type(countries[1]))
print(type(countries[2]))

print(countries[4][0])
print(countries[2:])
print(countries[1:3])

countries.clear()
del countries

print(countries)
