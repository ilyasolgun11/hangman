import time
from datetime import datetime
from .player import Player
from .leaderboard import Leaderboard
from .words import RandomWord
from .gameasciiart import AsciiArt
from .clearterminal import ClearTerminal
from .definition import GrabDefinition
import colorama
from colorama import Fore
colorama.init(autoreset=True)



class Game(Player, Leaderboard, RandomWord, AsciiArt, ClearTerminal, GrabDefinition):
    """
    The Game class represents the main Hangman game.

    Attributes:
    - start_time (float): The start time of the game.
    - player_won (bool): Indicates whether the player won the game.
    - selected_worksheet (str): The selected game mode worksheet.
    - random_word_instance (RandomWord): An instance of the RandomWord class 
      for generating hangman words.
    - ascii_art (AsciiArt): An instance of the AsciiArt class for displaying ASCII art.
    - clear_terminal (ClearTerminal): An instance of the ClearTerminal 
      class for clearing the terminal.
    - hangman_word (str): The current hangman word to be guessed.
    - display_word (str): The partially revealed word based on user guesses.
    - stages (int): The number of stages of the hangman (visual representation).
    - hints_remaining (int): The number of hint tokens remaining.
    - score (int): The player's score.
    - points (int): The points earned during the game.
    - guessed_letters (list): List of guessed letters.
    - guessed_words (list): List of guessed words.
    - guessed_correct_letters (list): List of correctly guessed letters.
    - game_hint_message (str): Message related to hints during the game.

    Methods:
    - how_to_play(): Provides instructions on how to play the game.
    - choose_game_mode(): Allows the player to choose the game mode.
    - play(): Starts the game and manages user input.
    - guess_word(user_input): Handles the user's attempt to guess a word.
    - guess_letter(user_input): Handles the user's attempt to guess a letter.
    - update_display_word(user_input): Updates the displayed word based on correct letter guesses.
    - reset_game(): Resets relevant game attributes for a new round.
    - leaderboard_mode_options(): Allows the player to view leaderboard's for different game modes.
    - game_end_options(): Displays options after the game ends (play again, 
      view leaderboard, or exit).
    - game_end(): Displays the win/lose screen and handles post-game options.
    """
    def __init__(self):
        """
        Initializes a new instance of the Hangman game.
        """
        super().__init__()
        self.start_time = None
        self.player_won = False
        self.selected_worksheet = "easy mode"
        self.random_word_instance = RandomWord()
        self.ascii_art = AsciiArt()
        self.clear_terminal = ClearTerminal()
        self.hangman_word = self.random_word_instance.game_modes("hard mode")
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

    def how_to_play(self):
        """
        Provide instructions on how to play the game and informs player of the points system.
        """
        # Clears the terminal 
        self.clear_terminal.clear_terminal()
        print(self.ascii_art.how_to_play_guide)
        print(
            Fore.YELLOW +
            f"""Hello {
                self.name_of_player}! We suggest you to read the how to play\nguide above before you begin.\n""")
        while True:
            # Try statement to avoid quitting game when player attempts keyboard interruption (ctrl + c) 
            try:
                player_option = input(
                    "A - Choose game mode\nB - Go back\nType 'a' or 'b' below\n>>> ")
                if player_option.lower() == "a":
                    # Navigates player to game mode screen
                    self.choose_game_mode()
                    break
                elif player_option.lower() == "b":
                    # Navigates player back to welcome screen
                    self.collect_info()
                    break
                else:
                    print(Fore.YELLOW + "Please enter a valid option.")
            except KeyboardInterrupt:
                print(Fore.YELLOW + "KeyboardInterrupt (ctrl + c) is not allowed during input. Please try again.")

    def choose_game_mode(self):
        """
        Gives the option to choose game mode, once the game mode is chosen and 
        depending on which one they choose, we use the game_modes 
        function within the RandomWord class to select words 
        and also pick one randomly
        """
        # Clears the terminal 
        self.clear_terminal.clear_terminal()
        print(self.ascii_art.game_modes_display)
        # Sets self.hangman_word to a randomized word gathered from the RandomWord class 
        # Also sets the display word, but multiplying "_" with the letters in self.hangman_word 
        def handle_game_mode(mode, worksheet):
            self.hangman_word = self.random_word_instance.game_modes(
                    mode)
            self.display_word = "_" * \
                    len(self.hangman_word)
            self.selected_worksheet = worksheet
            self.play()
        while True:
            # Try statement to avoid quitting game when player attempts keyboard interruption (ctrl + c) 
            try:
                player_mode_option = input(
                    Fore.GREEN +
                    """A - Easy mode\n""" +
                    Fore.YELLOW +
                    """B - Intermediate mode\n""" +
                    Fore.RED +
                    """C - Hard mode\n""" +
                    Fore.CYAN + 
                    """D - Country mode\n""" +
                    Fore.WHITE +
                    """Type 'a', 'b', 'c' or 'd' below\n>>> """)
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
                    print(Fore.YELLOW + "Please enter a valid option.")
            except KeyboardInterrupt:
                print(Fore.YELLOW + "KeyboardInterrupt (ctrl + c) is not allowed during input. Please try again.")

    def play(self):
        """
        Starts the game and depending on the user input "word", "letter", it calls
        the corresponding functions guess_word() or guess_letter(). Also if user selects the hint option
        it calls the api to get the definition of the hangman word.
        """
        # Starts timer, this timer ends when player either wins or loses, this is later used 
        # to display the time it took for the player to win in the Leaderboard section 
        self.start_time = time.time()
        # This message changes depending on what the user does during the game 
        self.game_hint_message = Fore.GREEN + "Good luck!"
        # While the game is still going on, do the following
        while self.score > 0:
            # Try statement to avoid quitting game when player attempts keyboard interruption (ctrl + c) 
            try:
                # Clear the terminal
                self.clear_terminal.clear_terminal()
                # Display which stage the player is on
                print(self.ascii_art.hangman_stages[self.stages])
                # Display hint message to inform player
                print(f"{self.game_hint_message}\n")
                # Displays the wrongly guessed letters and words
                print(
                    Fore.RED +
                    f"""Wrong guesses:\n{
                        self.guessed_letters +
                        self.guessed_words}\n""")
                # Displays the self.hangman_word in underscores, till user reveals them by
                # guessing correctly 
                print(f"""{" ".join(self.display_word)}\n""")
                # Depending on how many points the user has, display them in either red or green
                if self.points >= 25:
                    print(Fore.GREEN + f"Points: {self.points}\n")
                else:
                    print(Fore.RED + f"Points: {self.points}\n")
                # Use line for separation
                print("---------------------------------------------------")
                # Display the amount of attempts the user has, and if they have less than 3, display
                # it in yellow 
                if self.score < 3:
                    print(Fore.YELLOW + f"You have {self.score} attempt left")
                else:
                    print(Fore.GREEN + f"You have {self.score} attempts left")
                # If the players score is less than 4 and they have not used the hint token
                # then do the following  
                if self.hints_remaining == 1 and self.score < 4:
                    while True:
                        print(Fore.CYAN + "\nDo you want to use your hint token?")
                        user_hint_option = input(
                            Fore.GREEN +
                            """A - Yes i want to use my hint token\n""" +
                            Fore.RED +
                            """B - No i got this\n""" +
                            Fore.WHITE +
                            """Type 'a' or 'b' below\n>>> """)
                        if user_hint_option.lower() == "a":
                            # If the points of the player is
                            # more than 30, deduct 25 points 
                            self.hints_remaining -= 1
                            if self.points > 30:
                                pass
                            else:
                                self.points -= 25
                            if self.selected_worksheet != "country mode":
                                self.grab_word_definition(self.hangman_word)
                            else:
                                self.grab_country_data(self.hangman_word)
                            break
                        elif user_hint_option.lower() == "b":
                            pass
                            break
                        else:
                            # If the player is neither a or b, display that to player
                            print(Fore.YELLOW + "Please enter either 'a' or 'b'")
                    # Display different input message depending on the player score in the case of
                    # player not having used their hint token yet
                    user_input = input(
                        "Guess a letter or a word: \n>>> ").lower() if self.score > 2 else input(
                        Fore.RED + "Guess a letter or a word, Hurry!: \n>>> ").lower()
                else:
                    # Display different input message depending on the player score in the case of
                    # player having used their hint token already
                    user_input = input(
                        "Guess a letter or a word: \n>>> ").lower() if self.score > 2 else input(
                        Fore.RED + "Guess a letter or a word, Hurry!: \n>>> ").lower()
                # If the players input is a letter, pass that input to the guess_letter() otherwise
                # pass to guess_word()
                if user_input.isalpha():
                    if len(user_input) == 1:
                        self.guess_letter(user_input)
                    else:
                        self.guess_word(user_input)
                else:
                    # If player input is neither a letter or a word, display message
                    self.game_hint_message = Fore.RED + \
                        "Your input is neither a letter or a word, try again."
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
                                f"{elapsed_time:.2f} seconds",
                                self.hangman_word,
                                hints_used]
                    self.append_to_worksheet(self.selected_worksheet, data_to_add)
                    self.game_end()
            except KeyboardInterrupt:
                continue

    def guess_word(self, user_input):
        """
        Checks if the user word input is correct or not, increments or decrements points accordingly
        """
        # If player input is already guessed, display message
        if user_input in self.guessed_words:
            self.game_hint_message = Fore.YELLOW + \
                f"You have guessed the word '{user_input}' already."
        else:
            # If player input is correct ddo the following
            if user_input == self.hangman_word:
                # If the player guessed correctly before revealing the
                # first half of the word, award 750 points, otherwise 100 points
                if len(self.guessed_correct_letters) < round(
                        (len(self.hangman_word) / 2)):
                    self.points += 750
                    self.player_won = True
                else:
                    self.points += 100
                    self.player_won = True
            else:
                # If player guessed wrong, do the following
                self.points = 0
                self.score -= 1
                self.guessed_words.append(user_input)
                self.game_hint_message = Fore.RED + \
                    f"Wrong! {user_input} is not the word"
                if self.score != 0:
                    self.stages += 1
                else:
                    pass

    def guess_letter(self, user_input):
        """
        Checks if user letter input is correct or not, increments or decrements points accordingly
        """
        # If player already guessed a letter, display message
        if user_input in self.guessed_letters or user_input in self.guessed_correct_letters:
            self.game_hint_message = Fore.YELLOW + \
                f"You have guessed the letter '{user_input}' already"
        else:
            # If player guessed a letter correctly do the following
            if user_input in self.hangman_word:
                self.guessed_correct_letters.append(user_input)
                self.update_display_word(user_input)
                self.game_hint_message = Fore.GREEN + \
                    f"Correct! the letter '{user_input}' is in the word!"
                self.points += 25
                # If there are no more underscores in display_word, turn
                # player_won boolean to true
                if "_" not in self.display_word:
                    self.player_won = True
            else:
                # If player guessed incorrectly fo the following
                if self.points < 10:
                    pass
                else:
                    self.points -= 10
                self.score -= 1
                self.guessed_letters.append(user_input)
                self.game_hint_message = Fore.RED + \
                    f"Wrong! the letter {user_input} is not in the word"
                if self.score != 0:
                    self.stages += 1
                else:
                    pass

    def update_display_word(self, user_input):
        """
        Checks if the user letter input is in the self.hangman_word, if it is it reveals
        the letter in the correct place
        """
        updated_display = ""
        # Hide the hangman word with underscores, if the user guesses a letter
        # right then reveal the letters in the correct index
        for winning_word, displayed_word in zip(
                self.hangman_word, self.display_word):
            if winning_word == user_input or displayed_word != "_":
                updated_display += winning_word if winning_word == user_input else displayed_word
            else:
                updated_display += "_"
        self.display_word = updated_display

    def reset_game(self):
        """
        Resets only the class attributes that need to be reset, leaves the user name and location the same
        """
        self.player_won = False
        self.hangman_word = self.random_word_instance.game_modes("easy mode")
        self.display_word = "_" * \
            len(self.random_word_instance.game_modes("easy mode"))
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
            # Try statement to avoid quitting game when player attempts keyboard interruption (ctrl + c) 
            try:
                user_choice = input(
                    Fore.CYAN +
                    "\nA - Easy mode leaderboard\nB - Intermediate mode leaderboard\nC - Hard mode leaderboard\nD - Country mode leaderboard\n" + Fore.RESET + "Type 'a', 'b' or 'c' below\n>>> ")
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
                    print(Fore.YELLOW + "Please enter a valid option.")
            except KeyboardInterrupt:
                print(Fore.YELLOW + "KeyboardInterrupt (ctrl + c) is not allowed during input. Please try again.")

    def game_end_options(self):
        """
        Gives player options on either play again, leaderboard's or exit game
        """
        while True:
            # Try statement to avoid quitting game when player attempts keyboard interruption (ctrl + c) 
            try:
                
                user_choice = input(
                    "\nA - Play again\nB - Leaderboard's\nC - Exit game\nType 'a', 'b' or 'c' below\n>>>")
                if user_choice.lower() == "a":
                    self.reset_game()
                    self.choose_game_mode()
                    break
                elif user_choice.lower() == "b":
                    self.leaderboard_mode_options()
                    self.reset_game()
                    break
                elif user_choice.lower() == "c":
                    self.clear_terminal.clear_terminal()
                    print(f"Thank you so much for playing {self.name_of_player}!")
                    self.collect_info()
                else:
                    print(Fore.YELLOW + "Please enter a valid option.")
            except KeyboardInterrupt:
                print(Fore.YELLOW + "KeyboardInterrupt (ctrl + c) is not allowed during input. Please try again.")

    def game_end(self):
        """
        Displays win or lose screen depending if the user won or not, also asks the user if they
        want to play again, check leaderboard or exit the game
        """
        self.clear_terminal.clear_terminal()
        if self.player_won:
            print(self.ascii_art.win_logo_hangman)
            print(Fore.GREEN + f"Amazing job! you saved him!\n")
            print(Fore.YELLOW + "Leaderboard's updated.\n")
        else:
            print(self.ascii_art.lose_logo_hangman)
            print(Fore.RED + "Better luck next time, my dude is dead!\n")

        print(f"The word was " + Fore.CYAN + f"{self.hangman_word}\n")
        print("""Points:""" + Fore.GREEN + f""" {self.points}\n""" + Fore.RESET)
        self.game_end_options()
