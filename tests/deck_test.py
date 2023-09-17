
import pytest

import numpy as np
from the_game.deck import Deck

def test_deck_creation():
    min_card = 1
    max_card = 15
    np_random = np.random.RandomState(42)
    deck = Deck(min_card+1, max_card-1, np_random)
    assert len(deck.cards) == max_card - min_card - 1
    assert deck.cards[max_card-min_card-2].rank == max_card - 1

def test_deck_shuffle():
    min_card = 1
    max_card = 15
    np_random = np.random.RandomState(42)
    deck = Deck(min_card+1, max_card-1, np_random)
    deck.shuffle()
    assert len(deck.cards) == max_card - min_card - 1
    assert deck.cards[0].rank == 13
    assert deck.cards[max_card-min_card-2].rank == 8

