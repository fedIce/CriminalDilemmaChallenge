from os.path import dirname, basename, isfile, join
import glob, json
ROOT_MODULES_DIR = f'{dirname(__file__)}\modules'
MODULES_DIR = join(ROOT_MODULES_DIR, "*.py")

modules = glob.glob(MODULES_DIR)
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

print(__all__)

class Tournament:
    def __init__(self, number_of_cycles = 10):
        self.scores = dict()
        self.players = __all__
        self.cycle_index = 0
        self.cycles = number_of_cycles

    def calculate_score(self, player_answer, opponent_answer):
        if player_answer == 1 and opponent_answer == 1:
            return 10
        if player_answer == 0 and opponent_answer == 1:
            return 0
        if player_answer == 0 and opponent_answer == 0:
            return 5
        if player_answer == 1 and opponent_answer == 0:
            return 20

    
    def score_round(self, player, player_answer, opponent_answer): 
        if player in dict(self.scores.keys()):
            scores = self.scores[player]
        else:
            scores = {
                f'{player}': []
            }
        
        scores[player] = scores[player].append(self.calculate_score(player_answer, opponent_answer))


    def run_tornament(self, challenger, opponent=0):
        src = f'{ROOT_MODULES_DIR}\\{self.players[challenger]}.py'
        # src = f'{ROOT_MODULES_DIR}\\{self.players[opponent]}.py'

        with open(src, mode="r", encoding="utf-8") as c:
            code = c.read()

        code = compile(code, '<string>','exec')
        print(code)
        for x in range(1, self.cycles):
            exec(code,{"__builtins__": {"min": min, "print": print, 'int':int, 'bool':bool}, 'cycle_index': x, 'prev_answer': 1},{})

tournament = Tournament(10)
tournament.run_tornament(challenger=__all__.index(__all__[0]))