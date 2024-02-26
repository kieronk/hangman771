import random

word_list = ["apple", "blueberry", "strawberry", "raspberry", "pineapple"]

word = random.choice(word_list)

guess = input('Enter a single letter:')

if len(guess) == 1 and guess.isalpha() == True:
    print('Good guess!')
else:  
    print("Oops! That's not a valid input.") 
 
#if len(guess) == 1 and guess.isalpha() == True:
#    print('Good guess!')
#else:  
#    "Oops! That's not a valid input."

print(word_list)

print(word)
