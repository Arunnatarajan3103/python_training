import random

def main():
    # Generating a random number between 1 and 6
    roll = random.randint(1, 6)
   # For debugging

    # Taking user input
    user_guess = input("Guess a number between 1 and 6: ")

    try:
        user_guess = int(user_guess)  # Convert input to an integer

        if 1 <= user_guess <= 6:  # Check if the input is within range
            if user_guess == roll:
                print("You guessed correctly!")
            else:
                print("Better luck next time.")
        else:
            print("Your guess must be a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")

# Run the main function
main()