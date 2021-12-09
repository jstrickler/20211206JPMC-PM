
animal = "wombat"  # global variable

def spam():
    country = "Australia"  # local variable
    print("in spam(): country is", country)

spam()

print("in main: country is", country)

