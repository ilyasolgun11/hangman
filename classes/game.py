from player import Player
from leaderboard import Leaderboard
from words import RandomWord
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from hangman import *
import requests
from datetime import datetime
import time
from dotenv import load_dotenv
import sys
import os
load_dotenv(dotenv_path='env.py')
api_key = os.getenv('API_KEY')

class Game(Player, Leaderboard, RandomWord):

    def __init__(self):
        super().__init__()
        self.start_time = None
        self.player_won = False
        self.selected_worksheet = "easy mode"
        self.random_word_instance = RandomWord()
        self.hangman_word = self.random_word_instance.game_modes("easy mode")
        self.display_word = "_" * len(self.random_word_instance.game_modes("easy mode"))
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
        print(self.how_to_play_guide)
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
                self.hangman_word = self.random_word_instance.game_modes("easy mode")
                self.display_word = "_" * len(self.random_word_instance.game_modes("easy mode"))
                self.selected_worksheet = "easy mode"
                self.play()
                break
            elif player_mode_option.lower() == "b":
                self.hangman_word = self.random_word_instance.game_modes("intermediate mode")
                self.display_word = "_" * len(self.random_word_instance.game_modes("intermediate mode"))
                self.selected_worksheet = "intermediate mode"
                self.play()
                break
            elif player_mode_option.lower() == "c":
                self.hangman_word = self.random_word_instance.game_modes("hard mode")
                self.display_word = "_" * len(self.random_word_instance.game_modes("hard mode"))
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
                f"""Wrong guesses:\n{
                    self.guessed_letters +
                    self.guessed_words}\n""")
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
                self.append_to_worksheet(self.selected_worksheet, data_to_add)
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
                updated_display += winning_word if winning_word == user_input else displayed_word
            else:
                updated_display += "_"
        self.display_word = list(updated_display)

    def reset_game(self):
        """
        Resets only the class attributes that need to be reset, leaves the user name and location the same
        """
        self.player_won = False
        self.hangman_word = self.random_word_instance.game_modes("easy mode")
        self.display_word = "_" * len(self.random_word_instance.game_modes("easy mode"))
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

   
if __name__ == "__main__":
    game = Game()
    game.collect_info()
    