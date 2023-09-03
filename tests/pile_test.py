import pytest

import numpy as np
from the_game.pile import Pile

def test_pile_zero():
    card_value = 0
    pile = Pile(card_value)
    assert pile.direction == "up"
    assert pile.current_value == pile.inital_value == card_value

def test_pile_not_zero():
    card_value = 15
    pile = Pile(card_value)
    assert pile.direction == "down"
    assert pile.current_value == pile.inital_value == card_value