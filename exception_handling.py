import sqlite3

file_path = 'DATA/wombats.txt'

try:
    with open(file_path) as file_in:
        for line in file_in:
            print(line.rstrip())
except (FileNotFoundError, PermissionError) as err:
    print(err)

with open('DATA/breakfast.txt') as breakfast_in:
    food = breakfast_in.read().splitlines()

try:
    print(food[20])
except IndexError as err:
    print(err)

nums = [800, 5, 0, 101, 80, 1000, 32, 255, 400, 5, 5000]

for num in nums:
    try:
        result = 29 / num
    except ZeroDivisionError as err:
        print(err)
    except Exception as err:
        pass  # log, print, etc.
    else:
        print(result)

conn = None
try:
    conn = sqlite3.connect('DATA/animals/wombat.db')
except sqlite3.OperationalError as err:
    print(err)
else:
    cursor = conn.cursor()
    cursor.execute('select * from wombats')
    results = cursor.fetchall()
finally:
    if conn is not None:
        conn.close()






print("ALL DONE")

