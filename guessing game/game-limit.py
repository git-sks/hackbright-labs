"""A number-guessing game where player has a limited number of guesses"""

# set a max number of guesses
# create a variable to track number of guesses

import random


def play_game():
    """Starts a single game loop for the player.

    Returns player's score"""

    # Get a random number between 1 and 100 to guess
    num_to_guess = random.randint(1, 100)
    # print("The random number is", num_to_guess) #for testing

    # (re)set player's number of guesses to 0 for new game
    num_guesses = 0

    while True:
        # Get player's guess
        print("Guess a number between 1 and 100.")
        player_guess = input("> ")
        print("You guessed", player_guess)

        try:
            player_guess_int = int(player_guess)
            # Make sure player guess is within range
            if player_guess_int < 1 or player_guess_int > 100:
                print("Hey, that's not within range! Try again.")

            # Congratulate and end game if guessed correctly, otherwise give a hint
            else:
                # only increase number of guesses if it's a valid guess
                num_guesses = num_guesses + 1

                if player_guess_int == num_to_guess:
                    print("Congratulations! You've guessed the number!")
                    break
                elif player_guess_int < num_to_guess:
                    print("Sorry, you've guessed too low. Try again.")
                elif player_guess_int > num_to_guess:
                    print("Sorry, you've guessed too high. Try again.")
        except ValueError:
            # If player guess is not a number, handle error gracefully
            print("Hey, that's not a number! Try again.")

    return num_guesses


def start_session():
    """Starts a game session for the player."""

    # Initial greeting
    print('Hi!')

    # Get player name and print confirmation message
    player_name = input("What's your name? ")
    print("Nice to meet you, " + player_name + ".")

    # Initiate current high score for session. 0 means it's a new session/no high score.
    high_score = 0

    while True:
        # Have the user begin the game loop and then get their score from one play
        score = play_game()

        print()
        print("You won in", score, "guesses.")
        print()

        # flag to check if program should run another game round based on user response
        # defaults to False
        replay_flag = False

        while True:
            # Get whether user wants to play again or not
            print("Would you like to play again?")
            replay = input("> ")
            replay = replay.lower()

            print()

            if replay.startswith("n"):
                # Assumes any response beginning w/ n is a negative response
                # no need to change replay flag because by default is false
                # break out of play again? input loop
                print("Thanks for playing! Goodbye.")
                break
            elif replay.startswith("y"):
                # Assumes any response beginning w/ y is a positive response
                # change replay flag to true
                # break out of play again? input loop
                replay_flag = True
                break
            else:
                # If doesn't begin wiht y or n, then invalid response
                # go through the play again? input loop once more
                print("That is not a valid response. Try again.")
                print()

        # break out of the game loop if replay_flag is False
        if replay_flag == False:
            break



start_session()