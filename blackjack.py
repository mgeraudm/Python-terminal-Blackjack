"""
    This is a line executed Python BlackJack game written by mgeraudm during Mastering Fintech and ML course on Udemy (December 2022)
"""
from random import shuffle

def createdeck():
    Deck=[]
    faceValues = ["A","J","Q","K"]
    for i in range(4):
        for card in range (2,11):
            Deck.append(str(card))
        for card in faceValues:
            Deck.append(card)
    shuffle(Deck)
    return Deck
deck = createdeck()

#print(deck)

class Player: 
    def __init__(self, hand =[], money = 100):
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0
        
    def __str__(self):  #print(Player)
        currentHand = ""
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = currentHand + "score: " + str(self.score)
        return finalStatus
    def setScore(self):
        self.score = 0
        faceCardsDict = {"A":11,"J":10,"Q":10,"K":10, "2":2, "3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
        acecounter = 0
        for card in self.hand:
            self.score += faceCardsDict[card]
            if card == "A":
                acecounter += 1
            if self.score > 21 and acecounter != 0:
                self.score -= 10
                acecounter -= 1
        return self.score
    def hit(self, card):
        self.hand.append(card)
        self.score = self.setScore()
    def play(self, newhand):
        print("New Hand: ")
        self.hand = newhand
        self.score = self.setScore()
    def betMoney(self, amount):
        self.money -= amount
        self.bet += amount
    def win (self,result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money +=2.5*self.bet
            else: 
                self.money += 2*self.bet
            self.bet = 0
        else:
            self.bet = 0
    def draw(self):
        self.money += self.bet
        self.bet = 0
    def hasBlackjack(self):
          if self.score == 21 and len(self.hand) == 2:
              return True
          else:
              return False
            
def printHouse(House):
    for card in range(len(House.hand)):
        if card ==0:
            print ("House :", "X",end = " ")
        elif card == len(House.hand) - 1:
            print(House.hand[card])
        else:
            print(House.hand[card], end = " ")
            
cardDeck = createdeck()
firstHand = [cardDeck.pop(),cardDeck.pop()]
secondHand = [cardDeck.pop(),cardDeck.pop()]
Player1=Player(firstHand)
House = Player(secondHand)
keepPlaying = "y"

while(keepPlaying == "y"):
    if len(cardDeck) < 20:
        cardDeck = createdeck()
    
#print(cardDeck)
    firstHand = [cardDeck.pop(),cardDeck.pop()]
    secondHand = [cardDeck.pop(),cardDeck.pop()]
    Player1.play(firstHand)
    House.play(secondHand)
    
    Bet = int(input("Please place your bet: "))
    Player1.betMoney(Bet)
    #print("Player: $",Player1.money)
    #print(cardDeck)
    print("Player:", Player1)
    printHouse(House)
    print(" ")
    print(" ")

    if Player1.hasBlackjack():
        if House.hasBlackjack():
            Player1.draw()
        else:
            Player1.win(True)
    else:        
        while(Player1.score < 21):
            action = input("Do you want another card? (y/n): ")
            if action == "y": 
                Player1.hit(cardDeck.pop())
                print("Player:", Player1)
            else:
                break
        
        while(House.score < 16):
            House.hit(cardDeck.pop())
            printHouse(House)
        if Player1.score > 21:
            if House.score >21:
                Player1.draw()
            else:
                Player1.win(False)
                    
        elif Player1.score > House.score:
            Player1.win(True)    
        elif Player1.score == House.score:
            Player1.draw()
        else: 
            if House.score > 21:
                Player1.win(True)
            else:
                Player1.win(False)
                        
    print("House :", House)
    print("Player:", Player1)
    print("Player: $",Player1.money)
    print(" ")

    keepPlaying = input("Keep Playing ? (y/n): ")