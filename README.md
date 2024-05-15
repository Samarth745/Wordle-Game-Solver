## Introduction
Wordle is a puzzle game published by The New York Times every day on their website [here](https://www.nytimes.com/games/wordle/index.html). The Wordle Game Solver project aims to develop a rule-based model to solve the daily Wordle puzzle game within 6 guesses.

![image](https://github.com/Samarth745/Wordle-Game-Solver/assets/102907431/a828f1c8-d355-4d9e-9dc6-03951fd862d6)

## Goal
The goal of this project is to develop a rule-based model that can accurately solve the daily Wordle puzzle game within 6 guesses.

## Skills Used
- Python

## Model
This model utilizes the NLTK library to import all English words and further filters them to 5-letter words. It is a rule-based model with multiple if-else logic to filter out the next suggested word based on the game's feedback.

## Features
- Automatically forms words with correct letters in correct places once detected.
- While suggesting a new word, ignores the letters once they are rejected by the game.
- Shuffles the letters which are present but at wrong places to increase the performance of the solution.

## Logic
The words are imported and preprocessed using the NLTK library. For each input of a word, there are three possible scenarios:
1. The letter is included in the word and is placed in the correct place.
2. The letter is included in the word but is placed incorrectly.
3. The letter is not included in the word.
4. Use as maximum number unque letters in the word suggested 

The game starts with the word "STORY". With each iteration, the code checks for the following:
- Letters that are placed correctly, which will be included in the same position while suggesting the next word.
- Letters that are not included will not be present in the next word.
- Letters that are included but not in the correct place will be shuffled in the next suggestion.

## Usage
To use the Wordle Game Solver, follow these steps:
1. Clone the repository to your local machine.
2. Install the necessary dependencies, especially NLTK.
3. Run the main script to start solving Wordle puzzles.

## Contributing
Contributions to the Wordle Game Solver project are welcome! If you have any

