i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    name = input("Enter your name (or q to quit): ")
    if name == 'q':
        break  # exit loop NOW
    if name == '':
        print("Please enter a name.")
        continue  # go to top
    print("Hello,", name)
