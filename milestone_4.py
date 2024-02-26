import random 

class Hangman: 
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list) 
        self.word_guessed = []
        for letter in self.word: 
            self.word_guessed.append('_')
        self.num_letters = 0 
        self.list_of_guesses = []
    
def check_guess(guess):
    guess = guess.lower()
    if guess in word: 
        print("Good guess! {guess} is in the word.")
    else: 
        print()
    
def ask_for_input(): 
    while True: 
        guess = input('Guess a letter:')
        if guess.isalpha() == False:
            print("That's not a single letter, please enter a letter") 
        elif guess in list_of_guesses:
            print("You've already tried that letter!")
        else:
            check_guess(guess)
            list_of_guesses.append(guess)

word = 'cat' 
list_of_guesses = []
ask_for_input()







"""

word_guessed = []
        for letter in word: 
            word_guessed.append('_')
        
"""