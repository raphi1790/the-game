
import unittest

import numpy as np
from the_game.deck import Deck

class TestDeck(unittest.TestCase):
    def test_deck_creation(self):
        num_cards = 15
        np_random = np.random.RandomState(42)
        deck = Deck(num_cards, np_random)
        self.assertEqual(len(deck.cards), num_cards)
        self.assertEqual(str(deck.cards[num_cards-1]), "Card of rank 15")
    
    def test_deck_shuffle(self):
        num_cards = 15
        np_random = np.random.RandomState(42)
        deck = Deck(num_cards, np_random=np_random)
        deck.shuffle()
        self.assertEqual(len(deck.cards), num_cards)
        self.assertEqual(str(deck.cards[0]), "Card of rank 10")
        self.assertEqual(str(deck.cards[num_cards - 1]), "Card of rank 7")

if __name__ == '__main__':
    unittest.main()