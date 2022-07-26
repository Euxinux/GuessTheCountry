# GuessTheCountry - game app

This is a simple console game user - computer. Computer draw random country from text file (196 countries). User's task is guess the country letter by letter. User has constrained amount of lives which they themselves determinate. Created with Python 3.10

## How it works?
	1. Set the number of lives (min 1).
	2. Program displays the country as follows _ _ _ _ _ _ .
	3. Computer asks the user that they want to change a word for another one. If they want to agree (Y/y/YES/yes etc.) or want to refuse(N/n/NO/no etc), letter size doesn't matter.
	4. At this stage of the game start,the user gives the letter (A-Z) size letter doesn't matter too. 
	If a letter was given before the user doesn't lose their life - program displays communicate about that. 
	If they choose a properly letter, it shows in the correct place in the word.
	If choose wrong, lose one life (user can lose only one life, even then repeat wrong choice.
	5. Game takes as long as the user guesses the country or loses all lives.
	6. After a round user is asked if they want to play again? If no program is closed.
	
### Technology:
* Python 3.10

### Validation:
Ad. 1 User can give only positive integers at least 1. Every number below 1, strings, blank places, decimal number char and special  aren't accepted. Program displays errors, gives the user next chance and waits for correct input.
Ad. 3 Strings different than in "How it works" point 3 aren't accepted.
Ad. 4 Like in point 1, every input is validated, and only letters from the english alphabet are accepted. Letter size doesn't matter
Ad. 6 Look point Ad.3



### What possible to add?:
* Optional draw country from external API
* Countries divided by difficulty
* Game rank
* Cooperative game 1 vs 1 or equal.
* Other categories different than countries


# Dijkstra 07.2022