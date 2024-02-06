from words import random_word

def game():
    hangman_word = random_word()
    score = 7
    while score > 0:
        user_input = input("Guess a letter in the word \n")
        if user_input in hangman_word:
            print(f"Correct!")
        else:
            score -= 1
            print(f"False {user_input} in not in the word, your score is now {score}")
        if score == 0:
            print("You have lost")
            break
game()