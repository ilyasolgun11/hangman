import random

words = [
     "about", "after", "again", "airplane", "almost", "always", "animal", "another", "answer", "apartment",
    "apple", "arrive", "article", "asking", "athlete", "attention", "average", "awesome", "balance", "because",
    "before", "believe", "beneath", "between", "beyond", "bicycle", "birthday", "blanket", "building", "butterfly",
    "camera", "capital", "careful", "certain", "champion", "children", "chocolate", "clothing", "colorful", "comfortable",
    "community", "complete", "continue", "contribute", "convention", "courageous", "curious", "dangerous",
    "daughter", "decide", "delicious", "describe", "design", "different", "direction", "discover", "discussion", "education",
    "electric", "elephant", "emergency", "enormous", "entertain", "environment", "everywhere", "excellent", "exercise", "experience",
    "explain", "familiar", "favorite", "February", "fireplace", "football", "forever", "forget", "fortunate", "friendship",
    "generous", "gentleman", "government", "grandmother", "happiness", "health", "heartfelt", "helicopter", "holiday",
    "hospital", "important", "impossible", "incredible", "information", "innocent", "interesting", "invisible", "invitation", "January",
    "journey", "knowledge", "landscape", "language", "laughter", "learning", "leisure", "library", "listening", "literature",
    "lollipop", "lunchtime", "magazine", "magnificent", "management", "marriage", "measurement", "meditate", "memory", "mermaid",
    "message", "millionaire", "minimize", "miracle", "moment", "necessary", "neighborhood", "nighttime", "nonsense", "nothing",
    "November", "numerous", "obstacle", "occupation", "ocean", "offensive", "official", "operation", "opportunity", "optimistic",
    "organization", "outstanding", "overcome", "pancake", "paradise", "participate", "passenger", "peaceful", "penguin", "percentage",
    "performance", "permission", "photograph", "physical", "pleasure", "politeness", "population", "possibility", "potato", "practical",
    "precious", "preparation", "principle", "procedure", "procrastinate", "productive", "profession", "promenade", "promotion", "property",
    "prosperity", "punishment", "puzzle", "quarrel", "question", "quietly", "quintessence", "quotation", "radiance", "realize",
    "reasonable", "reception", "recognition", "rectangle", "reflection", "relaxation", "remarkable", "remembrance", "renewable", "repair",
    "resistance", "restaurant", "revolution", "satisfaction", "secretary", "sensation", "sensitive", "separation", "serious", "shimmer",
    "signature", "significant", "silhouette", "simultaneously", "slumber", "solitude", "spectacular", "spirit", "spontaneous", "strawberry",
    "substantial", "successful", "sufficient", "sumptuous", "superior", "support", "surprise", "suspension", "symphony", "technology",
    "telegraph", "telephone", "television", "temperature", "thankful", "thorough", "thoughtful", "thousand", "tomorrow", "trampoline",
    "transformation", "tranquil", "transparent", "treasure", "triangle", "tropical", "twilight", "umbrella", "understanding", "unexpected",
    "university", "unlimited", "valuable", "vegetable", "venture", "victory", "vintage", "visibility", "volunteer", "voyage", "waterfall",
    "weather", "wedding", "whisper", "wilderness", "winter", "wonderful", "worry", "writing", "yearning", "yesterday", "zeppelin"
]

def random_word():
    """
    Gets a random word within the words list
    """
    return random.choice(words)