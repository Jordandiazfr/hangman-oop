from art import stages
import requests
import logging

API = "https://random-word-api.herokuapp.com/word?number=1"

def handle_input(input):
    """ Checks the user input to make sure he puts only one letter from to A - Z """
    if not input.isalpha() or len(input) > 1:
        logging.debug("User input was not the expected")
        print(" You must guess ONLY ONE letter from A to Z")
        return False
    return True


def load_word():
    """ Send a request to the selected api and is expecting a random string formmated ['string'] """
    try:
        word = requests.get(API)
        purified_word = word.text[2:-2]
        list_word = [i for i in purified_word]
        logging.info("RANDOM WORD SUCCESFULLY LOADED FROM THE API")

        return list_word
    except:
        logging.error("SERVER ERROR o USER IS NOT CONNECTED TO INTERNET: Couldn't complete the get request from: %s " % API)
        print("THERE IS A SERVER ERROR, MAKE SURE YOU ARE CONNECTED TO THE INTERNET")
        return 0


class Hanged:
    def __init__(self):
        self.life = 7
        self.life_art = stages
        self.final_word = load_word()
        self.initial_blank = self.create_blanks()
        self.transition_word = self.initial_blank
        self.length = len(self.final_word)
        self.guessed_words = []
        logging.info("Object initiated")

    def create_blanks(self) -> list:
        blanks = ['_' for i in self.final_word]
        return blanks

    def transition(self, guess):
        if guess not in self.guessed_words:
            for letter in range(self.length):
                if guess == self.final_word[letter]:
                    self.transition_word[letter] = guess
                    self.guessed_words.append(guess)
        else:
            print("You already guessed that word.")
