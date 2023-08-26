
import unittest

import numpy as np
from the_game.dealer import Dealer
from the_game.player import Player

class TestDealer(unittest.TestCase):
    def test_dealer_init(self):
        num_cards = 15
        np_random = np.random.RandomState(42)
        dealer = Dealer(num_cards, np_random)
        self.assertEqual(len(dealer.deck.cards), num_cards)
        self.assertEqual(str(dealer.deck.cards[0]), "Card of rank 10")
        self.assertEqual(str(dealer.deck.cards[num_cards - 1]), "Card of rank 7")
    

    def test_deal(self):
        np_random = np.random.RandomState(42)
        num_cards = 15
        player_id = 0
        dealer = Dealer(num_cards, np_random)
        player = Player(player_id, np_random)
        dealer.deal_cards(player, 7)
        self.assertEqual(len(player.hand), 7)
        self.assertEqual(str(player.hand[0]), "Card of rank 7")
        


if __name__ == '__main__':
    unittest.main()