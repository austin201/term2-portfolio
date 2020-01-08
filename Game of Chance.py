# Austin Daybell
# Games of Chance

# imports
import random

deck = ['Queen', '6', '9', '10', 'Ace', 'King', '5', '2', '7', '4', '8', 'Jack', '3']
randanswer = random.shuffle(deck)
print(randanswer)
cardIndex = random.randint(0,12)
card = deck[cardIndex]
print(str.format("Card at index {0}='{1}'",cardIndex,card))
coinFlipOptions = ("Heads","Tails")
for i in range(0,5):
    flip = random.choice(coinFlipOptions)
    print("Coin-flip results:{0}",flip)
