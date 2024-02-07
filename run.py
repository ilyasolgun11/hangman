from words import random_word
from hangman import *

class HangmanGame:
    def __init__(self):
        self.player_won = False
        self.hangman_word = random_word()
        self.hangman_stage = hangman_stages
        self.stages = 0
        self.game_logo = hangman_logo
        self.score = 7
        self.guessed_letters = []
        self.guessed_correct_letters = []
        self.guessed_word = []
        self.name_of_player = ""
        self.location_of_player = ""

    def player_info(self):
        print(self.game_logo[0])
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
        while self.score > 0:
            user_input = input("Guess a letter or a word: \n>>> ").lower()
            if user_input.isalpha(): 
                if len(user_input) == 1:
                    self.guess_letter(user_input)
                else:
                    self.guess_word(user_input)
            else:
                print("Your input is neither a letter or a word, try again.")

            if self.score == 0 or self.player_won == True:
                print("You have lost!")
                break

    def guess_word(self, user_input):
        if user_input == self.hangman_word:
            print(f"You have won! the word was {self.hangman_word}")
            self.player_won == True
        else:
            self.guessed_word.append(user_input)
            self.score -= 1
            self.stages += 1
            print(f"Wrong! {user_input} is not the word, your score is now {self.score}")
            print(self.hangman_stage[self.stages])
    
    def guess_letter(self, user_input):
        if user_input in self.guessed_letters or user_input in self.guessed_correct_letters:
            print(f"You have guessed {user_input} already")
        elif user_input in self.hangman_word:
            self.guessed_correct_letters.append(user_input)
            print(f"Correct {user_input} is in the word!")
            if set(self.guessed_correct_letters) == set(self.hangman_word):
                print(f"You have won! the word is {self.hangman_word}")
                self.player_won == True
        else:
            self.guessed_letters.append(user_input)
            self.score -= 1
            self.stages += 1
            print(f"Wrong! {user_input} is not in the word your score is now {self.score}")
            print(self.hangman_stage[self.stages])

if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.player_info()