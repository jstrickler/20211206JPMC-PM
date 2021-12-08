import sys

print(sys.argv)
print("script name:", sys.argv[0])
if len(sys.argv) > 1:
    print("first arg:", sys.argv[1])
print(f"sys.argv has {len(sys.argv)} elements")
