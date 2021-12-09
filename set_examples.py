john_countries = ['Spain', 'Canada', 'China', 'Mexico', 'Bulgaria', 'France', 'UK',
                  'Austria']
clare_countries = ['Spain', 'Canada', 'Mexico', 'France', 'UK', 'Kenya', 'Denmark', 'Sweden']

john = set(john_countries)
clare = set(clare_countries)
john.add('Barbados')
clare.add('Barbados')
print("Common:", john & clare)  # intersection
print("Not common:", john ^ clare)  # xor
print("Either:", john | clare)   # union
print("Just John:", john - clare)
print("Just Clare:", clare - john)

food = ['spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]

unique_food = set(food)
print(unique_food)




