fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(fruits), min(fruits), max(fruits))
print(sorted(fruits), '\n')
print(len(nums), min(nums), max(nums), sum(nums))
print(sorted(nums))

print(fruits)
rf = reversed(fruits)
print(rf)
for fruit in rf:
    print(fruit, end=',')
print('\n')
print('-' * 60)
for fruit in rf:
    print("second time:", fruit, end=',')

capitals = ['Austin', 'Raleigh', 'Albany']
states = ['TX', 'NC', 'NY', 'DE', 'IL']
state_capitals = zip(capitals, states)
print(state_capitals)
print(list(state_capitals), '\n')

for i, fruit in enumerate(fruits):
    print(i, fruit)
print()
print(list(enumerate(fruits, 1)), '\n')
e = enumerate(fruits)
print(e)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("c: {}\n".format(c))

print('-' * 60)
print('wombats' * 3)
flags = [True] * 10
print(flags)
data = [0] * 25
print(data)

# range(stop)  range(start, stop)  range(start, stop, step)
r = range(10)
print(r)
for i in r:
    print(i, end='/')
print()
for i in range(1, 11):
    print(i, i ** 2, i ** 3)

for i in range(5):
    print("Python is the best!!")

