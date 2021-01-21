#!/usr/bin/env python
import logging
import os
import pathlib
from art import logo
from hanged import Hanged

logfile = pathlib.Path(f'{os.getcwd()}/logs.log')
logging.basicConfig(filename=logfile, format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')
logging.info("Import of modules succeded")


def main():
    game_on = True
    # Creating an instance
    hangman = Hanged()
    print(logo)
    #  Get the user guess input

    # Perpetual guess
    logging.info("Start of game_on")

    while game_on:

        guess = input("Guess a letter: ").lower()
        if hangman.handle_input(guess):
            if guess in hangman.final_word:
                hangman.transition(guess)
            else:
                hangman.life = hangman.life - 1
                print("You  guessed: %s but is not in this word... you are getting hanged" % guess)
                print(hangman.life_art[hangman.life])

            print(hangman.transition_word)
            # Stop the loop if user won
            if hangman.transition_word == hangman.final_word:
                print("Congratulations, You won ;) ")
                game_on = False

            if hangman.life == 0:
                print("You loose, you got hanged! ")
                print("Final word was: %s" % hangman.final_word)
                game_on = False

    logging.info("End of game_on")


if __name__ == '__main__':
    try:
        logging.info("+-------------------INITIALIZING GAME------------------------+")
        main()
        logging.info("+-------------------GAME SUCCESSFULLY ENDED------------------+")
    except Exception:
        logging.exception("Unable to start the game")
        print("Unable to start the game, check the logs for more INFO about why")
        raise

    closeInput = input("Press ENTER to exit")
    print("Closing...")
