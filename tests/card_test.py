import pytest

from the_game.card import Card

def test_card_creation():
    card = Card(110)
    assert str(card) == "Card of rank 110"