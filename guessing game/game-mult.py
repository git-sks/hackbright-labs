"""A number-guessing game with multiple rounds."""

# for multiple rounds
# create a variable to track current high score
# in a continuous loop
#   get a random number
#   track player's num of guesses, initiating it at 0
#   go through game loop of player guessing the number
#       player's num of guesses should be +1'd every time a guess is made
#   once number is guessed, check if a current high score exists
#       if one exists, check if user's num guesses lower than high score's num guesses
#           if so, congratulate the user on a new high score
#       otherwise just display current high score alongside user's current score
#   if a current high score doesn't exist
#       update the current high score so it's the user's current score

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


def update_high_score(curr_score, high_score):
    """Checks if current score is the new high score or not.

    Returns the high score."""

    if (high_score == 0) or (curr_score < high_score):
        # high_score being 0 means no high score currently,
        # or curr_score < high_score means player won with fewer guesses
        # so return the current score as the high score
        print("You have the new high score!")
        return curr_score
    else:
        # keep high score the same
        print("The current high score is", high_score, "guesses.")
        return high_score




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

        # Update current high score
        high_score = update_high_score(score, high_score)

        print()
        print("You won in", score, "guesses.")
        print()

        replay_flag = False

        while True:
            print("Would you like to play again?")
            replay = input("> ")
            replay = replay.lower()

            print()

            if replay.startswith("n"):
                print("Thanks for playing! Goodbye.")
                break
            elif replay.startswith("y"):
                replay_flag = True
                break
            else:
                print("That is not a valid response. Try again.")
                print()

        if replay_flag == False:
            break



start_session()