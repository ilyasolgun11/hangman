import colorama
import os
from colorama import Fore
colorama.init(autoreset=True)


class ClearTerminalMixin:
    """
    Clears the terminal above of where it is placed
    """

    @staticmethod
    # Taken from https://www.delftstack.com/howto/python/python-clear-console/
    def clear_terminal():
        command = 'clear'
        if os.name in (
                'nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

        print("\033c", end="")


class AsciiArtMixin:
    """
    Contains Ascii art to be used across the games classes
    """
    def __init__(self):
        self.hangman_stages = [
            Fore.LIGHTGREEN_EX + """
________________________________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
__|/\\/|______________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
""",
            Fore.LIGHTGREEN_EX + """
________________________________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|
  |/\\/|                        |
  |/\\/|                        |
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
__|/\\/|______________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
""",
            Fore.LIGHTGREEN_EX + """
________________________________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|
  |/\\/|                   z    |
  |/\\/|                    z __|__
  |/\\/|                    ('- o -')
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
__|/\\/|______________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
""",
            Fore.LIGHTYELLOW_EX + """
________________________________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|
  |/\\/|                        |
  |/\\/|                      __|__
  |/\\/|                    ('- _ o')
  |/\\/|                       |||
  |/\\/|                       |||
  |/\\/|                       |||
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
__|/\\/|______________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
""",
            Fore.LIGHTYELLOW_EX + """
________________________________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|
  |/\\/|                        |
  |/\\/|                      __|__
  |/\\/|                    ('O _ O')
  |/\\/|                     ./|||
  |/\\/|                    ./ |||
  |/\\/|                       |||
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|
__|/\\/|______________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
""",
            Fore.LIGHTRED_EX + """
________________________________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|
  |/\\/|                        |
  |/\\/|                      __|__
  |/\\/|                   ? (o _ O')
  |/\\/|                     ./|||\\.
  |/\\/|                    ./ ||| \\.
  |/\\/|                       |||
  |/\\/|
  |/\\/|
  |/\\/|
  |/\\/|             TOO CLOSE FOR COMFORT
  |/\\/|
  |/\\/|
  |/\\/|
__|/\\/|______________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
""",
            Fore.LIGHTRED_EX + """
________________________________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|
  |/\\/|                        |
  |/\\/|                      __|__
  |/\\/|                    ('O _ o) ?!
  |/\\/|                     ./|||\\.
  |/\\/|                    ./ ||| \\.
  |/\\/|                       |||
  |/\\/|                     ./
  |/\\/|                    _/
  |/\\/|
  |/\\/|             1 MORE AND HE'S A GONER
  |/\\/|
  |/\\/|
  |/\\/|
__|/\\/|______________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
"""
        ]
        self.hangman_logo = Fore.LIGHTGREEN_EX + """\n\n\n
    ______________________________
    |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
        |/\\/|                  __|__
        |/\\/|                ('x _ x')
        |/\\/|                 ./|||\\.
        |/\\/|                ./ ||| \\.
        |/\\/|                   |||
        |/\\/|                 ./   \\.
        |/\\/|                _/     \\_
   _____|/\\/|____________________  ____________
  / / / / / /_  __/  _/  |/  /   |/_  __/ ____/
 / / / / /   / /  / // /|_/ / /| | / / / __/
/ /_/ / /___/ / _/ // /  / / ___ |/ / / /___
\\____/_____/_/ /___/_/__/_/_/__|_/_/_/_____/_ ______    __  __
                / / / /   |  / | / / ____/  |/  /   |  / | / /
               / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ /
              / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /
             /_/ /_/_/  |_/_/ |_/\\____/_/  /_/_/  |_/_/ |_/
"""
        self.lose_logo_hangman = Fore.LIGHTRED_EX + """\n\n\n
    ______________________________
    |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
        |/\\/|                  __|__
        |/\\/|                ('x _ x')
        |/\\/|                 ./|||\\.
        |/\\/|                ./ ||| \\.  Y O U   L O S T!
        |/\\/|                   |||
        |/\\/|                 ./   \\.
        |/\\/|                _/     \\_
   _____|/\\/|____________________  ___________
  / / / / / /_  __/  _/  |/  /   |/_  __/ ____/
 / / / / /   / /  / // /|_/ / /| | / / / __/
/ /_/ / /___/ / _/ // /  / / ___ |/ / / /___
\\____/_____/_/ /___/_/__/_/_/__|_/_/_/_____/_ __ ___   __  __
                / / / /   |  / | / / ____/  |/  /   |  / | / /
               / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ /
              / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /
             /_/ /_/_/  |_/_/ |_/\\____/_/  /_/_/  |_/_/ |_/
"""
        self.win_logo_hangman = Fore.LIGHTGREEN_EX + """\n\n\n
    ______________________________
    |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
        |/\\/|                   ✂
        |/\\/|                  _____
        |/\\/|                ('O ^ O')
        |/\\/|                 ./|||\\.
        |/\\/|                ./ ||| \\.  Y O U   W O N !
        |/\\/|                   |||
        |/\\/|                 ./   \\.
   _____|/\\/|_______________ _/__  _\\_ ______
  / / / / / /_  __/  _/  |/  /   |/_  __/ ____/
 / / / / /   / /  / // /|_/ / /| | / / / __/
/ /_/ / /___/ / _/ // /  / / ___ |/ / / /___
\\____/_____/_/ /___/_/__/_/_/__|_/_/_/_____/_ __ ____  __  __
                / / / /   |  / | / / ____/  |/  /   |  / | / /
               / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ /
              / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /
             /_/ /_/_/  |_/_/ |_/\\____/_/  /_/_/  |_/_/ |_/
"""
        self.how_to_play_guide = Fore.LIGHTBLUE_EX + """
 ______________________________________________________________
|                                                              |
|                    H O W   T O   P L A Y :                   |
|    Game Rules:                                               |
|    1 - You will have 7 attempts to guess the right word      |
|    by guessing the word outright or guessing with letters.   |
|    2 - If you guess wrong, hangman will start to build       |
|    and if you have more than 15 points, they will be         |
|    deducted by 10 each time.                                 |
|    3 - If the attempts reach 0, hangman will be killed       |
|    and you will lose the game.                               |
|    4 - Each time you play and your attempts reach 3          |
|    you will get a hint token, if you use it you will get     |
|    the definition of the word but also 25 points             |
|    will be deducted if you have more than 25 already.        |
|                                                              |
|    Points system:                                            |
|   + 25 points each time you guess a letter right             |
|   + 100 points if you guess the word right with half of      |
|      the word exposed                                        |
|   + 750 points if you guess the word right without           |
|    revealing the first half of the word already              |
|   - 10 points if you guess a letter wrong, only applies if   |
|    your points are more than 15 already.                     |
|   - 100% points, you will lose all your points if you        |
|    guess the word wrong.                                     |
|______________________________________________________________|
"""
        self.game_modes_display = Fore.LIGHTBLUE_EX + """
 ______________________________________________________________
|                                                              |
|                                                              |
|                     G A M E   M O D E S                      |
|                                                              |
|     Easy mode:                                               |
|     Consists of words less than 5 letters in length          |
|                                                              |
|     Intermediate mode:                                       |
|     Consists of words with more than 5 or less than          |
|     8 letters in length                                      |
|                                                              |
|     Hard mode:                                               |
|     Consists of words more than 8 letters in length          |
|                                                              |
|     Country mode:                                            |
|     Consists of 195 countries with diverse name lengths      |
|                                                              |
|______________________________________________________________|

"""

    def thank_user(self, name, times_won, location):
        if times_won > 0:
            if times_won >= 2:
                times = f" {times_won} TIMES!"
            else:
                times = "!"
            print(Fore.LIGHTGREEN_EX + f"""\n\n\n
    ______________________________
    |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
        |/\\/|
        |/\\/|    THANK YOU FOR PLAYING {name.upper()}
        |/\\/|
        |/\\/|    YOU HAVE SAVED HANGMAN{times}
        |/\\/|
        |/\\/|    {location.upper()} IS AN AWESOME PLACE!
        |/\\/|
   _____|/\\/|____________________  ____________
  / / / / / /_  __/  _/  |/  /   |/_  __/ ____/
 / / / / /   / /  / // /|_/ / /| | / / / __/
/ /_/ / /___/ / _/ // /  / / ___ |/ / / /___
\\____/_____/_/ /___/_/__/_/_/__|_/_/_/_____/_ ______   __  __
                / / / /   |  / | / / ____/  |/  /   |  / | / /
               / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ /
              / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /
             /_/ /_/_/  |_/_/ |_/\\____/_/  /_/_/  |_/_/ |_/
""")
        else:
            print(Fore.LIGHTGREEN_EX + f"""\n\n\n
    ______________________________
    |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
        |/\\/|
        |/\\/|
        |/\\/|
        |/\\/|    THANK YOU FOR PLAYING {name.upper()}
        |/\\/|
        |/\\/|
        |/\\/|
   _____|/\\/|____________________  ____________
  / / / / / /_  __/  _/  |/  /   |/_  __/ ____/
 / / / / /   / /  / // /|_/ / /| | / / / __/
/ /_/ / /___/ / _/ // /  / / ___ |/ / / /___
\\____/_____/_/ /___/_/__/_/_/__|_/_/_/_____/_ ______   __  __
                / / / /   |  / | / / ____/  |/  /   |  / | / /
               / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ /
              / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /
             /_/ /_/_/  |_/_/ |_/\\____/_/  /_/_/  |_/_/ |_/
""")
