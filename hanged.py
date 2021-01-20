from art import stages
import requests
import logging

def load_word():
    try:
        api = "https://random-word-api.herokuapp.om/word?number=1"
        word = requests.get()
        purified_word = word.text[2:-2]
        list_word = [i for i in purified_word]
        logging.info("RANDOM WORD SUCCESFULLY LOADED FROM THE API")
        return list_word
    except:
        logging.error("API ERROR: Couldn't complete the get request from: %s " % api)
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
