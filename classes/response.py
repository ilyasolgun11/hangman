import requests
import os
from dotenv import load_dotenv
import colorama
from colorama import Fore
colorama.init(autoreset=True)
load_dotenv(dotenv_path='env.py')
api_key = os.getenv('API_KEY')


class GrabResponse:
    """
    Class representing the response functionality
    of the hangman game
    """
    @staticmethod
    def grab_word_definition(word):
        print(Fore.LIGHTYELLOW_EX + "Grabbing definition...")
        url = f"https://dictionary-data-api.\
p.rapidapi.com/definition/{word}"
        headers = {'X-RapidAPI-Key': api_key}
        response = requests.get(url, headers=headers)
        # If the data is grabbed successfully, do the following
        try:
            if response.status_code == 200:
                data = response.json()
                meanings = data.get('meaning', [])
                if meanings:
                    definition = meanings[0]["values"][0]
                    print(Fore.LIGHTCYAN_EX + f"Definition of word: \
{definition.replace(word, '(hidden correct word)')}" + Fore.RESET)
                else:
                    print("No meanings found.")
            else:
                print(f"Error: Sorry, no definitions found...")
        except Exception as e:
            # Handle any exception that may occur
            print(f"An error occurred: {e}")

    @staticmethod
    def grab_country_data(country):
        print(Fore.LIGHTYELLOW_EX + "Grabbing country data...")
        url = f"https://geography4.p.rapidapi.com/apis\
/geography/v1/country/name/{country}"
        headers = {'X-RapidAPI-Key': api_key}
        response = requests.get(url, headers=headers)
        # If the data is grabbed successfully, do the following
        try:
            if response.status_code == 200:
                data = response.json()
                country_data_list = data[0]
                region = country_data_list.get('region', '')
                capital_list = country_data_list.get('capital', [])
                capital = capital_list[0].get('name')
                currency_list = country_data_list.get('currencies', [])
                currency = currency_list[0].get('alphaCode')
                print(Fore.LIGHTCYAN_EX + f"This country is in the region\
 of {region} and it's capital city is {capital}\nand they use the currency\
 with the alpha code of{currency}" + Fore.RESET)
            else:
                # If no data has been grabbed, let the player know
                print(f"Error: Sorry, no definitions found...")
        except Exception as e:
            # Handle any exception that may occur
            print(f"An error occurred: {e}")
