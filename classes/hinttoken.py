from .definition import GrabDefinition


class HintToken(GrabDefinition):
    """
    Class representing the hint token functionality of the hangman game
    """
    def __init__(self):
        super().__init__()

    def use_hint_token(self, word, worksheet):
        if worksheet != "country mode":
            self.grab_word_definition(word)
        else:
            self.grab_country_data(word)
