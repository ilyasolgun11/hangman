import random

words = [
    "apple", "blue", "cat", "dog", "elephant", "feather", "guitar", "happy", "ice cream", "jump",
    "kite", "lemon", "moon", "nest", "orange", "puzzle", "quiet", "rainbow", "sunny", "tree",
    "umbrella", "violet", "watermelon", "xylophone", "yellow", "zebra", "basket", "cloud", "daisy",
    "firefly", "garden", "honey", "island", "jungle", "kiwi", "lighthouse", "mango", "notebook",
    "ocean", "penguin", "quilt", "river", "sailboat", "tulip", "unicorn", "vase", "whistle",
    "xylograph", "yarn", "zipper", "acrobat", "balloon", "carousel", "dolphin", "eclipse", "fountain",
    "globe", "harp", "iguana", "jigsaw", "kangaroo", "leopard", "muffin", "nightingale", "octopus",
    "parrot", "quasar", "rhinoceros", "saxophone", "tambourine", "ukulele", "violin", "whale", "x-ray",
    "yacht", "zeppelin", "astronomy", "butterfly", "caramel", "diamond", "envelope", "frost", "giraffe",
    "hurricane", "illusion", "jackal", "knight", "lagoon", "marble", "nougat", "obsidian", "puzzle",
    "quartz", "raccoon", "sapphire", "telescope", "unicorn", "velvet", "waffle", "xenon", "yellowstone",
    "zipper", "abacus", "ballet", "cappuccino", "dinosaur", "eucalyptus", "frisbee", "gazelle", "hologram",
    "infantry", "jamboree", "kangaroo", "labyrinth", "marmalade", "nirvana", "onomatopoeia", "paradox",
    "quintessence", "radiance", "serendipity", "trampoline", "utopia", "vagabond", "whirlwind", "xenophobia",
    "yodel", "zeppelin", "amazing", "breeze", "chocolate", "dancer", "enjoy", "festival", "graceful", "harmony", "illusion", "joyful",
    "kaleidoscope", "lullaby", "mystic", "navigate", "opulent", "piano", "quaint", "resilient", "serene", "tranquil",
    "universe", "vibrant", "whisper", "xylophonist", "yearning", "zenith", "bliss", "cascade", "delight", "effervescent",
    "fantasy", "glisten", "happiness", "inspire", "journey", "kismet", "luminary", "mesmerize", "nirvana", "oasis",
    "paradise", "quasar", "rhapsody", "serendipity", "talisman", "unwind", "vortex", "wanderlust", "xylography",
    "yonder", "zeal", "alchemy", "bountiful", "crescent", "dazzle", "ecstasy", "flourish", "gossamer", "hallowed",
    "illuminate", "jubilant", "kiss", "labyrinth", "mirth", "nebula", "onyx", "palette", "quixotic", "rapture",
    "savor", "twilight", "utopian", "vivid", "whimsical", "xanadu", "youthful", "zeppelin", "ambrosia", "bucolic",
    "celestial", "dewdrop", "elation", "fandango", "gazebo", "halcyon", "incandescent", "jocund", "kaleidoscopic",
    "luminous", "melody", "nymph", "overture", "phantasmagoria", "quiescent", "rhapsodic", "seraphic", "tranquility",
    "unfurl", "verdant", "whiff", "xylitol", "yearn", "zephyr", "allegro", "balletic", "cynosure", "diaphanous",
    "efflorescence", "felicity", "gloaming", "halo", "ineffable", "juxtapose", "kowtow", "languid", "mellifluous",
    "nostalgia", "oblivion", "peregrinate", "quintessential", "resplendent", "sonorous", "tryst", "ubiquitous",
    "veritable", "wistful", "xenial", "yarn", "zestful"
]

def random_word():
    """
    Gets a random word within the words list
    """
    return random.choice(words)