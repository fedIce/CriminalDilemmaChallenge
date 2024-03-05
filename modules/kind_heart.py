from modules.base import Player
import random

class Player1(Player):
    def __init__(self):
        self.grudge = 0
    
    def play(self, opponent_reply: bool) -> bool:

        self.update_grudge()
        self.hold_grudge(opponent_reply) # first check if player should hold a grudge on opponent and update the player's grudge accordingly
        
        if self.check_grudge(): # 
            return False
        else:
            return random.choices([True, False],[1,1])[0]

    def hold_grudge(self, opponent_reply: bool=False) -> None:
        if not opponent_reply:
            self.update_grudge(5)
    
    def update_grudge(self, amount: int = 0) -> None:
        '''
            if amount is positive, this means the player is increasing their grudge by that amount,
            if amount is 0, the player will forgive 1 grudge for that play cycle.
        '''
        if amount > 0:
            self.grudge = self.grudge +  amount
        else:
            if self.grudge > 0:
                self.grudge = self.grudge - 1
    

























    # current_cycle_index = cycle_index
# last_players_answer = prev_answer

# grudge = 0
# ans = 0

# if last_players_answer == '0':
#     grudge = 2 + int(current_cycle_index)

# if int(current_cycle_index) < grudge:
#     print(f'{ans =}')
# else:
#     print(f'{ans =}')