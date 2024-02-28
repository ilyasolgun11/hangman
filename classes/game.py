from player import Player
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from hangman import *

class Game(Player):

    def __init__(self):
        super().__init__()
        self.how_to_play_guide = how_to_play_guide

    def how_to_play(self):
        """
        Provide instructions on how to play the game.
        """
        print(self.how_to_play_guide)
        print(
            Fore.YELLOW +
            f"""Hello {
                self.name_of_player}! We suggest you to read the how to play\nguide above before you begin.\n""")
        while True:
            player_option = input(
                "A - Choose game mode\nB - Go back\nType 'a' or 'b' below\n>>> ")
            if player_option.lower() == "a":
                self.choose_game_mode()
                break
            elif player_option.lower() == "b":
                self.collect_info()
                break
            else:
                print(Fore.YELLOW + "Please enter a valid option.")
   
if __name__ == "__main__":
    game = Game()
    game.collect_info()
    