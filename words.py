import random

easy_mode = ["about", "after", "again", "apple", "arrive", "asking", "athlete", "before", "being", "below",
              "blank", "blend", "bread", "brief", "bring", "build", "bunch", "burst", "cake", "cause",
              "chair", "child", "climb", "close", "color", "could", "cover", "cream", "dance", "design",
              "doing", "early", "earth", "enjoy", "event", "every", "explore", "fence", "field", "first",
              "flame", "floor", "flower", "fresh", "fruit", "funny", "gather", "gift", "glide", "going"]

intermediate_mode = ["balance", "because",
    "before", "believe", "beneath", "between", "beyond", "bicycle", "birthday", "blanket", "building", "butterfly",
    "camera", "capital", "careful", "certain", "champion", "children", "chocolate", "clothing", "colorful", "comfortable", "complete", "continue", "contribute", "convention", "courageous", "curious", "dangerous",
    "daughter", "decide", "delicious", "describe", "design", "different", "direction", "discover", "discussion", "education",
    "electric", "elephant", "emergency", "enormous", "entertain", "environment", "everywhere", "excellent", "exercise", "experience",
    "explain", "familiar", "favorite", "February", "fireplace", "football", "forever", "forget"]

hard_mode = [
    "meticulous", "profound", "ubiquitous", "ephemeral", "serendipity", "quintessential", "ephemeral", "paradigm", "ineffable", "vernacular",
    "effervescent", "obfuscate", "innuendo", "vicissitude", "labyrinthine", "sesquipedalian", "mellifluous", "antithesis", "esoteric", "recalcitrant",
    "insidious", "disparate", "ostentatious", "nonchalant", "disparate", "perfidious", "pedantic", "perspicacious", "disparate", "disparate",
    "disparate", "pernicious", "recalcitrant", "ubiquitous", "vexatious", "idiosyncrasy", "lackadaisical", "languid", "quizzical", "sycophant",
    "zeitgeist", "alacrity", "quandary", "disparate", "inchoate", "indolent", "proclivity", "disparate", "paradoxical", "ephemeral",
    "obfuscate", "disparate", "disparate", "plethora", "idiosyncrasy", "disparate", "disparate", "quizzical", "profound", "quandary",
    "disparate", "quixotic", "disparate", "disparate", "quizzical", "profound", "quandary", "disparate", "quizzical", "profound"
]

def random_word(mode):
    """
    Gets a random word within the words list
    """
    if mode == "easy mode":
        return random.choice(easy_mode)
    elif mode == "intermediate mode":
        return random.choice(intermediate_mode)
    elif mode == "hard mode":
        return random.choice(hard_mode)
    else:
        raise ValueError(f"Invalid mode: {mode}")
    