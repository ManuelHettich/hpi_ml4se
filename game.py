import random

def number_guessing_game(low, high, rounds):
    print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {low} and {high}.")

    # Generate a random number
    number = random.randint(low, high)
    
    for _ in range(rounds):
        guess = input(f"Enter your guess (Round {_+1}/{rounds}): ")

        # Convert the guess to a number
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check the guess
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            return

    print(f"Sorry, you've run out of rounds. The number was {number}.")

# Example of running the game with range 1 to 100 and 5 rounds
number_guessing_game(1, 100, 5)
