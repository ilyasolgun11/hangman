import random


class RandomWord:
    """
    Class representing the words used in the hangman game.
    """
    def __init__(self):
        self.words = [
            "about", "after", "again", "apple", "arrive", "asking",
            "athlete", "before", "being", "below"
            "blank", "blend", "bread", "brief", "bring", "build", "bunch",
            "burst", "cake", "cause", "chair", "child", "climb", "close",
            "color", "could", "cover", "dance", "design", "doing",
            "early", "earth", "enjoy", "event", "every", "explore", "fence",
            "field", "first", "flame", "floor", "flower", "fresh", "fruit",
            "funny", "gather", "gift", "glide", "going"
            "balance", "because", "before", "believe", "beneath", "between"
            "beyond", "bicycle", "birthday", "blanket", "building",
            "butterfly", "camera", "capital", "careful", "certain",
            "champion", "children", "chocolate", "clothing", "colorful",
            "comfortable", "complete", "continue", "contribute", "convention",
            "courageous", "curious", "dangerous", "daughter", "decide",
            "delicious", "describe", "design", "different", "direction",
            "discover",  "discussion", "education", "electric", "elephant",
            "emergency", "enormous",  "entertain", "environment", "everywhere",
            "excellent", "exercise", "experience",
            "explain", "familiar", "favorite", "february", "fireplace",
            "football", "forever",  "forget", "elephant", "computer",
            "symphony", "template", "essential", "permanent",
            "knowledge", "algorithm", "beautiful", "attention",
            "magnificent", "celebrate", "challenge", "experience",
            "community", "incredible", "adventure", "wonderful",
            "existence", "efficiency", "definitely", "discipline",
            "restaurant", "boulevard",  "expensive", "enthusiasm", "principle",
            "frustrate", "investment", "integrate",  "recognize", "individual",
            "curriculum", "throughout", "technology", "productive",
            "happiness", "restaurant", "opportunity", "education",
            "contribute", "celebration", "achievement", "consequence",
            "creativity", "innovation", "tremendous", "adaptation",
            "imagination", "experiment", "perseverance", "courageous",
            "enthusiastic", "exploration", "revolution", "extraordinary",
            "spectacular", "fascinating",  "evolution", "interaction",
            "remarkable", "congratulate", "organization",
            "experience", "understand", "communication", "preference",
            "implement", "motivation", "technology", "communication",
            "appearance", "celebration", "considerate",
            "temperature", "recognition", "engineering", "sophisticated",
            "particularly", "investment", "opportunity", "intelligence",
            "entertainment", "contribution", "achievement", "encouragement",
            "relationship", "architecture", "significant",
            "information", "enthusiastically", "relationship", "communication",
            "architecture", "congratulation", "celebration", "exaggeration",
            "understanding", "extraordinary", "communication", "sunshine",
            "mountain", "ocean", "breeze", "adventure", "journey",
            "discovery", "harmony", "inspiration", "tranquil", "whisper",
            "serenity", "captivate", "freedom", "imagine", "reflection",
            "glisten", "effervescent", "lullaby", "luminescent", "mystical",
            "nostalgia", "paradise", "quintessence", "resplendent", "savor",
            "twilight", "vivid", "whimsical", "enchanted", "bewitch",
            "celestial", "cosmic", "delight", "ethereal", "fascinate",
            "galaxy", "happiness", "illuminate", "luminary"
            "marvel", "nurture", "orchestrate", "paragon", "quasar",
            "radiant", "sublime", "timeless", "universe", "velvet",
            "wanderlust", "xanadu", "yearning", "zenith",
            "effulgent", "spectacle", "exquisite", "bliss",
            "euphoria", "rhapsody", "breathtaking", "enchanting",
            "mellifluous", "opulent", "panorama", "quiescent",
            "resonance", "serendipity", "tranquility", "umbrella",
            "verdant", "whirlwind", "xylophone", "yardstick", "zeppelin"]

        self.countries = [
            "albania", "algeria", "andorra", "angola", "argentina",
            "armenia", "australia", "austria", "azerbaijan",
            "bahrain", "bangladesh", "belarus", "belgium", "belize",
            "benin", "bhutan", "bolivia", "bosnia", "botswana",
            "brazil", "brunei", "bulgaria", "burundi", "cambodia",
            "cameroon", "canada", "chad", "chile", "china",
            "colombia", "comoros", "congo", "croatia", "cuba", "cyprus",
            "denmark", "djibouti", "ecuador", "egypt",
            "estonia", "ethiopia", "finland", "france", "gabon", "gambia",
            "georgia", "germany", "ghana", "greece",
            "guatemala", "guinea", "guyana", "haiti", "honduras", "hungary",
            "iceland", "india", "indonesia", "iran",
            "iraq", "ireland", "israel", "italy", "jamaica", "japan",
            "jordan", "kazakhstan", "kenya", "kiribati",
            "kuwait", "kyrgyzstan", "latvia", "lebanon", "lesotho", "liberia",
            "libya", "liechtenstein", "lithuania",
            "luxembourg", "madagascar", "malawi", "malaysia", "mali",
            "malta", "mauritania", "mexico", "moldova",
            "monaco", "mongolia", "montenegro", "morocco", "mozambique",
            "namibia", "nepal", "netherlands",
            "nicaragua", "niger", "nigeria", "norway", "oman", "pakistan",
            "palau", "panama", "paraguay", "peru",
            "philippines", "poland", "portugal", "qatar", "romania",
            "rwanda", "samoa", "senegal", "serbia", "seychelles",
            "singapore", "slovakia", "slovenia", "somalia", "spain",
            "sudan", "suriname", "sweden", "switzerland",
            "syria", "taiwan", "tajikistan", "tanzania", "thailand",
            "togo", "tonga", "trinidad", "tunisia", "turkey",
            "turkmenistan", "uganda", "ukraine", "uruguay", "uzbekistan",
            "vanuatu", "venezuela", "vietnam", "yemen",
            "zambia", "zimbabwe"]

    def game_modes(self, mode):
        """
        Using list comprehension, gathering all words in self.words
        and splitting them up into modes by checking their length
        """
        easy_mode = [word for word in self.words if len(word) < 6]
        intermediate_mode = [word for word in self.words if 6 < len(word) < 8]
        hard_mode = [word for word in self.words if len(word) > 8]
        if mode == "easy mode":
            return random.choice(easy_mode)
        elif mode == "intermediate mode":
            return random.choice(intermediate_mode)
        elif mode == "hard mode":
            return random.choice(hard_mode)
        elif mode == "country mode":
            return random.choice(self.countries)
