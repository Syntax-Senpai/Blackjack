import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__ (self):
        suit = ['diamond', 'heart', 'spade', 'club']
        rank = {'2' : 2, '3':3, '4':4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 
                'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11}
        self.card = [Card(s,r,v) for s in suit for r, v in rank.items()]
        random.shuffle(self.card)

    def deal(self):
        return self.card.pop()


