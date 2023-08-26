from the_game.card import Card


class Deck:
    def __init__(self, num_cards=10, np_random=None):
        self.np_random = np_random
        self.num_cards = num_cards
        self.cards = [Card(i) for i in range(1,self.num_cards+1)]
    
    def shuffle(self) :
        self.np_random.shuffle(self.cards)
    
    def pop(self):
        return self.cards.pop()
        