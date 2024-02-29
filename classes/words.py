import random

class RandomWord:
    """
    Class representing the words used in the hangman game.
    """
    def __init__(self):
        self.easy_mode = ["about", "after", "again", "apple", "arrive", "asking", "athlete", "before", "being", "below",
              "blank", "blend", "bread", "brief", "bring", "build", "bunch", "burst", "cake", "cause",
              "chair", "child", "climb", "close", "color", "could", "cover", "cream", "dance", "design",
              "doing", "early", "earth", "enjoy", "event", "every", "explore", "fence", "field", "first",
              "flame", "floor", "flower", "fresh", "fruit", "funny", "gather", "gift", "glide", "going"]
        self.intermediate_mode = ["balance", "because",
            "before", "believe", "beneath", "between", "beyond", "bicycle", "birthday", "blanket", "building", "butterfly",
            "camera", "capital", "careful", "certain", "champion", "children", "chocolate", "clothing", "colorful", "comfortable", "complete", "continue", "contribute", "convention", "courageous", "curious", "dangerous",
            "daughter", "decide", "delicious", "describe", "design", "different", "direction", "discover", "discussion", "education",
            "electric", "elephant", "emergency", "enormous", "entertain", "environment", "everywhere", "excellent", "exercise", "experience",
            "explain", "familiar", "favorite", "February", "fireplace", "football", "forever", "forget"]
        self.hard_mode = ['elephant', 'computer', 'symphony', 'template', 'essential', 'permanent', 'knowledge', 'algorithm', 'beautiful', 'attention', 'magnificent', 'celebrate', 'challenge', 'experience', 'community', 'incredible', 'adventure', 'wonderful', 'existence', 'efficiency', 'definitely', 'discipline', 'restaurant', 'boulevard', 'expensive', 'enthusiasm', 'principle', 'frustrate', 'investment', 'integrate', 'recognize', 'individual', 'curriculum', 'throughout', 'technology', 'productive', 'happiness', 'restaurant', 'opportunity', 'education', 'contribute', 'celebration', 'achievement', 'consequence', 'creativity', 'innovation', 'tremendous', 'adaptation', 'imagination', 'experiment', 'perseverance', 'courageous', 'enthusiastic', 'exploration', 'revolution', 'extraordinary', 'spectacular', 'fascinating', 'evolution', 'interaction', 'remarkable', 'congratulate', 'organization', 'experience', 'understand', 'communication', 'preference', 'implement', 'motivation', 'technology', 'communication', 'appearance', 'celebration', 'considerate', 'temperature', 'recognition', 'engineering', 'sophisticated', 'particularly', 'investment', 'opportunity', 'intelligence', 'entertainment', 'contribution', 'achievement', 'encouragement', 'relationship', 'architecture', 'significant', 'information', 'enthusiastically', 'relationship', 'communication', 'architecture', 'congratulation', 'celebration', 'exaggeration', 'understanding', 'extraordinary', 'communication']

    def game_modes(self, mode):
        if mode == "easy mode":
            return random.choice(self.easy_mode)
        elif mode == "intermediate mode":
            return random.choice(self.intermediate_mode)
        elif mode == "hard mode":
            return random.choice(self.hard_mode)

