list1 = list()  # list list1 = new list();
# [1, 2, 3]
list2 = [1, 2, 'a', 'b', 9]
list3 = []

cities = ['Plano', 'Wilmington', 'Columbus', 'Jersey City']
print(cities)
print(cities[0], cities[3], cities[-1], cities[len(cities) - 1])
cities.insert(0, 'Dallas')
print(cities)
cities.insert(3, 'Arlington')
print(cities)
cities.append('Chicago')
cities.append('Durham')
print(cities)
more_cities = ['Hyderabad', 'Mumbai', 'Kolkata']
cities.extend(more_cities)
print(cities)

#  LIST.insert(pos, value)  LIST.append(value)  LIST.extend(iterable)
# more_cities = ['Miami', 'Miami', 'Miami']
# cities.extend(more_cities)
print(cities)
del cities[3]
print(cities)
c = cities.pop()
print(c, cities)

#  LIST.sort()
#  new_list = sorted(LIST)

cities.remove('Chicago')

#  del LIST[pos]    LIST.pop(pos=-1)   LIST.remove(value)

cities_sorted = sorted(cities)
print(cities_sorted)
print(cities)
# cities.sort()   sort in place
print(cities[0:3])   # [start:stop]  0 through 2
print(cities[2:6])   # 2 through 5
# start is INclusive
# stop is EXclusive
print(cities[:3])
print(cities[4:])
print(cities[-3:])
print(cities[1:-1])
print(cities)
print()

#  for VAR in ITERABLE:
for city in cities:
    print(city, len(city))

nothing = []
for thing in nothing:
    print("I'm having an existential crisis")

s = "abc"
for ch in s:
    print(ch.upper())













food = ['spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]



