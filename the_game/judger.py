from the_game.card import Card
from the_game.pile import Pile


class Judger:
    def __init__(self) -> None:
        pass
    
    def is_valid_card(self, card: Card, pile: Pile):
        if pile.direction == "up" & card.rank > pile.current_value:
            return True
        if pile.direction == "down" & card.rank < pile.current_value:
            return True
        # Special case in The Game
        if pile.direction == "up" & pile.current_value - card.rank == 10:
            return True
        # Special case in The Game
        if self.direction == "down" & card.rank - pile.current_value == 10:
            return True
        return False
        
    
