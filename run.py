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
        self.score = 7
        self.points = 0
        self.guessed_letters = []
        self.guessed_words = []
        self.guessed_correct_letters = []
        self.name_of_player = ""
        self.location_of_player = ""
        self.game_hint_message = ""

    def player_info(self):
        print(self.game_logo)
        print(Fore.YELLOW + "Welcome stranger!! could you be the one to save this poor guy from a \ngruesome death? i hope so! fill in your name and location to begin.\n")
        self.name_of_player = input(Fore.BLUE + "What is your name?\n>>> ")
        self.location_of_player = input(Fore.BLUE + "Which country/city are your from?\n>>> ")
        self.how_to_play()
    
    def how_to_play(self):
        print(f"Hello {self.name_of_player}! We suggest you to read the rules before you begin.\n")
        while True:
            player_option = input("Type 'P' to Play, 'L' for Leaderboard or 'B' to go Back\n>>> ").lower()
            if player_option == "p":
                self.play()
                break
            elif player_option == "l":
                self.get_leaderboard_data
                break
            elif player_option == "b":
                self.player_info()
                break
            else:
                print(Fore.RED + "Please enter a valid option.")

    def play(self):
        print(self.hangman_word)
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
        if user_input in self.guessed_words:
            self.game_hint_message = Fore.RED + f"You have guessed the word {user_input} already."
        elif user_input == self.hangman_word:
            if len(self.guessed_correct_letters) < round(len(self.hangman_word) / 2):
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
                self.points -= 10
            self.score -= 1
            self.guessed_letters.append(user_input)
            self.game_hint_message = Fore.RED + f"Wrong! {user_input} is not the word"
            if self.score != 0:
                self.stages += 1
                print(self.hangman_stage[self.stages])
            else:
                pass
    
    def guess_letter(self, user_input):
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
        updated_display = ""
        for winning_word, displayed_word in zip(self.hangman_word, self.display_word):
            if winning_word == user_input or displayed_word != "_":
                updated_display += winning_word
            else:
                updated_display += "_"
        self.display_word = updated_display  

    def reset_game(self):
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
        if self.player_won == True:
            print(self.win_logo)
            print(Fore.GREEN + f"Amazing job! the word was indeed {self.hangman_word}!\n")
        else:
            print(self.lose_logo)
            print(Fore.RED + "Better luck next time, my dude is dead!\n")
        
        print(f"Points: {self.points}\n")
        print(Fore.YELLOW + "Leaderboard's updated.\n")
        while True: 
            print("A - Play again\nB - Exit game\nC - Leaderboard")
            user_choice = input(">>> ").lower()
            if user_choice == "a":
                self.reset_game()
                self.play()
                break
            elif user_choice == "b":
                print(f"Thanks for playing {self.name_of_player}!")
                print("Hangman awaits your return!")
                sys.exit()
            elif user_choice == "c":
                self.reset_game()
                self.get_leaderboard_data()
                break
            else:
                print("Please enter a valid option.")

    def get_leaderboard_data(self):
        leaderboard_data = worksheet.get_all_records()
        sorted_leaderboard = sorted(leaderboard_data, key=lambda x: x['Points'], reverse=True)
        print(Fore.YELLOW + "------------------------------------------")
        print(Fore.YELLOW + "T O P   3 0   L E A D E R B O A R D")
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
            print(Fore.BLUE + "A - Play again\nB - Exit game\nC - Leaderboard")
            user_choice = input(">>> ").lower()
            if user_choice == "a":
                self.reset_game()
                self.play()
                break
            elif user_choice == "b":
                print(f"Thanks for playing {self.name_of_player}!")
                print("Hangman awaits your return!")
                sys.exit()
            elif user_choice == "c":
                self.get_leaderboard_data()
                break
            else:
                print(Fore.RED + "Please enter a valid option.")

if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.player_info()