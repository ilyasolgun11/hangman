import time
import sys
from datetime import datetime
from .player import Player
from .leaderboard import Leaderboard
from .words import RandomWord
from .mixins import AsciiArtMixin, ClearTerminalMixin
from .hinttoken import HintToken
import colorama
from colorama import Fore
colorama.init(autoreset=True)


class Game(Player, Leaderboard, RandomWord, AsciiArtMixin, ClearTerminalMixin,
           HintToken):
    """
    The Game class represents the main Hangman game.

    Attributes:
    - start_time (float): The start time of the game.
    - player_won (bool): Indicates whether the player won the game.
    - selected_worksheet (str): The selected game mode worksheet.
    - ascii_art (AsciiArt): An instance of the AsciiArt class for
      displaying ASCII art.
    - hangman_word (str): The current hangman word to be guessed.
    - display_word (str): The partially revealed word based on user guesses.
    - stages (int): The number of stages of the hangman
      (visual representation).
    - hints_remaining (int): The number of hint tokens remaining.
    - score (int): The player's score.
    - points (int): The points earned during the game.
    - guessed_letters (list): List of guessed letters.
    - guessed_words (list): List of guessed words.
    - guessed_correct_letters (list): List of correctly guessed letters.
    - game_hint_message (str): Message related to hints during the game.
    """

    def __init__(self):
        """
        Initializes a new instance of the Hangman game.
        """
        super().__init__()
        self.start_time = None
        self.player_won = False
        self.selected_worksheet = "easy mode"
        self.ascii_art = AsciiArtMixin()
        self.hangman_word = self.game_modes("easy mode")
        self.display_word = "_" * \
            len(self.hangman_word)
        self.stages = 0
        self.hints_remaining = 1
        self.score = 7
        self.points = 0
        self.guessed_letters = []
        self.guessed_words = []
        self.guessed_correct_letters = []
        self.game_hint_message = ""
        self.times_player_won = 0

    def how_to_play(self):
        """
        Provide instructions on how to play the game and informs
        player of the points system.
        """
        # Clears the terminal
        self.clear_terminal()
        print(self.ascii_art.how_to_play_guide)
        print(
            Fore.LIGHTYELLOW_EX +
            f"""Hello {
                self.name_of_player}! We suggest you to read the how to \
play guide above before you begin.\n""")
        while True:
            # Try statement to avoid quitting game when player attempts
            # keyboard interruption (ctrl + c)
            try:
                player_option = input(
                    """A - Choose game mode\nB - Go back\n\
Type 'a' or 'b' below\n""")
                if player_option.lower() == "a":
                    # Navigates player to game mode screen
                    self.choose_game_mode()
                    break
                elif player_option.lower() == "b":
                    # Navigates player back to welcome screen
                    self.collect_info()
                    break
                else:
                    print(Fore.LIGHTYELLOW_EX + "Please enter a valid option.")
            except KeyboardInterrupt:
                print(Fore.LIGHTYELLOW_EX + """KeyboardInterrupt (ctrl + c) \
is not allowed during input. Please try again.""")

    def choose_game_mode(self):
        """
        Gives the option to choose game mode, once the game mode is chosen and
        depending on which one they choose, we use the game_modes
        function within the RandomWord class to select words
        and also pick one randomly
        """
        # Clears the terminal
        self.clear_terminal()
        print(self.ascii_art.game_modes_display)
        def handle_game_mode(mode, worksheet):
            self.hangman_word = self.game_modes(
                mode)
            self.display_word = "_" * \
                len(self.hangman_word)
            self.selected_worksheet = worksheet
            self.play()
        while True:
            # Try statement to avoid quitting game when player
            # attempts keyboard interruption (ctrl + c)
            try:
                player_mode_option = input(
                    Fore.LIGHTGREEN_EX +
                    """A - Easy mode\n""" +
                    Fore.LIGHTYELLOW_EX +
                    """B - Intermediate mode\n""" +
                    Fore.LIGHTRED_EX +
                    """C - Hard mode\n""" +
                    Fore.LIGHTCYAN_EX +
                    """D - Country mode\n""" +
                    Fore.WHITE +
                    """Type 'a', 'b', 'c' or 'd' below\n""")
                if player_mode_option.lower() == "a":
                    handle_game_mode("easy mode", "easy mode")
                    break
                elif player_mode_option.lower() == "b":
                    handle_game_mode("intermediate mode", "intermediate mode")
                    break
                elif player_mode_option.lower() == "c":
                    handle_game_mode("hard mode", "hard mode")
                    break
                elif player_mode_option.lower() == "d":
                    handle_game_mode("country mode", "country mode")
                    break
                else:
                    print(Fore.LIGHTYELLOW_EX + "Please enter a valid option.")
            except KeyboardInterrupt:
                print(Fore.LIGHTYELLOW_EX + """KeyboardInterrupt (ctrl + c) \
is not allowed during input. Please try again.""")

    def play(self):
        """
        Starts the game and depending on the user input "word",
        "letter", it calls the corresponding functions guess_word()
        or guess_letter(). Also if user selects the hint option
        it calls the api to get the definition of the hangman word.
        """
        # Starts timer
        self.start_time = time.time()
        self.game_hint_message = Fore.LIGHTGREEN_EX + f"""This word is\
 {len(self.hangman_word)} letters in length, good luck!"""
        # While the game is still going on, do the following
        while self.score > 0:
            self.clear_terminal()
            # Try statement to avoid quitting game when player
            # attempts keyboard interruption (ctrl + c)
            try:
                print(self.ascii_art.hangman_stages[self.stages])
                print(f"{self.game_hint_message}\n")
                print(
                    Fore.LIGHTRED_EX +
                    f"""Wrong guesses:\n{
                        self.guessed_letters +
                        self.guessed_words}\n""")
                print(f"""{" ".join(self.display_word)}\n""")
                if self.points >= 25:
                    print(Fore.LIGHTGREEN_EX + f"Points: {self.points}\n")
                else:
                    print(Fore.LIGHTRED_EX + f"Points: {self.points}\n")
                print("---------------------------------------------------")
                if self.score < 3:
                    print(Fore.LIGHTYELLOW_EX + f"You have {self.score}\
 attempt left")
                else:
                    print(Fore.LIGHTGREEN_EX + f"You have {self.score}\
 attempts left")
                if self.hints_remaining != 0 and self.selected_worksheet != "\
country mode":
                    print(Fore.LIGHTCYAN_EX + "Hint token" + Fore.RESET + "\
: type 'hint' to get the words definition")
                elif (
                    self.hints_remaining != 0 and
                    self.selected_worksheet == "country mode"
                ):
                    print(Fore.LIGHTCYAN_EX + "Hint token" + Fore.RESET + "\
: type 'hint' to get country information")
                else:
                    pass
                user_input = input(
                    "Guess a letter or a word: \n\
").lower() if self.score > 2 else input(
                    Fore.LIGHTRED_EX + "Guess a letter or a word\
, Hurry!: \n").lower()
                try:
                    if user_input == "hint" and self.hints_remaining != 0:
                        self.hints_remaining -= 1
                        self.use_hint_token(self.hangman_word,
                                            self.selected_worksheet)
                        user_input = input(
                            "Guess a letter or a word\
: \n").lower() if self.score > 2 else input(
                            Fore.LIGHTRED_EX + "Guess a letter or a word\
, Hurry!: \n").lower()
                        if len(user_input) == 1:
                            self.guess_letter(user_input)
                        else:
                            self.guess_word(user_input)
                        if self.points > 25:
                            self.points -= 25
                        else:
                            pass
                    elif user_input.isalpha():
                        if len(user_input) == 1:
                            self.guess_letter(user_input)
                        else:
                            self.guess_word(user_input)
                    else:
                        self.game_hint_message = Fore.LIGHTRED_EX + \
                            "Your input is neither a letter or a \
word, try again."
                except KeyboardInterrupt:
                    pass
                # If player score is 0, end the game
                if self.score == 0:
                    self.game_end()
                # If the player wins, pass player data to google sheets
                if self.player_won:
                    if self.hints_remaining == 1:
                        hints_used = "No"
                    else:
                        hints_used = "Yes"
                    end_time = time.time()
                    elapsed_time = end_time - self.start_time
                    data_to_add = [self.name_of_player,
                                   self.points,
                                   datetime.now().strftime('%d/%m/%Y'),
                                   self.location_of_player,
                                   f"{round(elapsed_time, 3)} seconds",
                                   self.hangman_word,
                                   hints_used]
                    self.append_to_worksheet(
                        self.selected_worksheet, data_to_add)
                    self.game_end()
            except KeyboardInterrupt:
                continue

    def guess_word(self, user_input):
        """
        Checks if the user word input is correct or not,
        increments or decrements points accordingly
        """
        if user_input in self.guessed_words:
            self.game_hint_message = Fore.LIGHTYELLOW_EX + \
                f"You have guessed the word '{user_input}' already."
        else:
            if user_input == self.hangman_word:
                if len(self.guessed_correct_letters) < round(
                        (len(self.hangman_word) / 2) + 1):
                    self.points += 750
                    self.player_won = True
                else:
                    self.points += 100
                    self.player_won = True
            else:
                self.points = 0
                self.score -= 1
                self.guessed_words.append(user_input)
                self.game_hint_message = Fore.LIGHTRED_EX + \
                    f"Wrong! {user_input} is not the word"
                if self.score != 0:
                    self.stages += 1
                else:
                    pass

    def guess_letter(self, user_input):
        """
        Checks if user letter input is correct or not,
        increments or decrements points accordingly
        """
        if (
            user_input in self.guessed_letters
            or user_input in self.guessed_correct_letters
        ):
            self.game_hint_message = Fore.LIGHTYELLOW_EX + \
                f"You have guessed the letter '{user_input}' already"
        else:
            if user_input in self.hangman_word:
                self.guessed_correct_letters.append(user_input)
                self.update_display_word(user_input)
                self.game_hint_message = Fore.LIGHTGREEN_EX + \
                    f"Correct! the letter '{user_input}' is in the word!"
                self.points += 25
                if "_" not in self.display_word:
                    self.player_won = True
            else:
                if self.points < 10:
                    pass
                else:
                    self.points -= 10
                self.score -= 1
                self.guessed_letters.append(user_input)
                self.game_hint_message = Fore.LIGHTRED_EX + \
                    f"Wrong! the letter {user_input} is not in the word"
                if self.score != 0:
                    self.stages += 1
                else:
                    pass

    def update_display_word(self, user_input):
        """
        Checks if the user letter input is in the self.hangman_word,
        if it is it reveals the letter in the correct place
        """
        updated_display = ""
        # Hide the hangman word with underscores, if the user guesses a letter
        # right then reveal the letters in the correct index
        for winning_word, displayed_word in zip(
                self.hangman_word, self.display_word):
            if winning_word == user_input or displayed_word != "_":
                updated_display += (
                    winning_word
                    if winning_word == user_input
                    else displayed_word
                )
            else:
                updated_display += "_"
        self.display_word = updated_display

    def reset_game(self):
        """
        Resets only the class attributes that need to be reset,
        leaves the user name and location the same
        """
        self.player_won = False
        self.hangman_word = self.game_modes("easy mode")
        self.display_word = "_" * \
            len(self.game_modes("easy mode"))
        self.stages = 0
        self.score = 7
        self.points = 0
        self.guessed_letters = []
        self.guessed_words = []
        self.guessed_correct_letters = []
        self.game_hint_message = ""
        self.hints_remaining = 1

    def leaderboard_mode_options(self):
        """
        Gives player options on navigating to different mode leaderboard's
        """
        def handle_leaderboard_mode_options(worksheet):
            self.selected_worksheet = worksheet
            self.get_leaderboard_data(worksheet)
            self.game_end_options()
        while True:
            # Try statement to avoid quitting game when player attempts
            # keyboard interruption (ctrl + c)
            try:
                user_choice = input(
                    Fore.LIGHTCYAN_EX +
                    "\nA - Easy mode leaderboard\nB - Intermediate mode \
leaderboard\nC - Hard mode leaderboard\nD - Country mode leaderboard\n" +
                    Fore.RESET +
                    "Type 'a', 'b' or 'c' below\n")
                if user_choice.lower() == "a":
                    handle_leaderboard_mode_options("easy mode")
                    break
                elif user_choice.lower() == "b":
                    handle_leaderboard_mode_options("intermediate mode")
                    break
                elif user_choice.lower() == "c":
                    handle_leaderboard_mode_options("hard mode")
                    break
                elif user_choice.lower() == "d":
                    handle_leaderboard_mode_options("country mode")
                    break
                else:
                    print(Fore.LIGHTYELLOW_EX + "Please enter a valid option.")
            except KeyboardInterrupt:
                print(
                    Fore.LIGHTYELLOW_EX +
                    "KeyboardInterrupt (ctrl + c) is not allowed during\
 input. Please try again.")

    def game_end_options(self):
        """
        Gives player options on either play again, leaderboard's or exit game
        """
        while True:
            # Try statement to avoid quitting game when player attempts
            # keyboard interruption (ctrl + c)
            try:

                user_choice = input(
                    "A - Play again\nB - Leaderboard's\nC - \
Exit game\nType 'a', 'b' or 'c' below\n")
                if user_choice.lower() == "a":
                    self.reset_game()
                    self.choose_game_mode()
                    break
                elif user_choice.lower() == "b":
                    self.leaderboard_mode_options()
                    self.reset_game()
                    break
                elif user_choice.lower() == "c":
                    self.clear_terminal()
                    self.ascii_art.thank_user(
                        self.name_of_player,
                        self.times_player_won,
                        self.location_of_player)
                    sys.exit()
                else:
                    print(Fore.LIGHTYELLOW_EX + "Please enter a valid option.")
            except KeyboardInterrupt:
                print(
                    Fore.LIGHTYELLOW_EX +
                    "KeyboardInterrupt (ctrl + c) is not\
 allowed during input. Please try again.")

    def game_end(self):
        """
        Displays win or lose screen depending if the user
        won or not, also asks the user if they
        want to play again, check leaderboard or exit the game
        """
        self.clear_terminal()
        if self.player_won:
            self.times_player_won += 1
            print(self.ascii_art.win_logo_hangman)
            print(Fore.LIGHTGREEN_EX + f"Amazing job! you saved him!\n")
            print(Fore.LIGHTYELLOW_EX + "Leaderboard's updated.\n")
        else:
            print(self.ascii_art.lose_logo_hangman)
            print(Fore.LIGHTRED_EX + "Better \
luck next time, my dude is dead!\n")

        print(f"The word was " + Fore.LIGHTCYAN_EX + f"{self.hangman_word}\n")
        print(
            """Points:""" +
            Fore.LIGHTGREEN_EX +
            f""" {
                self.points}\n""" +
            Fore.RESET)
        self.game_end_options()
