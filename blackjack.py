import random

suits = ['C','D','H','S'] 
values = [str(i) for i in range(1,10)] + ['J','Q','K','A']
deck = []
for suit in suits:
    for value in values:
        deck.append(value + suit)
print(values)
print(deck)
random.shuffle(deck)
print(deck)

