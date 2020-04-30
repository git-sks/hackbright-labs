"""A number-guessing game."""

import random

# Initial greeting
print('Hi!')

# Get player name and print confirmation message
player_name = input("What's your name? ")
print("Nice to meet you, " + player_name + ".")

# Get a random number between 1 and 100 to guess
num_to_guess = random.randint(1, 100)
# print("The random number is", num_to_guess) #for testing

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
        elif player_guess_int == num_to_guess:
            print("Congratulations! You've guessed the number!")
            break
        elif player_guess_int < num_to_guess:
            print("Sorry, you've guessed too low. Try again.")
        elif player_guess_int > num_to_guess:
            print("Sorry, you've guessed too high. Try again.")
    except ValueError:
        # If player guess is not a number, handle error gracefully
        print("Hey, that's not a number! Try again.")