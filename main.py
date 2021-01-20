import logging
import pathlib
import os
from hanged import Hanged
from art import logo
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
    logging.info("Start of while loop")
    while game_on:
        guess = input("Guess a letter: ").lower()
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
            print("Final word was: %s" % hangman.final_word
                  )
            game_on = False
    logging.info("End of while loop")

if __name__ == '__main__':
    try:
        logging.info("+-------------------INITIALIZING GAME------------------------+")
        main()
    except:
        logging.exception("Unable to start the game")
        print("Unable to start the game, check the logs for more INFO about why")
        raise

