from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

for name, raw_data in knight_data.items():
    print(name, raw_data)
print()

# for key, data in DICT.items()
for name, raw_data in knight_data.items():
    print(raw_data[0], name)
print()
