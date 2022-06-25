<h1>
  Wordle Game Solver <br>
  <img src="https://i.pcmag.com/imagery/articles/01O9cD990ECgKwgagoHBoTW-2.fit_lim.size_768x.png", width="150" height="100"/>
</h1>
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

# Logic
The words are imported and preprocessed using nltk library <br>
For each input of a word there are three possible scenarios.
* The letter is included in the word and is placed in correct place
* The letter is included in the word and is placed incorrectly
* The letter is not included in the word. 
* The game starts with the word STORY. <br>

With each iterations the code checks for the letter 

* letters which are placed correctly which will be included in the same position while suggesting next word <br>
* Letters which are not included will not be present in the next word <br>
* Letters which are included but not in the write place will be shuffled in the next suggestion <br>


