file_path = "DATA/mary.txt"

#  'r' 'w' 'a' 'x'

with open(file_path, 'r') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open(file_path, 'r') as mary_in:
    all_contents = mary_in.read()
    print("raw:", repr(all_contents))
    print("normal:")
    print(all_contents)
print('-' * 60)

with open(file_path, 'r') as mary_in:
    lines_with_cr = mary_in.readlines()
    print(lines_with_cr)
print('-' * 60)

with open(file_path, 'r') as mary_in:
    lines_without_cr = mary_in.read().splitlines()
    print(lines_without_cr)

start_letter = 'x'
count = 0
output_file_name = f"{start_letter}_words.txt"
with open('DATA/words.txt') as words_in:
    with open(output_file_name, 'w') as words_out:
        for line in words_in:
            if line.startswith(start_letter):
                count += 1
                words_out.write(line)
print(f"{count} words start with {start_letter}")

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

