from copy import deepcopy
import numpy as np

from the_game.dealer import Dealer
from the_game.judger import Judger
from the_game.pile import Pile
from the_game.player import Player


class TheGame:

    def __init__(self, allow_step_back=False, num_players=2, min_card=1, max_card=15, num_hand_cards=3, current_player_id=0):
        self.allow_step_back = allow_step_back
        self.np_random = np.random.RandomState()
        self.num_players = num_players
        self.payoffs = [0 for _ in range(self.num_players)]
        self.min_card = min_card
        self.max_card = max_card
        self.num_hand_cards = num_hand_cards   
        self.current_player_id = current_player_id
        self.actions = []

    def configure(self, game_config):
        ''' Specifiy some game specific parameters, such as number of players
        '''
        self.num_players = game_config['game_num_players']

    def init_game(self):
        ''' Initialize players and state

        Returns:
            (tuple): Tuple containing:

                (dict): The first state in one game
                (int): Current player's id
        '''
        # Initalize payoffs
        self.payoffs = [0 for _ in range(self.num_players)]

        # Initialize a dealer that can deal cards
        self.dealer = Dealer(min_card=self.min_card, max_card=self.max_card, np_random=self.np_random)

        # Initialize four players to play the game
        self.players = [Player(i, self.np_random) for i in range(self.num_players)]

        # Deal cards to each player to prepare for the game
        for player in self.players:
            self.dealer.deal_cards(player, self.num_hand_cards)

        
        self.piles = [Pile(min_value=self.min_card, max_value=self.max_card, direction="up") for _ in range(2)] + [Pile(min_value=self.min_card, max_value=self.max_card, direction="down") for _ in range(2)] 

        


    # def step(self, action):
    #     ''' Get the next state

    #     Args:
    #         action (str): A specific action

    #     Returns:
    #         (tuple): Tuple containing:

    #             (dict): next player's state
    #             (int): next plater's id
    #     '''

    #     if self.allow_step_back:
    #         # First snapshot the current state
    #         his_dealer = deepcopy(self.dealer)
    #         his_round = deepcopy(self.round)
    #         his_players = deepcopy(self.players)
    #         self.history.append((his_dealer, his_players, his_round))

    #     self.round.proceed_round(self.players, action)
    #     player_id = self.round.current_player
    #     state = self.get_state(player_id)
    #     return state, player_id

    # def step_back(self):
    #     ''' Return to the previous state of the game

    #     Returns:
    #         (bool): True if the game steps back successfully
    #     '''
    #     if not self.history:
    #         return False
    #     self.dealer, self.players, self.round = self.history.pop()
    #     return True

    def get_state(self):
        ''' Return the game's state

        Args:
            player_id (int): player id

        Returns:
            (dict): The state of the game
        '''
        state = dict()
        state['num_players'] = self.num_players
        state['current_player'] = self.players[self.current_player_id]
        state['players'] = self.players
        state['piles'] = self.piles
        state['deck'] = self.dealer.deck
        state['actions'] = self.actions
        return state

    # def get_payoffs(self):
    #     ''' Return the payoffs of the game

    #     Returns:
    #         (list): Each entry corresponds to the payoff of one player
    #     '''
    #     winner = self.round.winner
    #     if winner is not None and len(winner) == 1:
    #         self.payoffs[winner[0]] = 1
    #         self.payoffs[1 - winner[0]] = -1
    #     return self.payoffs

    # def get_legal_actions(self):
    #     ''' Return the legal actions for current player

    #     Returns:
    #         (list): A list of legal actions
    #     '''

    #     return self.round.get_legal_actions(self.players, self.round.current_player)

    # def get_num_players(self):
    #     ''' Return the number of players in Limit Texas Hold'em

    #     Returns:
    #         (int): The number of players in the game
    #     '''
    #     return self.num_players

    # @staticmethod
    # def get_num_actions():
    #     ''' Return the number of applicable actions

    #     Returns:
    #         (int): The number of actions. There are 61 actions
    #     '''
    #     return 61

    # def get_player_id(self):
    #     ''' Return the current player's id

    #     Returns:
    #         (int): current player's id
    #     '''
    #     return self.round.current_player

    # def is_over(self):
    #     ''' Check if the game is over

    #     Returns:
    #         (boolean): True if the game is over
    #     '''
    #     return self.round.is_over