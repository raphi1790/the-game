import pytest

import numpy as np
from the_game.dealer import Dealer
from the_game.player import Player


def test_dealer_init():
    min_card = 1
    max_card = 15
    np_random = np.random.RandomState(42)
    dealer = Dealer(min_card, max_card, np_random)
    assert len(dealer.deck.cards) == max_card - min_card - 1
    assert dealer.deck.cards[0].rank == 13
    assert dealer.deck.cards[max_card - min_card - 2].rank == 8

def test_deal():
    np_random = np.random.RandomState(42)
    min_card = 1
    max_card = 15
    player_id = 0
    dealer = Dealer(min_card, max_card, np_random)
    player = Player(player_id, np_random)
    dealer.deal_cards(player, 7)
    assert len(player.hand) == 7
    assert [card.rank for card in player.hand] == [8, 5, 12, 9, 6, 14, 3] 
    assert len(dealer.deck.cards) == max_card - min_card - 1 - 7
        
