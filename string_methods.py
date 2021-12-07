import re

actor = "Chris Hemsworth"

print(actor)
print(len(actor), type(actor), isinstance(actor, str))
print(actor.upper())
print(actor.lower())
print(actor.capitalize())
print(actor.title())
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))  # ignore case
print("spam".upper())

print(re.match('chris', actor, re.I))
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print(actor.find('Chris'))
print(actor.lower().find('chris'))
print(actor.find('worth'))
print(actor.find('Liam'))

s = "     fee    fi     fo     fum     "
print(s.split())

s = "fee:fi:fo:fum"
print(s.split(':'))

suits = 'Clubs Diamonds Hearts Spades'.split()
print(suits)

print(actor.replace('Chris', 'Liam'))

s = "    All my exes live in Texas      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print('-' * 60)

s = "xxxxxxxxxxxxyxxxxxAll my exes live in Texasyyyyyxyyyyyy"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print('-' * 60)

line = "spam\n"
data = line.rstrip()

item = "45."
data = item.rstrip(".")
print(data)

s = "foo/bar"
print(s.partition('/'))





