
import pytest

import numpy as np
from the_game.deck import Deck

def test_deck_creation():
    num_cards = 15
    np_random = np.random.RandomState(42)
    deck = Deck(num_cards, np_random)
    assert len(deck.cards) == num_cards
    assert str(deck.cards[num_cards-1]) == "Card of rank 15"

def test_deck_shuffle():
    num_cards = 15
    np_random = np.random.RandomState(42)
    deck = Deck(num_cards, np_random=np_random)
    deck.shuffle()
    assert len(deck.cards) == num_cards
    assert str(deck.cards[0]) == "Card of rank 10"
    assert str(deck.cards[num_cards - 1]) == "Card of rank 7"

