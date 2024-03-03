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
                self.num_letters -= 1 

        if guess not in self.word: 
                print(f"Sorry, {guess} is not in the word.")
                self.num_lives -= 1 
                print(f"You have {self.num_lives} lives left.") 
       

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
hangman = Hangman('car fish')
pprint(vars(hangman))

hangman.ask_for_input()


"""

word_guessed = []
        for letter in word: 
            word_guessed.append('_')
        
"""

 #if guess in word: 
    #    print("Good guess! {guess} is in the word.")
    #    for letter in word: 
    #        if letter == guess: 
    #            word_guessed letter = letter



#num_lives = 5 
#word_guessed = ['_', '_', '_'] 
#word = 'cat' 
#list_of_guesses = []
#num_letters = 3 