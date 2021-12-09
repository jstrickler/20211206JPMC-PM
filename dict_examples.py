d1 = dict()  # empty dict
d2 = {'a': 5, 'm': 3, 'e': 7}
d3 = {}  # empty dict

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
airports['ALB'] = 'Albany'
airports['MCI'] = 'Dogpatch'
print(airports)

print(airports['RDU'], '\n')

for code in 'RDU', 'LAX', 'SEA', 'IAH', 'ABQ':
    print(code, code in airports)
print()

# print(airports['IAH'])
print(airports.get('IAH'))
print(airports.get('IAH', 'NOT IN DB'))

print(airports.setdefault('IAH', 'Houston'))
print(airports, '\n')

for code, name in airports.items():
    print(code, name)
print()




