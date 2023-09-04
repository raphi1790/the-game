import pytest

import numpy as np
from the_game.card import Card
from the_game.pile import Pile

def test_pile_init():
    card = Card(10)
    pile = Pile(min_value=0, max_value=15, direction="down", card=card)
    assert pile.direction == "down"
    assert pile.current_value == card.rank == 10
    assert pile.min_value == 0
    assert pile.max_value == 15

def test_set_card():
    card_1 = Card(12)
    pile = Pile(min_value=0, max_value=15, direction="down", card=card_1)
    card_2 = Card(7)
    pile.set_card(card_2)
    assert pile.direction == "down"
    assert pile.current_value == card_2.rank == 7
    assert pile.min_value == 0
    assert pile.max_value == 15