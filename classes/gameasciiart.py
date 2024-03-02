import colorama
from colorama import Fore
colorama.init(autoreset=True)


class AsciiArt:
    def __init__(self):
        self.hangman_stages = [
            Fore.GREEN + """
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
            Fore.GREEN + """
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
            Fore.GREEN + """
________________________________
|/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|
  |/\\/|                        |
  |/\\/|                      __|__
  |/\\/|                    ('- _ -')
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
            Fore.YELLOW + """
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
            Fore.YELLOW + """
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
            Fore.RED + """
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
            Fore.RED + """
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
        self.hangman_logo = Fore.GREEN + """\n\n\n
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
\\____/_____/_/ /___/_/__/_/_/__|_/_/_/_____/_ __ ____   __  __
                / / / /   |  / | / / ____/  |/  /   |  / | / /
               / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ /
              / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /
             /_/ /_/_/  |_/_/ |_/\\____/_/  /_/_/  |_/_/ |_/
"""
        self.lose_logo_hangman = Fore.RED + """\n\n\n
    ______________________________
    |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
        |/\\/|                  __|__
        |/\\/|                ('x _ x')
        |/\\/|                 ./|||\\.
        |/\\/|                ./ ||| \\.  Y O U   L O S T!
        |/\\/|                   |||
        |/\\/|                 ./   \\.
        |/\\/|                _/     \\_
   _____|/\\/|____________________  ______ _____
  / / / / / /_  __/  _/  |/  /   |/_  __/ ____/
 / / / / /   / /  / // /|_/ / /| | / / / __/
/ /_/ / /___/ / _/ // /  / / ___ |/ / / /___
\\____/_____/_/ /___/_/__/_/_/__|_/_/_/_____/_ __ ____   __  __
                / / / /   |  / | / / ____/  |/  /   |  / | / /
               / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ /
              / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /
             /_/ /_/_/  |_/_/ |_/\\____/_/  /_/_/  |_/_/ |_/
"""
        self.win_logo_hangman = Fore.GREEN + """\n\n\n
    ______________________________
    |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\|
        |/\\/|                   ✂
        |/\\/|                  _____
        |/\\/|                ('O ^ O')
        |/\\/|                 ./|||\\.
        |/\\/|                ./ ||| \\.  Y O U   W O N !
        |/\\/|                   |||
        |/\\/|                 ./   \\.
   _____|/\\/|_______________ _/__  _\\_ ________
  / / / / / /_  __/  _/  |/  /   |/_  __/ ____/
 / / / / /   / /  / // /|_/ / /| | / / / __/
/ /_/ / /___/ / _/ // /  / / ___ |/ / / /___
\\____/_____/_/ /___/_/__/_/_/__|_/_/_/_____/_ __ ____   __  __
                / / / /   |  / | / / ____/  |/  /   |  / | / /
               / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ /
              / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /
             /_/ /_/_/  |_/_/ |_/\\____/_/  /_/_/  |_/_/ |_/
"""
        self.how_to_play_guide = Fore.BLUE + """
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
        self.game_modes_display = """
 ______________________________________________________________
|                                                              |
|                                                              |
|                     """ + Fore.CYAN + """G A M E   M O D E S :""" + Fore.WHITE + """                    |
|                                                              |
|     """ + Fore.GREEN + """Easy mode:""" + Fore.WHITE + """                                               |
|     Consists of words less than 5 letters in length          |
|                                                              |
|     """ + Fore.YELLOW + """Intermediate mode:""" + Fore.WHITE + """                                       |
|     Consists of words with more than 5 or less than          |
|     8 letters in length                                      |
|                                                              |
|     """ + Fore.RED + """Hard mode:""" + Fore.WHITE + """                                               |
|     Consists of words more than 8 letters in length          |
|                                                              |
|     """ + Fore.CYAN + """Country mode:""" + Fore.WHITE + """                                            |      
|     Consists of 195 countries with diverse name lengths      |
|                                                              |
|______________________________________________________________|

"""
