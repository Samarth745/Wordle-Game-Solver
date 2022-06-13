# Wordle-Game-Solver
Wordle is a puzzle game which is published by The New York Times everyday on the website https://www.nytimes.com/games/wordle/index.html.<br />
**Goal** To devlop a rule based model to solve your daily wordle puzzle game in 6 guesses <br />
**Skills Used** - Python

# Model
This Model uses nltk library to import all the english words and further fliter them to 5 letter words  <br />
This Model is a rule based model with multiple if else logic to filter out next suggestion of word  <br />
Features :  <br />
* Automatically form words with correct letters in correct places once detected
* While suggesting a new word Ignores the letters once the letters are rejected
* Shuffle the letters which are present but at wrong places to increase the performance of the solution <br />

The function in the model takes input to check which letters have been correctly guessed by the game at every iteration. 
