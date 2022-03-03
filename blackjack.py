import random

suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":1}

playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def __str__(self):
        return "\n".join([str(card) for card in self.all_cards])
         

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
    
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1
        

    def adjust_for_aces(self):
        if self.value >= 11 and self.aces > 0:
            self.value += 10
            
    
    def __str__(self):
        return ", ".join([str(card) for card in self.cards])
    

class Chips:
    def __init__(self):
        self.total = 0
        self.bet = 0
       
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
    
    def take_bet(self):
        while True:
            bet = input("Please place your bet:")
            if bet.isdigit():
                self.bet = int(bet)
                break
            else:
                print("Please enter a number")
                continue
                
                
#function for playing setup

#taking Hits function
#function to display the hand
def show_some(player,dealer):
    dealer_first_rank = dealer.cards[0].rank
    dealer_first_suit = dealer.cards[0].suit
    print("Player hand: {}".format(player))
    print("Dealer hand: {} of {}".format(dealer_first_rank,dealer_first_suit))
    
#taking Hits function
def show_all(player,dealer):
    print("Player hand: {}".format(player))
    print("Dealer hand: {}".format(dealer))

def hit(deck,hand):
    global playing
    while hand.value < 22:
        hit = input("Do you want to hit? Y/N")
        if hit == "Y" or hit == "y":
            hand.add_card(deck.deal_one())
            hand.adjust_for_aces()
            show_some(player,dealer)
            
        else:
            playing = False
            break
    
    
def player_busts(player,chips):
    global playing
    if player.value > 21:
        print("Player bust!")
        chips.lose_bet()
        playing = False
        

def player_wins(player,chips,dealer):
    if player.value < 22 and player.value > dealer.value:
        print("Player wins!")
        chips.win_bet()
        
    

def dealer_busts(chips,dealer):
    if dealer.value > 21:
        print("Dealer busts! Player wins!")
        chips.win_bet()
        
        

def dealer_wins(player,chips,dealer):
    if player.value < dealer.value:
        print("Dealer wins")
        chips.lose_bet()
        
        

def push():
    if player.value == dealer.value:
        print("Push")
        chips.bet = 0 
        
        
        
#Gameplay

while True:
    print("Welcome to the Blackjack game")
    global playing
    playing = True
    #Creating the deck of card and shuffle
    deck = Deck()
    deck.shuffle()
    
    #Creating player and dealer hand
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_one())
    player.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())
    
    #setup player chips
    chips = Chips()
    
    #asking for player bet
    chips.take_bet()
    
    #show card (only 1 for dealer)
    show_some(player,dealer)
    
    
    
    while playing:
        #ask to hit or stand
        hit(deck,player)
        
        #check if player bust
        
        player_busts(player,chips)
        
    #show all cards
    show_all(player,dealer)
        
    #play dealer hand until he reach 17
    while dealer.value < 17:
        dealer.add_card(deck.deal_one())
        dealer.adjust_for_aces()
            
    show_all(player,dealer)
        
    #running different winning scenarios
    player_wins(player,chips,dealer)
    dealer_busts(chips,dealer)
    dealer_wins(player,chips,dealer)
    push()
        
    #inform player of their chips total
    print("Your chips total is : {}".format(chips.total))
    
    play_again = input("Do you want to play another hand? Y/N")
    if play_again == "Y" or play_again == "y":
        continue
    else:
        break