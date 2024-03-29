from .mixins import AsciiArtMixin, ClearTerminalMixin
import colorama
from colorama import Fore
colorama.init(autoreset=True)

special_chars = set("!@#$%^&*()-_+=[]{}|;:'\"<>,.?/¬`")


class Player(AsciiArtMixin, ClearTerminalMixin):
    """
    The Player class represents the players in the hangman game.

    Attributes:
    - ascii_art (AsciiArt): An instance of the AsciiArt
      class for displaying ASCII art.
    - name_of_player (str): Stores the name of the player.
    - location_of_player (str): Stores the location of the player.
    """

    def __init__(self):
        """
        Initializes a new instance of the Player class.
        """
        super().__init__()
        self.ascii_art = AsciiArtMixin()
        self.name_of_player = ""
        self.location_of_player = ""

    def collect_info(self):
        """
        Collect player information before starting the game.
        """
        self.clear_terminal()
        print(self.ascii_art.hangman_logo)
        print(Fore.LIGHTYELLOW_EX + "Welcome! could you be the one \
to save this poor guy from a \ngruesome death? I hope so! fill in \
your name and location to\nsee the how to play guide.\n")
        while True:
            try:
                self.name_of_player = input(
                    Fore.LIGHTCYAN_EX + "What is your first name?\n")
                if len(self.name_of_player) == 0:
                    print(Fore.LIGHTYELLOW_EX + "Please enter your name..")
                elif any(char.isdigit() for char in self.name_of_player):
                    print(Fore.LIGHTYELLOW_EX + "Your name does \
not have numbers in it... right??")
                elif ' ' in self.name_of_player:
                    print(Fore.LIGHTYELLOW_EX + "Your name cannot contain \
spaces.")
                elif any(
                    char in special_chars for char in self.name_of_player
                ):
                    print(Fore.LIGHTYELLOW_EX + "Your name cannot contain \
special characters.")
                else:
                    break
            except KeyboardInterrupt:
                print(Fore.LIGHTYELLOW_EX + "(ctrl + c) \
is not allowed during input. Please try again.")
            except EOFError:
                print(Fore.LIGHTYELLOW_EX + "(ctrl + z) \
is not allowed during input. Please try again.")

        while True:
            try:
                self.location_of_player = input(
                    Fore.LIGHTCYAN_EX + "Which country/city \
are your from?\n")
                if len(self.location_of_player) == 0:
                    print(Fore.LIGHTYELLOW_EX + "Please \
enter your location..")
                elif any(char.isdigit() for char in self.location_of_player):
                    print(Fore.LIGHTYELLOW_EX + "Please \
do not use numbers..")
                elif ' ' in self.location_of_player:
                    print(Fore.LIGHTYELLOW_EX + "Your name cannot \
contain spaces.")
                elif any(
                    char in special_chars for char in self.location_of_player
                ):
                    print(Fore.LIGHTYELLOW_EX + "Your name cannot \
contain special characters.")
                else:
                    self.how_to_play()
                    break
            except KeyboardInterrupt:
                print(Fore.LIGHTYELLOW_EX + "(ctrl + c) \
is not allowed during input. Please try again.")
            except EOFError:
                print(Fore.LIGHTYELLOW_EX + "(ctrl + z) \
is not allowed during input. Please try again.")
