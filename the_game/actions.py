from the_game.card import Card
from the_game.pile import Pile


class Action:
    def __init__(self, player_id, mode, card: Card = None, pile: Pile= None):
        self.player_id = player_id
        self.mode = mode
        self.card = card
        self.pile = pile

    def __str__(self):
        return (self.player_id, self.mode, self.card, self.pile)