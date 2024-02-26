import random

fruit_list = ["apple", "blueberry", "strawberry", "raspberry", "pineapple"]

random_word = random.choice(fruit_list)

user_guess = input('Enter a single letter:')

if len(user_guess) == 1 and user_guess.isalpha() == True:
    print('Good guess!')
else:  
    print("Oops! That's not a valid input.") 

#print(word_list)
#print(word)

