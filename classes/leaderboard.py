import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET_NAME = 'ultimate-hangman-leaderboard'
SHEET = GSPREAD_CLIENT.open(SPREADSHEET_NAME)

class Leaderboard():

    @staticmethod
    def append_to_worksheet(sheet, data):
        return SHEET.worksheet(sheet).append_row(data)
    
    @staticmethod
    def get_leaderboard_data(mode):
        """
        Gets leaderboard data from google sheets and displays the top 15 highest scores, also gives user the option
        to play again, choose a different modes leaderboard or exit the game
        """
        leaderboard_sheet = SHEET.worksheet(mode)
        leaderboard_data = leaderboard_sheet.get_all_records()
        sorted_leaderboard = sorted(
            leaderboard_data,
            key=lambda x: x['Points'],
            reverse=True)
        if mode == "easy mode":
            leaderboard_header_mode = "E A S Y   M O D E"
        elif mode == "intermediate mode":
            leaderboard_header_mode = "I N T E R M E D I A T E    M O D E"
        elif mode == "hard mode":
            leaderboard_header_mode = "H A R D    M O D E"
        print(
            Fore.YELLOW +
            "--------------------------------------------------------------------------------")
        print(
            Fore.YELLOW +
            f"  T O P   1 5   L E A D E R B O A R D  |  {leaderboard_header_mode}")
        print(
            Fore.YELLOW +
            "--------------------------------------------------------------------------------\n")
        print(
            Fore.BLUE +
            "POSITION  NAME      POINTS LOCATION    DATE        TIME TO WIN    WORD        HINT USED?")
        # Using the data from worksheet.get_all_records(), the data is displayed with designated column widths to separate
        # columns evenly without overflow
        for position, player_data in enumerate(
                sorted_leaderboard[:15], start=1):
            position_str = str(position).ljust(10)
            name_str = player_data['Name'].ljust(10).capitalize()
            points_str = str(player_data['Points']).ljust(7)
            location_str = player_data['Country/City'].ljust(12).capitalize()
            date_str = player_data['Date'].ljust(12)
            time_to_win_str = player_data['Time to win'].ljust(15)
            winning_word = player_data['Winning word'].ljust(12).capitalize()
            hint_used = player_data['Hint used?'].ljust(12).capitalize()
            print(Fore.GREEN + f"""{position_str}{name_str}{points_str}{location_str}{
                  date_str}{time_to_win_str}{winning_word}{hint_used}""")