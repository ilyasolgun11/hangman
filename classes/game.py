import os
from dotenv import load_dotenv
import time
from datetime import datetime
import requests
from .player import Player
from .leaderboard import Leaderboard
from .words import RandomWord
from .gameasciiart import AsciiArt
from .clearterminal import ClearTerminal
import colorama
from colorama import Fore
colorama.init(autoreset=True)
load_dotenv(dotenv_path='env.py')
api_key = os.getenv('API_KEY')


class Game(Player, Leaderboard, RandomWord, AsciiArt, ClearTerminal):
    def __init__(self):
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
        Provide instructions on how to play the game.
        """
        self.clear_terminal.clear_terminal()
        print(self.ascii_art.how_to_play_guide)
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

    def choose_game_mode(self):
        self.clear_terminal.clear_terminal()
        print(self.ascii_art.game_modes_display)
        def handle_game_mode(mode, worksheet):
            self.hangman_word = self.random_word_instance.game_modes(
                    mode)
            self.display_word = "_" * \
                    len(self.hangman_word)
            self.selected_worksheet = worksheet
            self.play()
        while True:
            player_mode_option = input(
                Fore.GREEN +
                """A - Easy mode\n""" +
                Fore.YELLOW +
                """B - Intermediate mode\n""" +
                Fore.RED +
                """C - Hard mode\n""" +
                Fore.WHITE +
                """Type 'a', 'b' or 'c' below\n>>> """)
            if player_mode_option.lower() == "a":
                handle_game_mode("easy mode", "easy mode")
                break
            elif player_mode_option.lower() == "b":
                handle_game_mode("intermediate mode", "intermediate mode")
                break
            elif player_mode_option.lower() == "c":
                handle_game_mode("hard mode", "hard mode")
                break
            else:
                print(Fore.YELLOW + "Please enter a valid option.")

    def play(self):
        """
        Starts the game and depending on the user input "word", "letter", it calls
        the corresponding functions guess_word() or guess_letter(). Also if user selects the hint option
        it calls the api to get the definition of the hangman word.
        """
        self.start_time = time.time()
        self.game_hint_message = Fore.GREEN + "Good luck!"
        while self.score > 0:
            self.clear_terminal.clear_terminal()
            print(self.ascii_art.hangman_stages[self.stages])
            print(f"{self.game_hint_message}\n")
            print(self.hangman_word)
            print(
                Fore.RED +
                f"""Wrong guesses:\n{
                    self.guessed_letters +
                    self.guessed_words}\n""")
            print(" ".join(self.display_word))
            if self.points >= 25:
                print(Fore.GREEN + f"Points: {self.points}\n")
            else:
                print(Fore.RED + f"Points: {self.points}\n")
            print("---------------------------------------------------")
            if self.score == 1:
                print(Fore.YELLOW + f"You have {self.score} attempt left")
            else:
                print(Fore.YELLOW + f"You have {self.score} attempts left")
            url = f"""https://dictionary-data-api.p.rapidapi.com/definition/{
                self.hangman_word}"""
            headers = {'X-RapidAPI-Key': api_key}
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
                        print(Fore.YELLOW + "Grabbing definition...")
                        self.hints_remaining -= 1
                        if self.points > 30:
                            pass
                        else:
                            self.points -= 25
                        response = requests.get(url, headers=headers)
                        if response.status_code == 200:
                            data = response.json()
                            meanings = data.get('meaning', [])
                            if meanings:
                                definition = meanings[0]["values"][0]
                                print(
                                    Fore.BLUE +
                                    f"""Definition of word: {
                                        definition.replace(
                                            self.hangman_word,
                                            '(hidden correct word)')}""")
                            else:
                                print("No meanings found.")
                        else:
                            print(f"Error: Sorry, no definitions found...")
                        break
                    elif user_hint_option.lower() == "b":
                        pass
                        break
                    else:
                        print(Fore.YELLOW + "Please enter either 'a' or 'b'")
                if self.score > 2:
                    user_input = input(
                        "Guess a letter or a word: \n>>> ").lower()
                else:
                    user_input = input(
                        Fore.RED + "Guess a letter or a word, Hurry!: \n>>> ").lower()
            else:
                if self.score > 2:
                    user_input = input(
                        "Guess a letter or a word: \n>>> ").lower()
                else:
                    user_input = input(
                        Fore.RED + "Guess a letter or a word, Hurry!: \n>>> ").lower()
            if user_input.isalpha():
                if len(user_input) == 1:
                    self.guess_letter(user_input)
                else:
                    self.guess_word(user_input)
            else:
                self.game_hint_message = Fore.RED + \
                    "Your input is neither a letter or a word, try again."
            if self.score == 0:
                self.game_end()
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

    def guess_word(self, user_input):
        """
        Checks if the user word input is correct or not, increments or decrements points accordingly
        """
        if user_input in self.guessed_words:
            self.game_hint_message = Fore.YELLOW + \
                f"You have guessed the word '{user_input}' already."
        else:
            if user_input == self.hangman_word:
                if len(self.guessed_correct_letters) < round(
                        (len(self.hangman_word) / 2)):
                    self.points += 750
                    self.player_won = True
                else:
                    self.points += 100
                    self.player_won = True
            else:
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
        if user_input in self.guessed_letters or user_input in self.guessed_correct_letters:
            self.game_hint_message = Fore.YELLOW + \
                f"You have guessed the letter '{user_input}' already"
        else:
            if user_input in self.hangman_word:
                if user_input in self.hangman_word:
                    self.guessed_correct_letters.append(user_input)
                    self.update_display_word(user_input)
                    self.game_hint_message = Fore.GREEN + \
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
        while True:
            user_choice = input(
                Fore.CYAN +
                "A - Easy mode leaderboard\nB - Intermediate mode leaderboard\nC - Hard mode leaderboard\nType 'a', 'b' or 'c' below\n>>> " +
                Fore.RESET)
            if user_choice.lower() == "a":
                self.selected_worksheet = "easy mode"
                self.get_leaderboard_data("easy mode")
                self.game_end_options()
                break
            elif user_choice.lower() == "b":
                self.selected_worksheet = "intermediate mode"
                self.get_leaderboard_data("intermediate mode")
                self.game_end_options()
                break
            elif user_choice.lower() == "c":
                self.selected_worksheet = "hard mode"
                self.get_leaderboard_data("hard mode")
                self.game_end_options()
                break
            else:
                print(Fore.YELLOW + "Please enter a valid option.")

    def game_end_options(self):
        while True:
            print("")
            user_choice = input(
                "A - Play again\nB - Leaderboard's\nC - Exit game\nType 'a', 'b' or 'c' below\n>>>")
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
        print(f"Points: {self.points}\n")
        self.game_end_options()
