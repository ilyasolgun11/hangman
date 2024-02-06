from words import random_word
from hangman import *

class HangmanGame:
    def __init__(self):
        self.player_won = False
        self.hangman_word = random_word()
        self.hangman_stage = hangman_stages
        self.stages = 0
        self.score = 7
        self.guessed_letters = []
        self.guessed_correct_letters = []
        self.guessed_word = []

    def play(self):
        print(self.hangman_word)

        while self.score > 0:
            user_input = input("Guess a letter or a word: \n>>> ").lower()
            if len(user_input) > 1:
                self.guess_word(user_input)
            else:
                self.guess_letter(user_input)
            
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
    hangman_game.play()