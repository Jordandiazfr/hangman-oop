from art import stages
import requests


def load_word():
    word = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    purified_word = word.text[2:-2]
    list_word = [i for i in purified_word]
    return list_word

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
        for letter in range(self.length):
            if guess == self.final_word[letter]:
                self.transition_word[letter] = guess
