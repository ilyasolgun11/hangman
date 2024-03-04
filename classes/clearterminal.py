import os

class ClearTerminal:
    """
    Clears the terminal above of where it is placed
    """

    @staticmethod
    # Taken from https://www.delftstack.com/howto/python/python-clear-console/
    def clear_terminal():
        command = 'clear'
        if os.name in (
                'nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
        print("\033c", end="") 
