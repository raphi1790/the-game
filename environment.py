import jax
import jax.numpy as jnp
from jax import random
from jax import jit
from functools import partial

class TheGame:
    def __init__(self):
        self.number_of_cards = 12
        self.number_of_players = 1
        self.number_of_piles = 1
        self.number_of_hand_cards = 4


    def _maybe_reset(self, env_state, done):
      key = env_state[1]
      return jax.lax.cond(done, self._reset, lambda key: env_state, key)
    
    def _get_obsv(self, state):
        obsv = dict(player_hands=state["player_hands"],
        remaining_cards=state["remaining_cards"],
        pile=state["pile"],
        number_of_piles=state["number_of_piles"],
        number_of_cards=state["number_of_cards"], 
        number_of_hand_cards=state["number_of_hand_cards"], 
        )
        return obsv

    @partial(jit, static_argnums=(0,))
    def step(self, env_state, action):
        pass

    def _initialize_game(self, key):
        deck = random.permutation(key,jnp.arange(1, self.number_of_cards+1))

        # deal the cards
        hands = [deck[i*self.number_of_hand_cards:(i+1)*self.number_of_hand_cards] for i in range(self.number_of_players)]

        # add the remaining deck to a new list
        remaining_deck = deck[self.number_of_players*self.number_of_hand_cards:]

        # sort the remaining deck in order to get all remainind cards without an order
        remaining_cards = remaining_deck.sort()

        # initialiize the pile
        pile = jnp.empty((0,))
        
        new_state = dict(player_hands=hands, 
            remaining_deck=remaining_deck,
            remaining_cards=remaining_cards,
            pile=pile,
            number_of_players=self.number_of_players,
            number_of_piles=self.number_of_piles,
            number_of_cards=self.number_of_cards, 
            number_of_hand_cards=self.number_of_hand_cards, 
            original_deck=deck)
        new_key = random.split(key)[0]

        return new_state, new_key
        

    @partial(jit, static_argnums=(0,))
    def reset(self, key):
        env_state = self._initialize_game(key)
        initial_state = env_state[0]
        return  env_state, self._get_obsv(initial_state)
