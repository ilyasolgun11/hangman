from words import random_word
import sys
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import time
from pprint import pprint
from hangman import *
import colorama
from colorama import Fore
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET_NAME = 'ultimate-hangman-leaderboard'
SHEET = GSPREAD_CLIENT.open(SPREADSHEET_NAME)
worksheet = SHEET.get_worksheet(0)


class HangmanGame:
    """Class representing a Hangman game.

        Attributes:
        - start_time (float): Timestamp representing the start time of the game.
        - player_won (bool): Flag indicating whether the player has won the game.
        - hangman_word (str): The word to be guessed by the player.
        - display_word (str): Current state of the word being guessed, with underscores for unrevealed letters.
        - hangman_stage (list): List of ASCII art representations for different stages of the hangman.
        - stages (int): Current stage of the hangman figure.
        - game_logo (str): ASCII art representing the game logo.
        - lose_logo (str): ASCII art representing the lose scenario logo.
        - win_logo (str): ASCII art representing the win scenario logo.
        - score (int): Remaining attempts for the player to guess the word.
        - points (int): Current score of the player.
        - guessed_letters (list): List of letters guessed by the player.
        - guessed_words (list): List of words guessed by the player.
        - guessed_correct_letters (list): List of correctly guessed letters.
        - name_of_player (str): Name of the player.
        - location_of_player (str): Location of the player.
        - game
    """
    def __init__(self):
        self.start_time = None
        self.player_won = False
        self.hangman_word = random_word()
        self.display_word = "_" * len(self.hangman_word)
        self.hangman_stage = hangman_stages
        self.stages = 0
        self.game_logo = hangman_logo
        self.lose_logo = lose_logo_hangman
        self.win_logo = win_logo_hangman
        self.how_to_play_guide = how_to_play_guide
        self.score = 7
        self.points = 0
        self.guessed_letters = []
        self.guessed_words = []
        self.guessed_correct_letters = []
        self.name_of_player = ""
        self.location_of_player = ""
        self.game_hint_message = ""

    def player_info(self):
        """
        Collect player information before starting the game.
        """
        print(self.game_logo)
        print(Fore.YELLOW + "Welcome stranger!! could you be the one to save this poor guy from a \ngruesome death? i hope so! fill in your name and location to\n see how to play guide.\n")
        self.name_of_player = input(Fore.BLUE + "What is your first name?\n>>> ")
        self.location_of_player = input(Fore.BLUE + "Which country/city are your from?\n>>> ")
        self.how_to_play()
    
    def how_to_play(self):
        """
        Provide instructions on how to play the game.
        """
        print(self.how_to_play_guide)
        print(Fore.YELLOW + f"Hello {self.name_of_player}! We suggest you to read the how to play\nguide above before you begin.\n")
        while True:
            player_option = input("Type 'P' to Play 'B' to go Back\n>>> ")
            if player_option.lower() == "p":
                self.play()
                break
            elif player_option.lower() == "b":
                self.player_info()
                break
            else:
                print(Fore.RED + "Please enter a valid option.")

    def play(self):
        """
        Starts the game and depending on the user input "word", "letter", it calls
        the corresponding functions guess_word() or guess_letter()
        """
        self.start_time = time.time()
        self.game_hint_message = Fore.GREEN + f"You have to guess a word with {len(self.hangman_word)} letters"
        while self.score > 0:
            if self.stages == 0:
                print(self.hangman_stage[self.stages])
            else:
                pass
            print(f"{self.game_hint_message}\n")
            print(Fore.RED + f"Guessed wrong letters:\n{self.guessed_letters}\n")
            print(f"Word: {self.display_word}\n")
            if self.points >= 25:
                print(Fore.GREEN + f"Points: {self.points}\n")
            else: 
                print(Fore.RED + f"Points: {self.points}\n")
            print("---------------------------------------------------")
            if self.score == 1:
                print(Fore.YELLOW + f"You have {self.score} attempt left")
            else:
                print(Fore.YELLOW + f"You have {self.score} attempts left")
            if self.score > 2:
                user_input = input("Guess a letter or a word: \n>>> ").lower()
            else:
                user_input = input(Fore.RED + "Guess a letter or a word, Hurry!: \n>>> ").lower()
            
            if user_input.isalpha(): 
                if len(user_input) == 1:
                    self.guess_letter(user_input)
                else:
                    self.guess_word(user_input)
            else:
                self.game_hint_message = Fore.RED + "Your input is neither a letter or a word, try again."

            if self.score == 0:
                self.game_end()

            if self.player_won == True:
                end_time = time.time()
                elapsed_time = end_time - self.start_time
                data_to_add = [self.name_of_player, self.points, datetime.now().strftime('%d/%m/%Y'), self.location_of_player, f"{elapsed_time:.2f} seconds"]
                worksheet.append_row(data_to_add)
                self.game_end()
                

    def guess_word(self, user_input):
        """
        Checks if the user word input is correct or not, increments or decrements points accordingly
        """
        if user_input in self.guessed_words:
            self.game_hint_message = Fore.RED + f"You have guessed the word {user_input} already."
        elif user_input == self.hangman_word:
            if len(self.guessed_correct_letters) < round(len(self.hangman_word) / 2) + 1:
                self.points += 750
                print(f"You have won! the word was {self.hangman_word}")
                self.player_won = True
            else:
                print(f"You have won! the word was {self.hangman_word}")
                self.player_won = True
        else:
            if self.points < 10:
                pass
            else:
                self.points = 0
            self.score -= 1
            self.guessed_letters.append(user_input)
            self.game_hint_message = Fore.RED + f"Wrong! {user_input} is not the word"
            if self.score != 0:
                self.stages += 1
                print(self.hangman_stage[self.stages])
            else:
                pass
    
    def guess_letter(self, user_input):
        """
        Checks if user letter input is correct or not, increments or decrements points accordingly
        """
        if user_input in self.hangman_word:
            print(self.hangman_stage[self.stages])
            if user_input in self.guessed_letters or user_input in self.guessed_correct_letters:
                self.game_hint_message = Fore.RED + f"You have guessed {user_input} already"
            elif user_input in self.hangman_word:
                self.guessed_correct_letters.append(user_input)
                self.update_display_word(user_input)
                self.game_hint_message = Fore.GREEN + f"Correct! the letter '{user_input}' is in the word!"
                self.points += 25
            if "_" not in self.display_word:
                print(f"You have won! the word is {self.hangman_word}")
                self.player_won = True 
        else:
            if self.points < 10:
                pass
            else:
                self.points -= 10
            self.score -= 1
            self.guessed_letters.append(user_input)
            self.game_hint_message = Fore.RED + f"Wrong! the letter {user_input} is not in the word"
            if self.score != 0:
                self.stages += 1
                print(self.hangman_stage[self.stages])
            else:
                pass

    def update_display_word(self, user_input):
        """
        Checks if the user letter input is in the self.hangman_word, if it is it reveals
        the letter in the correct place
        """
        updated_display = ""
        for winning_word, displayed_word in zip(self.hangman_word, self.display_word):
            if winning_word == user_input or displayed_word != "_":
                updated_display += winning_word
            else:
                updated_display += "_"
        self.display_word = updated_display  

    def reset_game(self):
        """
        Resets only the class attributes that need to be reset, leaves the user name and location the same
        """
        self.player_won = False
        self.hangman_word = random_word()
        self.display_word = "_" * len(self.hangman_word)
        self.stages = 0
        self.score = 7
        self.points = 0
        self.guessed_letters = []
        self.guessed_words = []
        self.guessed_correct_letters = []
        self.game_hint_message = ""
        
    def game_end(self):
        """
        Displays win or lose screen depending if the user won or not, also asks the user if they
        want to play again, check leaderboard or exit the game
        """
        if self.player_won == True:
            print(self.win_logo)
            print(Fore.GREEN + f"Amazing job! the word was indeed {self.hangman_word}!\n")
            print(Fore.YELLOW + "Leaderboard's updated.\n")
        else:
            print(self.lose_logo)
            print(Fore.RED + "Better luck next time, my dude is dead!\n")
        
        print(f"Points: {self.points}\n")
        while True: 
            print("A - Play again\nB - Exit game\nC - Leaderboard")
            user_choice = input(">>> ")
            if user_choice.lower() == "a":
                self.reset_game()
                self.play()
                break
            elif user_choice.lower() == "b":
                print(f"Thanks for playing {self.name_of_player}!")
                print("Hangman awaits your return!")
                sys.exit()
            elif user_choice.lower() == "c":
                self.get_leaderboard_data()
                self.reset_game()
                break
            else:
                print("Please enter a valid option.")

    def get_leaderboard_data(self):
        """
        Gets leaderboard data from google sheets and displays the top 20 highest scores, also gives user the option
        to play again or exit the game
        """
        leaderboard_data = worksheet.get_all_records()
        sorted_leaderboard = sorted(leaderboard_data, key=lambda x: x['Points'], reverse=True)
        print(Fore.YELLOW + "------------------------------------------")
        print(Fore.YELLOW + "T O P   2 0   L E A D E R B O A R D")
        print(Fore.YELLOW + "------------------------------------------\n")
        print(Fore.BLUE + "POSITION     NAME         POINTS       LOCATION           DATE         TIME TO WIN")
        
        for position, player_data in enumerate(sorted_leaderboard[:20], start=1):
            
            position_str = str(position).ljust(13)
            name_str = player_data['Name'].ljust(13)
            points_str = str(player_data['Points']).ljust(13)
            location_str = player_data['Country/City'].ljust(19)
            date_str = player_data['Date'].ljust(13)
            time_to_win_str = player_data['Time to win'].ljust(16)
            
            print(Fore.CYAN + f"{position_str}{name_str}{points_str}{location_str}{date_str}{time_to_win_str}")

        while True: 
            print("")
            print(Fore.BLUE + "A - Play again\nB - Exit game\n")
            user_choice = input(">>> ")
            if user_choice.lower() == "a":
                self.reset_game()
                self.play()
                break
            elif user_choice.lower() == "b":
                print(f"Thanks for playing {self.name_of_player}!")
                print("Hangman awaits your return!")
                sys.exit()
            else:
                print(Fore.RED + "Please enter a valid option.")

if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.player_info()