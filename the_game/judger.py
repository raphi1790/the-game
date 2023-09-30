from typing import List
from the_game.actions import Action
from the_game.card import Card
from the_game.dealer import Dealer
from the_game.pile import Pile
from the_game.player import Player


class Judger:
    def __init__(self) -> None:
        pass
    
    def is_valid_card(self, card: Card, pile: Pile):
        
        if pile.direction == "up" & card.rank > pile.current_value:
            return True
        if pile.direction == "down" & card.rank < pile.current_value:
            return True
        # Special case in The Game
        if pile.direction == "up" & pile.current_value - card.rank == 10:
            return True
        # Special case in The Game
        if self.direction == "down" & card.rank - pile.current_value == 10:
            return True
        return False
  
    def get_legal_actions(self, state):
        legal_actions = []
        player = state['current_player']
        piles = state['piles']
        previous_actions = state['actions']
        hand = player.hand
        for card in hand:
            for pile in piles:
                if self.is_valid_card(card, pile):
                    legal_actions.append(Action(player.player_id, "play", card, pile))
        
        if len(previous_actions)>0:
            last_action = previous_actions[-1]
            if last_action.player_id == player.player_id & len(dealer.deck.cards)==0:
                legal_actions.append(Action(player.player_id, 'change_player', None, None))
        
        if len(previous_actions)>1:
            second_last_action = previous_actions[-2]
            if second_last_action.player_id == player.player_id & last_action.player_id == player.player_id:
                legal_actions.append(Action(player.player_id, 'change_player', None, None))

        return legal_actions


        
    
