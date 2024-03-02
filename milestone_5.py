

import random 
from pprint import pprint

class Hangman: 
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list.split()) 
        self.word_guessed = []
        for letter in self.word: 
            self.word_guessed.append('_')
        self.num_letters = 0 
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        for letter in range(0, len(self.word)): 
            if guess == self.word[letter]:
                print(f"Good guess! {guess} is in the word.")
                self.word_guessed[letter] = guess  
                print(self.word_guessed)

        if guess not in self.word: 
                print(f"Sorry, {guess} is not in the word.")
                self.num_lives -= 1 
                print(f"You have {self.num_lives} lives left.") 
        self.num_letters -= 1 

    def ask_for_input(self): 
        while True: 
            guess = input('Guess a letter:')
            if guess.isalpha() == False:
                print("That's not a single letter, please enter a letter") 
            elif guess in self.list_of_guesses:
                print("You've already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


#hangman = Hangman(word_list = 'cat car', num_lives = 5)
#hangman = Hangman('car fish')
#pprint(vars(hangman))

#hangman.ask_for_input()


def play_game(word_list): 
    num_lives = 5
    game = Hangman 
    game = game(word_list, num_lives)
    while True: 
        if num_lives == 0: 
            print('You lost')
        if num_letters > 0: 
            ask_for_input()
        if num_lives != 0 and num_letters == 0:
            print('You have won the game!') 

play_game('car fish') 
