# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain number of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The programme takes an input from the user, checks if the input is present in the word, then informs the user if they were correct or not. Of course, if the guess is not in the letter then the user loses a life! 

In terms of the code, the programme has 2 main elements: a Hangman class, and a play_game function. It also uses the imported function 'random' to choose a random word from a word list and pprint for debugging purposes. 

The 'Hangman' class contains: 
- The attributes for the game. These are the word list (word_list), number of lives (num_lives), randomly chosen word from the list (word), number of letters left to guess (num_letters), and the guesses that the user has made (guess). 
- The 2 methods that enable the game to be played. The 2 methods are: 

1. ask_for_input - This takes the user input, checks the length of the input is equal to 1, and that it is alphabetical. If this is not the case it prompts the user to enter another letter. It then checks if the guess is already in the list of guesses, if so it informs the user that they have already guessed that letter. If not it runs the check_guess function to check if the guess is in the word. Finally appends the guess to the list of guesses that the user has made. 

2. check_user_guess - this converts the input to lower case, then checks whether the letter is in the word or not. If it is, it informs the user, and decreases the variable 'num_letters' so that the programme can keep track of the number of letters the user has left to guess. It then prints the number of letters left to guess. If the guess is not in the word, the programme informs the user via a print statement, decreases the number of lives the user has left, and informs the user how many lives they have left.

The play_game function 
This function takes an argument of the word list that the user would like to play with (as a string). It initialises the instance of the Hangman class and runs a while loop to control how the methods of the instance of the Hangman class are used. The while loop:
- Checks that the user has lives left to play the game by checking if the variable num_lives is 0 
- If the user has lives left, it runs the ask_for_input function to enable the user to make further guess
- It breaks out of the loop if the player either wins or loses

To play the game the user runs the play_game and passes in the word list they'd like to use to guess from. 

#Improvements

There are 2 future improvements I'd like to make to the game. Firstly making the word list something that is created automatically in order that the user doens't have to add them themselves. Secondly adding the classic visual representation of the hangman rather than just a print statement informing the user that they have so many guesses left. 
