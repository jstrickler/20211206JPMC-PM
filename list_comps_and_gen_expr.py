fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

f1 = [f.upper() for f in fruits]  # list comprehension
print("f1: {}\n".format(f1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

food = ['spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'toast',
        'waffles', 'naan', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam',
        'eggs',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]

good_food = [f for f in food if f != 'spam']
print("good_food: {}\n".format(good_food))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[3] for p in people]
print("dobs: {}\n".format(dobs))

f1 = [f.upper() for f in fruits]
fgen = (f.upper()[:3] for f in fruits)
print("fgen: {}\n".format(fgen))
for fruit in fgen:
    print(fruit)




