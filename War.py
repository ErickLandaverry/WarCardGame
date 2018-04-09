from random import shuffle
import time

class card:
    def __init__(self, suit, rank):
        self.suit = suit.lower() 
        self.rank = rank

    def isBlackOrRed(self):
      
        if self.suit == "hearts" or self.suit == "diamonds":
            return "red"
        else:
            return "black"

    def isFaceCard(self):
       
        faceCards = [11, 12, 13]
        for faceCard in faceCards:
            if self.rank == faceCard:
                return True
        return False

    def getDescription(self):
        
        return [self.rank, self.suit]

    def __repr__(self):
       
        rank = self.rank
        if rank == 1:
            rank = "ace"
        elif rank == 11:
            rank = "jack"
        elif rank == 12:
            rank = "queen"
        elif rank == 13:
            rank = "king"

        return "{} of {}".format(rank, self.suit)



class cardStack:
    
    def __init__(self, name=""):
        
        self.stack = []
        self.name = name

    def giveFullDeck(self):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        for suit in suits:
            for rank in range(1, 14):
                self.stack.append(card(suit, rank))  

    def stackSize(self):
        
        return len(self.stack)

    def shuffle(self, amount=1):
       
        for i in range(0, amount):
            shuffle(self.stack)

    def deal(self, amount, stack, position=-1):
        for i in range(0, amount):
            dealt = self.stack[0:1]
            self.stack = self.stack[1:]
            for i in dealt:
                stack.stack.insert(position, i)

    def splitDeckIntoTwoStacks(self, stack1, stack2):
       
        while len(self.stack) > 0:
                self.deal(1, stack1)
                self.deal(1, stack2)

    def splitStack(self, stack):
        
        while len(self.stack) > len(self.stack)/2:
                self.deal(1, stack)

    def __str__(self):
        spaces = ""
        print(self.name)
        for card in self.stack:
            print(spaces, card)
            spaces += "  "
        return ""

def highPlay(mainDeck):
    play1 = deck.stack[0].rank
    print("You played:", deck.stack[0])
    play2 = deck.stack[1].rank
    print("Your opponent played:", deck.stack[1])
    if play1 > play2:
        return "play1"
    elif play2 > play1:
        return "play2"
    else:
        return "draw"


deck = cardStack()  
deck.giveFullDeck()  
deck.shuffle(amount=5)  
player1Hand = cardStack()  
player2Hand = cardStack()  
deck.splitDeckIntoTwoStacks(player1Hand, player2Hand) 
round = 0



print('This is War!!')
answer=input('Are you ready to battle?')
if answer == "yes":
  print('')
  print('''Rules: This two player game is played using a standard 52-card deck. The objective of the game is to win all the cards. The deck is divided evenly among the players, giving each a deck of face-down cards. In unison, each player reveals the top card of their deck – this is a battle – and the player with the higher card adds both cards to the bottom of their deck. If the cards are of equal value, it's war!

This process is repeated until one player runs out of cards, at which point the other player is declared the winner.''')
  print("")
elif answer == "no":
  print("whatever... bye") 


while True:
    
    player1Hand.shuffle()
    player2Hand.shuffle()
    round += 1 
    print()
    print("------")
    print()
    print("This is round:", round)
    print("and you have", len(player1Hand.stack), "cards")  
    deck.stack = []  
    wait = input("press ENTER to play a card")
    print()

    
    player1Hand.deal(1, deck)  
    player2Hand.deal(1, deck)  
    while True:
        highestPlay = highPlay(deck)  
        if highestPlay == "play1":
            print("YOU WON THE ROUND!")
            print("You won the following cards:")
            print(deck)
            deck.deal(len(deck.stack), player1Hand)
            break
        elif highestPlay == "play2":
            print("Your opponent won the round")
            print("He won the following cards:")
            print(deck)
            deck.deal(len(deck.stack), player2Hand)
            break

        elif highestPlay == "draw":
            print("DRAW!")
            wait = input("WAR! Press ENTER to play a card facedown")
            player1Hand.deal(1, deck)  
            wait = input("press ENTER to play a card faceup")
            print()
            player1Hand.deal(1, deck, 0)  
            player2Hand.deal(1, deck)
            player2Hand.deal(1, deck, 0)
            print("Your opponent played two cards")

    if len(player1Hand.stack) == 0:  
        print("You lost the war")
        wait = input("the game is over, press ENTER to quit")
        break
    elif len(player2Hand.stack) == 0:  
        print("You Win!")
        wait = input("the game is over, press ENTER to quit")
        break