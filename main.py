from hanged import Hanged
from art import logo


def main():
    game_on = True
    # Creating an instance
    hangman = Hanged()
    print(hangman.final_word)
    print(logo)
    #  Get the user guess input

    # Perpetual guess
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


if __name__ == '__main__':
    main()

