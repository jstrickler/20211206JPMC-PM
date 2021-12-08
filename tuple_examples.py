
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'
print(type(person), type(person[0]))
print(person[0], person[1])

first_name, last_name, product, dob = person   # iterable unpacking

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

for person in people:
    print(person[0], person[1])
print('-' * 60)

for person in people:
    first_name, last_name, product, dob = person
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product, dob in people:
    print(first_name, last_name)
print('-' * 60)

cities = [('Plano', 'TX'), ("Wilmington", 'DE'), ("Chicago", "IL")]
print(type(cities), type(cities[0]))

for city, state in cities:
    print(f"{city} is in {state}")

print('-' * 60)
print("city: {}\n".format(city))

