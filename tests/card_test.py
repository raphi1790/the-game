
import unittest
from the_game.card import Card

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = Card(110)
        self.assertEqual(str(card), "Card of rank 110")

if __name__ == '__main__':
    unittest.main()