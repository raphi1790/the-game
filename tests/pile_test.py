import pytest

import numpy as np
from the_game.card import Card
from the_game.pile import Pile

def test_pile_init():
    pile = Pile(min_value=1, max_value=15, direction="down")
    assert pile.direction == "down"
    assert pile.current_value == 15
    assert pile.min_value == 1
    assert pile.max_value == 15

def test_set_card():
    pile = Pile(min_value=1, max_value=15, direction="down")
    card = Card(7)
    pile.set_card(card)
    assert pile.direction == "down"
    assert pile.current_value == card.rank == 7
    assert pile.min_value == 1
    assert pile.max_value == 15