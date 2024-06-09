
import random

def guess_num():
    # Generate a random number between 1 and 50
    secret_num = random.randint(1, 10)
    
    # Set the number of attempts
    attempt = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 50. Can you guess it?")
    
    while True:
        # Get user input
        guess = int(input("Enter your guess: "))
        # Increment the number of attempts
        attempt += 1
        
        # Check if the guess is correct or not
        if guess == secret_num:
            print(f"Congratulations! You've guessed the number in {attempt} attempt!")
            break
        # when user guess wrong number 
        else:
            print("You guess wrong number! Try again.")

# Start the game
guess_num() 