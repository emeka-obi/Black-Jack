"""This program mimicks my version of black jack using a class card and deck"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True



class Card:
    """ This class has two object has two data attributes to suit and rank"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
      

    def __str__ (self):
        deck_comp = " "
        for card in self.deck:
            deck_comp +=  '\n' + card.__str__()
        return "The deck has: " +deck_comp
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:

    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.card.append(card)
        self.value += values[card.rank]
        
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_aces(self):
          while self.value > 21 and self.aces:
              self.value -= 10
              self.aces -= 1


# test_deck = Deck()
# test_deck.shuffle
# test_player = Hand()
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card )
# print(test_player.value) 
# test_player.add_card(test_deck.deal())   
# print(test_player.value)   


    

class Chips():

    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet (self):
        self.total = self.total - self.bet
        #return self.total

    def lose_bet(self):
        self.total -= self.bet




def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except:
            print("sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("sorry you do not have enough chips, you have {}".format(chips .total))
            else:
                break

playing = True
def hit(deck, hand):
    obtained_card = deck.deal()
    hand.add_card(obtained_card)
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):

    global playing # to control an upcoming while loop
    while True:
        x = input("Hit or stand ?, enter h or s: ")
        if x[0].lower( )== "s":
             print("Player standds, Dealer's Turn")
             playing = False
        elif x[0].lower() == "h":
            hit(deck, hand)
            playing = True
        else:
            print('You did not enter either h or s, please enter the specified parameters')
            continue
        break

def show_some(player, dealer):
    print("Dealers Hand: ")
    print("One card hidden!")
    print(dealer.card[1])
    print("\n")
    print("Players hand: ")
    for card in player.card:
        print(card)

def show_all(player, dealer):
    print("Dealer's hand")
    for card in dealer.card:
        print(card)
    print("\n")
    print("Players hand: ")
    for card in player.card:
        print(card)


def player_busts(player,dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player wins!!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Player Wins! Dealer busted")

def dealer_wins(player, dealer, chips):
    print("Dealer wins")

def push(player, dealer):
    print("Dealer and player tie! PUSH")
            
        
Game_on = True
while Game_on:

    print("Welcome to   BLACKJACK")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #set up the player's chips
    player_chips = Chips()

    #prompt the player for their bet
    take_bet(player_chips)

    #show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
                
            break

    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        #show all cards
        show_all(player_hand, dealer_hand)

        #run different winning scenarios

        if dealer_hand.value > 21 :
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print("\n Player total chips at: {}".format(player_chips.total))

    new_game = input("Would you like to play another hand ? y/n: ")


    if new_game == "y":
        continue
    else:
        print("Thank you for playing!")
        Game_on = False
        break


      