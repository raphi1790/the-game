import pytest

import numpy as np
from the_game.dealer import Dealer
from the_game.game import TheGame

def test_game_init():
    min_card = 1
    max_card = 15
    num_hand_cards = 2
    num_players = 2
    game = TheGame(num_players=num_players, min_card=min_card,max_card=max_card, num_hand_cards=num_hand_cards)
    game.init_game()
    assert [len(game.players[i].hand) for i in range(num_players)] == [2, 2]
    origin_deck_size = max_card - min_card - 1
    assert len(game.dealer.deck.cards) == origin_deck_size - num_players * num_hand_cards
    assert len(game.piles) == 4
    directions = ["up", "up", "down", "down"]
    values = [min_card, min_card, max_card, max_card]
    assert [game.piles[i].direction for i in range(4)] == directions
    assert [game.piles[i].current_value for i in range(4)] == values