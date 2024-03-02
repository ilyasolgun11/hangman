class ClearTerminal:
    """
    Clears the terminal above of where it is placed
    """

    @staticmethod
    def clear_terminal():
        print("\033c", end="") 
