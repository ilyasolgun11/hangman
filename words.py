import random

words = [
    "tiger", "river", "smile", "ocean", "happy", "candle", "sunny", "cloud", "pizza", "music"
]

def random_word():
    """
    Gets a random word within the words list
    """
    return random.choice(words)