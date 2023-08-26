from the_game.deck import Deck


class Dealer:
    def __init__(self, num_cards, np_random):
        self.num_cards = num_cards
        self.np_random = np_random
        self.deck = Deck(num_cards, np_random)
        self.shuffle()

    def shuffle(self):
        self.deck.shuffle()

    def deal_cards(self, player, num):
        ''' Deal some cards from deck to one player

        Args:
            player (object): The object of a particular player
            num (int): The number of cards to be dealed to the player
        '''
        for _ in range(num):
            player.hand.append(self.deck.pop())

    def flip_top_card(self):
        ''' Flip top card when a new game starts

        Returns:
            (object): The object of the Card at the top of the deck
        '''
        top_card = self.deck.pop()
        return top_card