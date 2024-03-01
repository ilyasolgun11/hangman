from .gameasciiart import AsciiArt
import colorama
from colorama import Fore
colorama.init(autoreset=True)


class Player(AsciiArt):
    """
    The Player class represents the players in the hangman game.

    Attributes:
    - ascii_art (AsciiArt): An instance of the AsciiArt class for displaying ASCII art.
    - name_of_player (str): Stores the name of the player.
    - location_of_player (str): Stores the location of the player.
    """

    def __init__(self):
        """
        Initializes a new instance of the Player class.
        """
        super().__init__()
        self.ascii_art = AsciiArt()
        self.name_of_player = ""
        self.location_of_player = ""

    def collect_info(self):
        """
        Collect player information before starting the game.
        """
        print(self.ascii_art.hangman_logo)
        print(Fore.YELLOW + "Welcome! could you be the one to save this poor guy from a \ngruesome death? i hope so! fill in your name and location to\nsee the how to play guide.\n")
        while True:
            # Try statement to avoid quitting game when player attempts keyboard interruption (ctrl + c) 
            try: 
                self.name_of_player = input(
                    Fore.CYAN + "What is your first name?\n>>> ")
                if len(self.name_of_player) == 0:
                    print(Fore.YELLOW + "Please enter your name..")
                else:
                    break
            except KeyboardInterrupt:
                print(Fore.YELLOW + "KeyboardInterrupt (ctrl + c) is not allowed during input. Please try again.")

        while True:
            # Try statement to avoid quitting game when player attempts keyboard interruption (ctrl + c) 
            try:
                self.location_of_player = input(
                    Fore.CYAN + "Which country/city are your from?\n>>> ")
                if len(self.location_of_player) == 0:
                    print(Fore.YELLOW + "Please enter your name..")
                else:
                    self.how_to_play()
                    break
            except KeyboardInterrupt:
                print(Fore.YELLOW + "KeyboardInterrupt (ctrl + c) is not allowed during input. Please try again.")