from classes.game import Game
from classes.mixins import ClearTerminalMixin

if __name__ == "__main__":
    ClearTerminalMixin.clear_terminal()
    game = Game()
    game.collect_info()
