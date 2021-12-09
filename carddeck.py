import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):  # interpreter
        # Card('3', 'Diamonds')
        return f"Card('{self.rank}', '{self.suit}')"

    def __str__(self):  # eyeballs
        #  3-Diamonds
        return f"{self.rank}-{self.suit}"

class CardDeck:  # inherit from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer  # private instance data
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if len(self) == 0:
            raise ValueError("No more cards")
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards


    @property
    def dealer(self):  # getter property (like a getter method)
        return self._dealer

    @dealer.setter
    def dealer(self, value):  # setter property
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a str")

    def __str__(self):  # str(obj)
        my_name = type(self).__name__
        return f"{my_name}-{self.dealer}-{len(self)}"

    def __len__(self):
        return len(self._cards)

    def __truediv__(self, other):
        return "HA HA HA"
