from words import random_word

def game():
    hangman_word = random_word()
    print(hangman_word)
    score = 7
    guessed_letters = []
    guessed_correct_letters = []
    guessed_word = []
    while score > 0:
        user_input = input("Guess a letter in the word: ")
        if len(user_input) > 1:
            print("You guessed a word")
            if user_input == hangman_word:
                guessed_word.append(user_input)
                print(f"You won! the word was {hangman_word}")
                break
            else:
                 guessed_word.append(user_input)
                 print(guessed_word)
                 score -= 1
                 print(f"False {user_input} is not the word, your score is now {score}")
        else: 
            if user_input in guessed_letters:
                print(f"You have guessed {user_input} already.")
                print(guessed_letters)
            elif user_input in hangman_word:
                guessed_correct_letters.append(user_input)
                guessed_letters.append(user_input)
                print("Correct!")
                if set(guessed_correct_letters) == set(set(hangman_word)):
                    print(f"You won! The word was {hangman_word}")
                    print(guessed_correct_letters)
                    break
            else:
                guessed_letters.append(user_input)
                score -= 1
                print(f"False {user_input} is not in the word, your score is now {score}")

        if score == 0:
            print("You have lost")
            break
game()