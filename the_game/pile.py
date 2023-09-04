from the_game.card import Card


class Pile:
    def __init__(self, min_value, max_value, direction, card:Card) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = card.rank 
        if direction == "up":
            self.direction = "up"
        else:
            self.direction = "down"
 

    def set_card(self, card):
        self.current_value = card.rank
        