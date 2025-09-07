"""________This is a blackjack game____________
__---This program is not case-sensitive---___"""


import time
from cards import *
print("This program is not case-sensitive")
print("Welcome to star Casino Uwu!")
print("Welcome to black jack game!")
choice = int(input("Enter (1) - One player game | (2) Game Rules "))

if (choice == 1) :
    name = input("Hey! I am the dealer of the casino. My name is \"Syntax Senpai\". What is the Gentlemen's name? ")   #Enter your name
    time.sleep(1)
    while (True):
        inp1 = input("HohOhOHo! Welcome " + str(name) + ". Shall we play the game? (Enter 'no' to stop playing) : ")
        if (inp1.lower() == "no") : break
        
        class Player:                   #   CLASS
            def __init__(self, name):   #   Object is initialized
                self.name = name
                self.hand = []

            def add_card(self, card):   
                self.hand.append(card)

            def calculate_score(self):
                total = sum(Card.value for Card in self.hand)
                # Handle Ace adjustment
                aces = sum(1 for Card in self.hand if Card.rank == "A")
                while total > 21 and aces:
                    total -= 10
                    aces -= 1
                return total

            def show_hand(self, reveal_all=True):
                if reveal_all:
                    return ", ".join(str(c) for c in self.hand)     #   Using .join function 
                else:
                    return f"{self.hand[0]},  [Hidden]"
            
            def player_hit(self):
                human.add_card(game_deck.deal())
                print("drawing card...")
                time.sleep(1)
                print("...Huh Your cards are : ", self.show_hand())
                time.sleep(1)
                print(str(name) + "'s sum is : ",self.calculate_score())
                time.sleep(1)
    
                
            def computer_hit(self):
                print("Let me draw a card....")
                time.sleep(1)
                self.add_card(game_deck.deal())
                print("drawing card...")
                print("Ok then.. Syntax Senpai's cards are : ",self.show_hand(reveal_all=False))
                time.sleep(1)
    

                """Distribution of cards"""
        game_deck = Deck()
        human = Player(name)
        human.add_card(game_deck.deal())
        human.add_card(game_deck.deal())
        print("Here are your cards kid : ", human.show_hand())

        time.sleep(2)

        computer = Player("computer")
        computer.add_card(game_deck.deal())
        computer.add_card(game_deck.deal())
        print("Hehe, here is my 1st card : ",computer.show_hand(reveal_all=False))
        time.sleep(2)
        print("Hehehe boy, seems like your sum is : ",human.calculate_score())
        inp2 = input("Choose hit or stand : ")
        while (inp2.lower() == "hit"):
            time.sleep(1)       
            human.player_hit()                              #player_hit
            if (human.calculate_score() > 21) : 
                print("Heheh was waiting for it.")
                break

            
            while (computer.calculate_score() < 17) :      #computer turn
                time.sleep(2)
                computer.computer_hit()                     #computer_hit
                if (computer.calculate_score() >= 17) :
                    if (computer.calculate_score() > 21) :
                        print("Oops.. ")
                        print("Well Seems like I will need to stop.")
                        break
                    time.sleep(1)
                    break
            if (computer.calculate_score() > 17) : print("Syntax Senpai is choosing stand.")

            if (human.human_score() != 21) :
                inp2 = input("Choose (hit) | (stand) : ")
            elif (human.calculate_score() == 21) :
                print("Wow! Now it's time for either draw or win for you kid!")
                break
            
            if (inp2.lower() != "hit") : break

        if (inp2.lower() == "stand") :
            print("Hoho You have chosen stand, wise choice!")
            if (computer.calculate_score() >= 17) : print("Syntax Senpai is choosing stand.")

            while (computer.calculate_score() < 17) :
                time.sleep(2)
                computer.computer_hit()
                if (computer.calculate_score() >= 17) :
                    if (computer.calculate_score() > 21) :
                        print("Oops.. ")
                        print("Well Seems like I will need to stop.")
                        break
                    print("Syntax Senpai is choosing stand.")
                    break
        
        print("The outcome is here at last : ")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")        
        time.sleep(1)
        print("1")

        human_score = human.calculate_score()
        computer_score = computer.calculate_score()
        
        #   DISPLAY
        print("This is Syntax Senpai's hand : ", computer.show_hand())
        time.sleep(2)
        print("This is the dealer's score : ",computer_score)
        time.sleep(3)
        print("This is "+ str(name) + "'s hand :", human.show_hand())
        print("This is " + str(name) + "'s score : ", human_score)
        time.sleep(2)

        #Results
        if (human_score > 21): print("You hit hard and the wall hit you back. LMAO DEAD.")
        elif (human_score > computer_score) : print("Haha kid your luck is working today, GG " + str(name) + " !")
        elif (computer_score > 21) : print(" Uwu!! " + str(name) + " won")
        elif (human_score < computer_score ) : print("Heh kid better luck next time!")
        else : print("Hohoh that's a tie.")
        

elif choice == 2:
    rules = """
🃏 BLACKJACK GAME RULES 🃏

1. Goal: Get as close to 21 as possible without going over.
2. Card Values:
   - 2–10 = face value
   - J, Q, K = 10
   - Ace = 1 or 11 (whichever is better for you)
3. Gameplay:
   - You and the dealer start with 2 cards.
   - Dealer shows 1 card face-up, 1 card hidden.
   - On your turn, you can:
       * Hit  -> take another card
       * Stand -> stop taking cards
   - If your total > 21, you bust and lose.
4. Dealer Rules:
   - Dealer reveals hidden card after you finish.
   - Dealer must hit until reaching at least 17.
   - If dealer goes over 21, dealer busts (you win).
5. Winner:
   - If nobody busts, whoever is closer to 21 wins.
   - Equal scores = Tie (Push).
6. Special Case:
   - Ace + 10-value card on first 2 cards = Blackjack (instant win, unless dealer also has Blackjack).
"""
    print(rules)
else:
    print("Invalid input!")
