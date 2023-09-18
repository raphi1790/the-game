from the_game.card import Card


class Pile:
    def __init__(self, min_value, max_value, direction) -> None:
        self.min_value = min_value
        self.max_value = max_value
        if direction == "up":
            self.direction = "up"
            self.current_value = min_value
        else:
            self.direction = "down"
            self.current_value = max_value
 

    def play_card(self, card):
        self.current_value = card.rank
        