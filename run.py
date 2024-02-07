from words import random_word
from hangman import *
import colorama
from colorama import Fore
colorama.init(autoreset=True)

class HangmanGame:
    def __init__(self):
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
        self.name_of_player = input("What is your name?\n>>> ")
        self.location_of_player = input("Which country are your from?\n>>> ")
        self.how_to_play()
    
    def how_to_play(self):
        print(f"Hello {self.name_of_player}! Welcome to Ultimate Hangman!")
        while True:
            player_option = input("Type (P)lay or (B)ack\n>>> ").lower()
            if player_option == "p":
                self.play()
                break
            elif player_option == "b":
                self.player_info()
                break
            else:
                print("Please enter a valid option.")

    def play(self):
        print(self.hangman_word)
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
            print(Fore.YELLOW + f"You have {self.score} attempt{"" if self.score == 1 else "s"} left\n")
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
                self.game_end()

    def guess_word(self, user_input):
        if user_input in self.guessed_words:
            self.game_hint_message = Fore.RED + f"You have guessed the word {user_input} already."
        elif user_input == self.hangman_word:
            if len(self.guessed_correct_letters) < round(len(self.hangman_word) / 2):
                self.points += 500
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
        self.guessed_correct_letters = ""
        self.game_hint_message = ""
        
    def game_end(self):
        if self.player_won == True:
            print(self.win_logo)
            print(Fore.GREEN + "Amazing job! You have saved him!\n")
        else:
            print(self.lose_logo)
            print(Fore.RED + "Better luck next time, my dude is dead!\n")
        
        print(f"Points: {self.points}\n")
        while True: 
            print("A - Play again\nB - Exit game")
            user_choice = input(">>> ").lower()
            if user_choice == "a":
                self.reset_game()
                self.play()
            elif user_choice == "b":
                print(f"Thanks for playing {self.name_of_player}!")
                print("Hangman awaits your return!")
                break
            else:
                print("Please enter a valid option.")



if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.player_info()