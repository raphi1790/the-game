class Pile:
    def __init__(self, value=0) -> None:
        self.inital_value = value
        self.current_value = value
        if value == 0:
            self.direction = "up"
        else:
            self.direction = "down"


    def set_card(self, card):
        self.current_value = card.rank
        