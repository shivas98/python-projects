import random

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:

    def __init__(self):
        self.deck = []  # deck start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # build Card objects and add them to the list

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The Deck has:' + deck_comp
    
class Hand():

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self, total=100):
        self.total = total   # This is set as default value and can be modified to supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How much chips would you like to bet?\n'))
        except:
            print('Sorry, a bet must be a number\n')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you don\'t have enough chips. You have {chips.total} chips left. Make a bet again\n')
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        user_input = input("Would you like to Hit or Stand? Enter 'H' or 'S'\n")
        
        if user_input[0].lower() == 'h':
            hit(deck,hand)

        elif user_input[0].lower() == 's':
            print("Player stands. Dealer is playing.\n")
            playing = False

        else:
            print("Sorry, please try again.\n")
            continue
        break

def show_some(player,dealer):
    print("Dealer's Hand:")
    print("<card hidden>")
    print(dealer.cards[1])
    print("Player's Hand:", *player.cards, sep='\n')
    
def show_all(player,dealer):
    print("Dealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer Hand's Value =",dealer.value)
    print("Player's Hand:", *player.cards, sep='\n')
    print("Player Hand's Value =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts! Dealer Wins!\n")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!\n")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts! Player Wins!\n")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!\n")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.\n")


if __name__ == '__main__':

    # defining the suit and rank of the cards in a deck
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
    playing = True

    while True:
        # Printing an opening statement
        print('Welcome to BLACK JACK!\n')

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's chips
        player_chips = Chips()

        # Prompt the Player to make their bet
        take_bet(player_chips)

        while playing:

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck,player_hand)

            # If player's hand exceeds 21, break out of loop
            if player_hand.value > 21:
                playing = False

        # If Player isn't busted, play Dealer's hand until Dealer until dealer hand's value is less than player hand's value 
        if player_hand.value <= 21:

            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

        # Runing different winning scenarios
        if player_hand.value > 21:
            show_all(player_hand, dealer_hand)  # Show all cards
            player_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > 21:
            show_all(player_hand, dealer_hand)  # Show all cards
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            show_all(player_hand, dealer_hand)  # Show all cards
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            show_all(player_hand, dealer_hand)  # Show all cards
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            show_all(player_hand, dealer_hand)  # Show all cards
            push(player_hand, dealer_hand)

        # Informing Player of their chips total
        print(f'Player\'s total chips stands at: {player_chips.total}\n')

        # Asking to play again
        new_game = input('Would you like to play the game again? Y/N\n').lower()

        if new_game[0] == 'y':
            playing = True
            continue
        else:
            break