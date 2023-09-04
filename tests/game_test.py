import pytest

import numpy as np
from the_game.dealer import Dealer
from the_game.game import TheGame

def test_game_init():
    num_cards = 19
    num_hand_cards = 2
    num_players = 2
    game = TheGame(num_players=num_players, num_cards=num_cards, num_hand_cards=num_hand_cards)
    game.init_game()
    assert [len(game.players[i].hand) for i in range(num_players)] == [2, 2]
    assert len(game.dealer.deck.cards) == num_cards - num_players * num_hand_cards