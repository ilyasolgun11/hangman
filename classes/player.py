import colorama
from colorama import Fore
colorama.init(autoreset=True)
from hangman import *

class Player:
    def __init__(self):
        self.name_of_player = ""
        self.location_of_player = ""
        self.game_logo = hangman_logo

    def collect_info(self):
        """
        Collect player information before starting the game.
        """
        print(self.game_logo)
        print(Fore.YELLOW + "Welcome! could you be the one to save this poor guy from a \ngruesome death? i hope so! fill in your name and location to\nsee the how to play guide.\n")
        while True:
            self.name_of_player = input(
                Fore.CYAN + "What is your first name?\n>>> ")
            if len(self.name_of_player) == 0:
                print(Fore.YELLOW + "Please enter your name..")
            else:
                break

        while True:
            self.location_of_player = input(
                Fore.CYAN + "Which country/city are your from?\n>>> ")
            if len(self.location_of_player) == 0:
                print(Fore.YELLOW + "Please enter your name..")
            else:
                self.how_to_play()
                break