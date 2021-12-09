from carddeck import CardDeck
d1 = CardDeck('Andy')
d2 = CardDeck('Nellie')
print(d1, d2)
print(d1.dealer, d2.dealer)
d1.dealer = "Little Bear"
print(d1.dealer)
try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
else:
    print(d1.dealer.upper())

d1.shuffle()
print(d1.cards)
for _ in range(5):
    print(d1.draw())

print(len(d1), len(d2))
print(d1 / d2)
print(d1, d2)
