Here's a README file for your guessing game code:

---

# Guessing Game

## Description

This is a simple command-line game where the user is challenged to guess a randomly generated number between 1 and 100. The program provides feedback after each guess, indicating whether the guess was too high or too low, and continues to prompt the user until they correctly guess the number. The game also keeps track of the number of attempts the user takes to guess the correct number.

## Features

- Random number generation between 1 and 100.
- User input and feedback loop.
- Feedback on whether the guess is too high or too low.
- Tracks the number of attempts made by the user.
- Congratulates the user when they guess correctly.

## How It Works

1. **Random Number Generation**:
   - The program generates a random number between 1 and 100 using Python's `random.randint` function.

2. **User Input**:
   - The user is prompted to guess the number by entering a value between 1 and 100.

3. **Feedback**:
   - After each guess, the program provides feedback:
     - "Too low!" if the guess is lower than the secret number.
     - "Too high!" if the guess is higher than the secret number.

4. **Winning Condition**:
   - The game continues until the user correctly guesses the number.
   - Once the correct number is guessed, the program congratulates the user and displays the number of attempts it took to win the game.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Clone or download the script.
2. Run the script using a Python interpreter:

   ```bash
   python guessing_game.py
   ```

3. Follow the on-screen instructions to start guessing.

### Example

When you run the program, it will start like this:

```bash
Welcome to the Guessing Game!
I have selected a random number between 1 and 100.
```

You will then be prompted to enter your guess. After each guess, the program will tell you whether the guess is too high or too low, and you can keep guessing until you find the correct number.

### Winning the Game

When you guess the correct number, the program will display a message like this:

```bash
Congratulations! You've guessed the number 42 in 7 attempts.
```

## Error Handling

- The program expects the user to input an integer. If the input is not an integer, the program will raise a `ValueError`. You may consider adding input validation if you want to handle this scenario gracefully.

## Contributing

Feel free to fork this repository and submit pull requests. If you find any bugs or have suggestions for improvements, please create an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This README file explains the purpose of the game, how it works, and how users can run it. You can expand on this based on any additional features or instructions you might have.
