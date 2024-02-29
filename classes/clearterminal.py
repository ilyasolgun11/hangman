import os


class ClearTerminal:

    @staticmethod
    def clear_terminal():
        command = 'clear'
        if os.name in (
                'nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
