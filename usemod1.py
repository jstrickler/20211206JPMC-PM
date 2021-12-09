import sys
from john.math import geometry

# find and load geometry.py

c1 = geometry.circle_area(100)
c2 = geometry.circle_area(118)
r1 = geometry.rectangle_area(5, 10)
r2 = geometry.rectangle_area(8.5, 13.7)
print(c1, c2)
print(r1, r2)
print(10 * geometry.PI)
print()

# module search order:
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders

for path in sys.path:
    print(path)