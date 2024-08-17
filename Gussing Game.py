import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None
    
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    
    while guess != secret_number:
        # Prompt the user to enter their guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Compare the guess to the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

# Start the game
guessing_game()
