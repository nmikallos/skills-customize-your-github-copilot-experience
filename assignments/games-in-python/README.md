
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Practice core Python skills by building a playable Hangman game using strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description
Prepare the game by selecting a random secret word and creating the variables needed to track progress.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list.
- Initialize variables for guessed letters, incorrect guesses, and maximum allowed incorrect guesses.
- Display the word progress using underscores (for example: `_ _ _ _ _`).

### 🛠️ Build the Hangman Game Loop

#### Description
Implement the main gameplay loop where the player guesses letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Accept one letter guess from the user each turn.
- Update and display progress after each guess.
- Decrease remaining attempts only for incorrect guesses.
- End when the full word is guessed or attempts are exhausted.
- Display a clear win or lose message at the end of the game.
