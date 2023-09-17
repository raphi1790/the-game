from the_game.card import Card


class Deck:
    def __init__(self, min_card, max_card, np_random=None):
        self.np_random = np_random
        self.min_card = min_card
        self.max_card = max_card
        self.cards = [Card(i) for i in range(min_card,max_card+1)]
    
    def shuffle(self) :
        self.np_random.shuffle(self.cards)
    
    def pop(self):
        return self.cards.pop()
        