import pytest

import numpy as np
from the_game.dealer import Dealer
from the_game.player import Player


def test_dealer_init():
    num_cards = 15
    np_random = np.random.RandomState(42)
    dealer = Dealer(num_cards, np_random)
    assert len(dealer.deck.cards) == num_cards
    assert dealer.deck.cards[0].rank == 10
    assert dealer.deck.cards[num_cards - 1].rank == 7

def test_deal():
    np_random = np.random.RandomState(42)
    num_cards = 15
    player_id = 0
    dealer = Dealer(num_cards, np_random)
    player = Player(player_id, np_random)
    dealer.deal_cards(player, 7)
    assert len(player.hand) == 7
    assert player.hand[0].rank == 7
    assert [card.rank for card in player.hand] == [7, 4, 13, 11, 8, 5, 15] 
        
