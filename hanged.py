from art import stages
import json
import random


def load_word():
    f = open("words.json")
    data = json.load(f)
    return data['words']


def select_winner():
    choose = random.choice(load_word())
    winner = [win.lower() for win in choose]
    return winner


class Hanged:
    def __init__(self):
        self.life = 7
        self.life_art = stages
        self.final_word = select_winner()
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
