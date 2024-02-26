
word = 'test'

def ask_for_input(): 
    while True: 
        user_guess = input('Guess a letter:')
        if len(user_guess) == 1 and user_guess.isalpha() == True:
            break
        else:  
            print("Please enter a single letter.") 
    check_user_guess(user_guess)

def check_user_guess(user_guess):
    user_guess = user_guess.lower()
    if user_guess in word: 
        print(f'Good guess! {user_guess} is in the word.')
    else: 
        print(f"Sorry, {user_guess} is not in the word. Try again.")

ask_for_input()