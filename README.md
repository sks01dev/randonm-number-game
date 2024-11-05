
# 🎲 Number Guessing Game 🎲

Welcome to the **Number Guessing Game**! A fun, simple game where you try to guess a randomly generated number within a limited number of attempts.

## 🎮 How to Play

1. **Goal**: Guess the random number between **1 and 10**.
2. **Hints**: The game provides feedback to guide your guesses:
   - If your guess is too **high**, it will say "**The number is lower**."
   - If your guess is too **low**, it will say "**The number is higher**."
3. **Attempts**: You only have **3 chances** to guess correctly. Use them wisely!

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Running the Game
1. Clone this repository or download the code file.
2. Open your terminal and navigate to the folder containing the script.
3. Run the game:
   ```bash
   python number_guessing_game.py
   ```

## 🛠️ Code Walkthrough

- The game initializes with `randint()` to pick a random number within the specified range.
- A `while` loop keeps the game running until you either guess correctly or exhaust your attempts.
- Error handling (`try-except`) ensures you enter a valid number each time.

## 🖥️ Example Gameplay

```plaintext
Guess the number in the range from 1 to 10. You only get 3 guesses!
Guess: 5
The number is higher.
Guess: 7
The number is lower.
Guess: 6
You guessed it!
```

## 🔥 Features

- **Hint System**: Assists players in refining their guesses.
- **Limited Attempts**: Adds challenge to the game.
- **Error Handling**: Ensures a smooth playing experience.

---

Enjoy this small yet thrilling game, and test your luck!
