import math
import os


def get_message():
    return "Hello, JPMC world"


def show_message():
    message = get_message()
    print(message)


show_message()
m = get_message()
print("m: {}".format(m))

sm = show_message()
print("sm: {}".format(sm))

get_message()
print(get_message())


def circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2


def rectangle_area(length, width):
    return length * width


print(circle_area(100))
print(rectangle_area(80, 99))
print(circle_area(.2903))

def find_term(search_term, *paths, ignore_case=True):
    for file_path in paths:
        file_name = os.path.basename(file_path)
        with open(file_path) as file_in:
            for line in file_in:
                if search_term in line:
                    print(f"{file_name} {line.rstrip()}")

print('-' * 60)
find_term('bird', 'DATA/alice.txt', 'DATA/parrot.txt')
find_term('Lizard', 'DATA/alice.txt', ignore_case=False)
def lookup(*, city, state):
    pass

lookup(city='Durham', state='NC')
lookup(state='NC', city='Durham')

import lxml.etree as et
a = et.Element('animal', genus='Vombatus', species='ursinus')
a.text = "William"
print(et.tostring(a, pretty_print=True).decode())




