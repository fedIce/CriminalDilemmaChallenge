from typing import Protocol

class Player(Protocol):

    grudge = 0

    def __init__(self):
        self.grudge = 0

    def play(self, opponent_reply:bool, cycle_index:int) -> bool:
        '''Play round'''
        ...

    def hold_grudge(self, opponent_reply:bool) -> None:
        '''update grudge variable'''
        ...

    def check_grudge(self) -> bool:
        '''check if this player is currently holding a grudge'''
        ...

    def update_grudge(self, amount) -> None:
        '''Update players grudge'''