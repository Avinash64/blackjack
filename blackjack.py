import random

def card_value(card):
    val = card[:-1]
    if val in "JQK":
        return 10
    if val == 'A':
        return 11
    return int(card[:-1])

suits = ['C','D','H','S'] 
values = [str(i) for i in range(1,10)] + ['J','Q','K','A']
deck = []
for suit in suits:
    for value in values:
        deck.append(value + suit)
#print(values)
#print(deck)
random.shuffle(deck)
#print(deck)
hand = []
dealer = []
hsum = 0
dsum = 0
print('Welcome to Blackjack!')
for i in range(2):
    card = deck.pop(0)
    hand.append(card)
    hsum += card_value(card)
    card = deck.pop(0)
    dealer.append(card)
    dsum += card_value(card)
    action = None
print(f'Your cards are {" ".join(hand)} [Total: {hsum}]')
while hsum < 21 and action != 's':
    action = input("Hit or stand?: ").lower()
    while action == '' or action not in 'hs':
        action = input("Invalid input! Hit or stand?: ")
    action = action[0]
    if action == 'h':
        card = deck.pop(0)
        hand.append(card)
        hsum += card_value(card)
        print('hit')
        print(f'Your cards are {" ".join(hand)} [Total: {hsum}]')
            
    if action == 's':
        print('stand')
if hsum > 21:
    print("You've gone bust! Better luck next time.")
else:
    while dsum <17:
        print(f'Your cards are {" ".join(hand)} [Total: {hsum}]')
        card = deck.pop(0)
        dealer.append(card)
        dsum += card_value(card)
        print(f'Dealers cards are {" ".join(dealer)} [Total: {dsum}]')
    if dsum > 21:
        print('Dealer has gone bust. You win!')
    elif hsum == dsum:
        print("Its a draw! The hand is a wash")
    else:
        print(f'You have {hsum}, the dealer has {dsum}...')
        if dsum > hsum:
            print("Dealer Wins!")
        else:
            print("You Win!")

#for i in range(52):
#    card = deck.pop(0)
#    print(card, card_value(card))
