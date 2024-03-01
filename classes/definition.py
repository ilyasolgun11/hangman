import colorama
from colorama import Fore
colorama.init(autoreset=True)
import requests
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='env.py')
api_key = os.getenv('API_KEY')

class GrabDefinition:
       """
       Class representing the definition functionality of the hangman game
       """
       
       @staticmethod
       def grab_word_definition(word):
            # URL in which would be used to gather the definition data for the self.hangman_word
            # if the user decides to use the hint token 
            url = f"""https://dictionary-data-api.p.rapidapi.com/definition/{
                word}"""
            # Header that would be used alongside with the url to gather definition data of
            # the self.hangman_word, and holds the secret api key which is being held 
            # in the env.py file
            headers = {'X-RapidAPI-Key': api_key}
            response = requests.get(url, headers=headers)
            # If the data is grabbed successfully, do the following
            try:
                if response.status_code == 200:
                    data = response.json()
                    meanings = data.get('meaning', [])
                    if meanings:
                        definition = meanings[0]["values"][0]
                        # Display definition to player and hide the word by replacing 
                        # it with "(hidden correct word)"
                        print(
                            Fore.BLUE +
                            f"""Definition of word: {
                                definition.replace(
                                    word,
                                    '(hidden correct word)')}""")
                    else:
                        # If no definition is found, let the player know
                        print("No meanings found.")
                else:
                    # If no data has been grabbed, let the player know
                    print(f"Error: Sorry, no definitions found...")
            except Exception as e:
                # Handle any exception that may occur
                print(f"An error occurred: {e}")