from classes.game import Game
from classes.clearterminal import ClearTerminal

if __name__ == "__main__":
    ClearTerminal.clear_terminal()
    game = Game()
    game.collect_info()
