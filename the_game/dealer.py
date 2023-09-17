from the_game.deck import Deck
from the_game.player import Player


class Dealer:
    def __init__(self, min_card, max_card, np_random):
        self.min_card = min_card
        self.max_card = max_card
        self.np_random = np_random
        self.deck = Deck(min_card=min_card+1, max_card=max_card-1, np_random=np_random)
        self.shuffle()

    def shuffle(self):
        self.deck.shuffle()

    def deal_cards(self, player:Player, num_cards):
        ''' Deal some cards from deck to one player

        Args:
            player (object): The object of a particular player
            num (int): The number of cards to be dealed to the player
        '''
        for _ in range(num_cards):
            player.hand.append(self.deck.pop())

    def flip_top_card(self):
        ''' Flip top card when a new game starts

        Returns:
            (object): The object of the Card at the top of the deck
        '''
        top_card = self.deck.pop()
        return top_card