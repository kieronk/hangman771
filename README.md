# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The programme takes an input from the user, checks if the input is present in the word, then informs the user of the answers. Of course, if it is not in the letter then the user also loses a life! 

In terms of the code, the programme has the class 'Hangman' which contains: 
- The attributes for the game
- 2 methods that enable the game to be played

The 2 methods are: 
1. ask_for_input() This takes the user input, checks the length of the input is equal to 1, and that it is alphabetical. If this is not the case it prompts the user to enter another letter.
2. check_user_guess() This converts the input to lower case, then checks whether it is in the word or not. It informs the user if the letter is in the word or not. 



    A description of the project: what it does, the aim of the project, and what you learned
    Installation instructions
    Usage instructions
    File structure of the project
    License information
