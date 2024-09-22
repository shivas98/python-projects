import random

class Card:
    '''This class handles and instantiate one card'''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Deck:
    '''This class instantiates a deck of cards'''
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #creating list of objects for all cards
                self.all_cards.append(Card(suit,rank))

    def shuffle_cards(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        #remove one card from the list of all_cards
        return self.all_cards.pop()
    
class Player:
    '''This class instatiates player objects who will play the cards during the game'''
    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        # remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


if __name__ == '__main__':
    # defining the suit and rank of the cards in a deck
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

    # initializing a new deck of cards
    new_deck = Deck()
    # shuffling the deck of the cards created
    new_deck.shuffle_cards()

    # initializing the players who will play the game
    player_one = Player('One')
    player_two = Player('Two')

    # distributing the deck of cards between two players
    for i in range(26):
        player_one.all_cards.append(new_deck.deal_one())
        player_two.all_cards.append(new_deck.deal_one())

    game_on = True
    round_num = 0

    while game_on:

        # checking if any players has lost all cards
        if len(player_one.all_cards) == 0:
            print('Player One is out of cards. Player Two Wins!')
            print('Game Over!')
            game_on = False
            break
        elif len(player_two.all_cards) == 0:
            print('Player Two is out of cards. Player One Wins!')
            print('Game Over!')
            game_on = False
            break

        # stating a new round
        round_num += 1
        print(f'Round {round_num}')

        # Start a new round and reset current cards "on the table"
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True

        while at_war:

            # comparing player cards
            if player_one_cards[-1].value > player_two_cards[-1].value:
                # player one wins, adding both cards to player one's deck
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                at_war = False

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                # player two wins, adding both cards to player two's deck
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                at_war = False

            else:
                print('WAR!')
                
                if len(player_one.all_cards) < 5:
                    # if player one does not have 5 cards left to draw for war, player two wins
                    print('Player One does not have enough cards to play war. Player Two wins!')
                    print('Game Over!')
                    game_on = False
                    at_war = False

                elif len(player_two.all_cards) < 5:
                    # if player two does not have 5 cards left to draw for war, player one wins
                    print('Player Two does not have enough cards to play war. Player One wins!')
                    print('Game Over!')
                    game_on = False
                    at_war = False
                else:
                    # if both players have 5 cards left to draw for war, they draw the cards and game continues
                    for i in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())




