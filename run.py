from words import random_word
import sys
import gspread
import requests
from google.oauth2.service_account import Credentials
from datetime import datetime
import time
import json
from hangman import *
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='env.py')
api_key = os.getenv('API_KEY')


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

class ClearConsole:
    def clear_console(self):
        return os.system("cls" if os.name in ("nt", "dos") else "clear")

class PlayerInfo(ClearConsole):
    """Class collecting using name and location of user.

        Attributes:
        - name_of_player (str) grabs the name of player and stores it
        - location_of_player (str) grabs the location of player and stores it
    """

    def __init__(self):
        """
        Initializes player info attributes
        """
        super().__init__()
        self.name_of_player = ""
        self.location_of_player = ""

    def collect_info(self):
        """
        Collect player information before starting the game.
        """
        self.clear_console()
        print(self.game_logo)
        print(Fore.YELLOW + "Welcome stranger! could you be the one to save this poor guy from a \ngruesome death? i hope so! fill in your name and location to\nsee the how to play guide.\n")
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


class HangmanGame(PlayerInfo, ClearConsole):
    """Class representing the Hangman game.

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
        - game_hint_message (str): holds value thats shown in the game screen.
    """

    def __init__(self):
        """
        Initializes hangman game attributes
        """
        super().__init__()
        self.start_time = None
        self.player_won = False
        self.selected_worksheet = "easy mode"
        self.hangman_word = random_word("easy mode")
        self.display_word = "_" * len(random_word("easy mode"))
        self.hangman_stage = hangman_stages
        self.stages = 0
        self.game_logo = hangman_logo
        self.lose_logo = lose_logo_hangman
        self.win_logo = win_logo_hangman
        self.how_to_play_guide = how_to_play_guide
        self.game_modes_display = game_modes_display
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
        self.clear_console()
        print(self.how_to_play_guide)
        print(
            Fore.YELLOW +
            f"Hello {
                self.name_of_player}! We suggest you to read the how to play\nguide above before you begin.\n")
        # Gives the user the option of starting the game and also going back, it will repeat that question until the user
        # provides the correct input, this is done using a while loop
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
        self.clear_console()
        print(self.game_modes_display)
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
                self.hangman_word = random_word("easy mode")
                self.display_word = "_" * len(random_word("easy mode"))
                self.selected_worksheet = "easy mode"
                self.play()
                break
            elif player_mode_option.lower() == "b":
                self.hangman_word = random_word("intermediate mode")
                self.display_word = "_" * len(random_word("intermediate mode"))
                self.selected_worksheet = "intermediate mode"
                self.play()
                break
            elif player_mode_option.lower() == "c":
                self.hangman_word = random_word("hard mode")
                self.display_word = "_" * len(random_word("hard mode"))
                self.selected_worksheet = "hard mode"
                self.play()
                break
            else:
                print(Fore.YELLOW + "Please enter a valid option.")

    def play(self):
        """
        Starts the game and depending on the user input "word", "letter", it calls
        the corresponding functions guess_word() or guess_letter(). Also if user selects the hint option
        it calls the api to get the definition of the hangman word.
        """
        # Timer starts and it runs till the game_end function is called
        self.start_time = time.time()
        self.game_hint_message = Fore.GREEN + "Good luck!"
        # URL changes based on the random hangman word
        # While user score is more than 0 (the game is still going on) display
        # the game screen
        while self.score > 0:
            print(self.hangman_stage[self.stages])
            print(f"{self.game_hint_message}\n")
            print(
                Fore.RED +
                f"Wrong guesses:\n{
                    self.guessed_letters +
                    self.guessed_words}\n")
            print(f"Word: {' '.join(self.display_word)}\n")
            if self.points >= 25:
                print(Fore.GREEN + f"Points: {self.points}\n")
            else:
                print(Fore.RED + f"Points: {self.points}\n")
            print("---------------------------------------------------")
            if self.score == 1:
                print(Fore.YELLOW + f"You have {self.score} attempt left")
            else:
                print(Fore.YELLOW + f"You have {self.score} attempts left")
            # If the user has not spent their hint token (the value of self.hints_remaining is till 1) and user score is less than 4, as the
            # user if they want to user their hint token, if they do send a call to the dictionary API, and if the status code is 200 then display
            # the returned data, if not handle the error.
            url = f"https://dictionary-data-api.p.rapidapi.com/definition/{
            self.hangman_word}"
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
                                    f"Definition of word: {
                                        definition.replace(
                                            self.hangman_word,
                                            '(hidden correct word)')}")
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
                # Change input message from "attempts" to "attempt" based on
                # the number of attempts remaining
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
            # Check if the user input is a letter or a word using the isalpha function and depending on which one they choose call the
            # respective functions guess_word() or guess_letter(). If the user
            # input is not a letter or word then handle it
            if user_input.isalpha():
                if len(user_input) == 1:
                    self.guess_letter(user_input)
                else:
                    self.guess_word(user_input)
            else:
                self.game_hint_message = Fore.RED + \
                    "Your input is neither a letter or a word, try again."
            # If the user has no attempts left, call the game_end function
            if self.score == 0:
                self.game_end()
            # If the player_won attribute is True end the timer started when the play function was initially called. Also send of the gathered user data
            # to google sheets
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
                SHEET.worksheet(
                    self.selected_worksheet).append_row(data_to_add)
                self.game_end()

    def guess_word(self, user_input):
        """
        Checks if the user word input is correct or not, increments or decrements points accordingly
        """
        # If the user has guessed a word, and the word was already guessed,
        # display message
        if user_input in self.guessed_words:
            self.game_hint_message = Fore.YELLOW + \
                f"You have guessed the word '{user_input}' already."
        else:
            # If the user_input is equal to the hangman_word, check if the user guessed the word before or after half the letters were found
            # already, if they guessed before they revealed the first half of
            # letters then reward them with 750 points, otherwise reward them
            # with 100
            if user_input == self.hangman_word:
                if len(self.guessed_correct_letters) < round(
                        len(self.hangman_word) / 2):
                    self.points += 750
                    self.player_won = True
                else:
                    self.points += 100
                    self.player_won = True
            # If the word the user guessed is not equal to the hangman word
            # then take away all their points, and decrement the attempts by 1
            else:
                self.points = 0
                self.score -= 1
                self.guessed_words.append(user_input)
                self.game_hint_message = Fore.RED + \
                    f"Wrong! {user_input} is not the word"
                # If the attempts left is not 0 then increment the stages
                # attribute to get the next ASCII art from the hangman_stages
                # list
                if self.score != 0:
                    self.stages += 1
                else:
                    pass

    def guess_letter(self, user_input):
        """
        Checks if user letter input is correct or not, increments or decrements points accordingly
        """
        # If the user input letter was already guessed, ask the user to
        # re-enter a letter
        if user_input in self.guessed_letters or user_input in self.guessed_correct_letters:
            self.game_hint_message = Fore.YELLOW + \
                f"You have guessed the letter '{user_input}' already"
        else:
            # If the letter the user guessed is in the hangman word do the
            # following..
            if user_input in self.hangman_word:
                # If the user input letter is in the hangman word then add 25
                # points and congratulate the user
                if user_input in self.hangman_word:
                    self.guessed_correct_letters.append(user_input)
                    self.update_display_word(user_input)
                    self.game_hint_message = Fore.GREEN + \
                        f"Correct! the letter '{user_input}' is in the word!"
                    self.points += 25
                # If there is no more underscores left in the display_word
                # string, then let the user know they won
                if "_" not in self.display_word:
                    print(f"You have won! the word is {self.hangman_word}")
                    self.player_won = True
            else:
                # If the user input letter is not in the hangman word then check if the points is under 10, if it is not then
                # decrement by 10 and decrement the attempts left.
                if self.points < 10:
                    pass
                else:
                    self.points -= 10
                self.score -= 1
                self.guessed_letters.append(user_input)
                self.game_hint_message = Fore.RED + \
                    f"Wrong! the letter {user_input} is not in the word"
                # If the attempts left is not 0 then increment the stages
                # attribute to get the next ASCII art from the hangman_stages
                # list
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
        self.hangman_word = random_word(self.selected_worksheet)
        self.display_word = "_" * len(self.hangman_word)
        self.stages = 0
        self.score = 7
        self.points = 0
        self.guessed_letters = []
        self.guessed_words = []
        self.guessed_correct_letters = []
        self.game_hint_message = ""
        self.hints_remaining = 1

    def game_end(self):
        """
        Displays win or lose screen depending if the user won or not, also asks the user if they
        want to play again, check leaderboard or exit the game
        """
        if self.player_won:
            print(self.win_logo)
            print(Fore.GREEN + f"Amazing job! you saved him!\n")
            print(Fore.YELLOW + "Leaderboard's updated.\n")
        else:
            print(self.lose_logo)
            print(Fore.RED + "Better luck next time, my dude is dead!\n")

        print(f"The word was " + Fore.CYAN + f"{self.hangman_word}\n")
        print(f"Points: {self.points}\n")
        # While the user does not select an invalid option (anything other than
        # a, b or c) then keep asking them for a valid input
        while True:
            user_choice = input(
                "A - Play again\nB - Exit game\nC - Leaderboard\nType 'a', 'b' or 'c' below\n>>>")
            if user_choice.lower() == "a":
                self.reset_game()
                self.choose_game_mode()
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
                print(Fore.YELLOW + "Please enter a valid option.")

    def get_leaderboard_data(self):
        """
        Gets leaderboard data from google sheets and displays the top 15 highest scores, also gives user the option
        to play again, choose a different modes leaderboard or exit the game
        """
        leaderboard_sheet = SHEET.worksheet(self.selected_worksheet)
        leaderboard_data = leaderboard_sheet.get_all_records()
        sorted_leaderboard = sorted(
            leaderboard_data,
            key=lambda x: x['Points'],
            reverse=True)
        if self.selected_worksheet == "easy mode":
            leaderboard_header_mode = "E A S Y   M O D E"
        elif self.selected_worksheet == "intermediate mode":
            leaderboard_header_mode = "I N T E R M E D I A T E    M O D E"
        elif self.selected_worksheet == "hard mode":
            leaderboard_header_mode = "H A R D    M O D E"
        print(
            Fore.YELLOW +
            "--------------------------------------------------------------------------------")
        print(
            Fore.YELLOW +
            f"  T O P   1 5   L E A D E R B O A R D  |  {leaderboard_header_mode}")
        print(
            Fore.YELLOW +
            "--------------------------------------------------------------------------------\n")
        print(
            Fore.BLUE +
            "POSITION  NAME      POINTS LOCATION    DATE        TIME TO WIN    WORD        HINT USED?")
        # Using the data from worksheet.get_all_records(), the data is displayed with designated column widths to separate
        # columns evenly without overflow
        for position, player_data in enumerate(
                sorted_leaderboard[:15], start=1):
            position_str = str(position).ljust(10)
            name_str = player_data['Name'].ljust(10).capitalize()
            points_str = str(player_data['Points']).ljust(7)
            location_str = player_data['Country/City'].ljust(12).capitalize()
            date_str = player_data['Date'].ljust(12)
            time_to_win_str = player_data['Time to win'].ljust(15)
            winning_word = player_data['Winning word'].ljust(12).capitalize()
            hint_used = player_data['Hint used?'].ljust(12).capitalize()
            print(Fore.GREEN + f"{position_str}{name_str}{points_str}{location_str}{
                  date_str}{time_to_win_str}{winning_word}{hint_used}")

        # While the user does not select an invalid option (anything other than
        # a or b) then keep asking them for a valid input
        while True:
            print("")
            user_choice = input(
                "A - Play again\nB - See other mode leaderboard's\nC - Exit game\nType 'a', 'b' or 'c' below\n>>> ")
            if user_choice.lower() == "a":
                self.reset_game()
                self.choose_game_mode()
                break
            elif user_choice.lower() == "b":
                self.leaderboard_mode_choice()
                break
            elif user_choice.lower() == "c":
                print(f"Thanks for playing {self.name_of_player}!")
                print("Hangman awaits your return!")
                sys.exit()
            else:
                print(Fore.YELLOW + "Please enter a valid option.")

    def leaderboard_mode_choice(self):
        while True:
            print("")
            user_choice = input(
                "A - Easy mode leaderboard\nB - Intermediate mode leaderboard\nC - Hard mode leaderboard\nType 'a', 'b' or 'c' below\n>>> ")
            if user_choice.lower() == "a":
                self.selected_worksheet = "easy mode"
                self.get_leaderboard_data()
                break
            elif user_choice.lower() == "b":
                self.selected_worksheet = "intermediate mode"
                self.get_leaderboard_data()
                break
            elif user_choice.lower() == "c":
                self.selected_worksheet = "hard mode"
                self.get_leaderboard_data()
                break
            else:
                print(Fore.YELLOW + "Please enter a valid option.")


if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.collect_info()
