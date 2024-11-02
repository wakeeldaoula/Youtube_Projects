import random

def select_random_word():
    word_list = ['python', 'hangman', 'programming', 'developer', 'internship']
    return random.choice(word_list)

def show_hangman(remaining_attempts):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |
           |
        ''',
        '''
           ------
           |    |
           |    O
           |
           |
           |
        ''',
        '''
           ------
           |    |
           |
           |
           |
           |
        ''',
        '''
           ------
           |    |
           |
           |
           |
           |
        '''
    ]
    return stages[remaining_attempts]

def run_hangman_game():
    secret_word = select_random_word()
    unique_letters = set(secret_word)
    guessed_letters = set()
    max_attempts = 6

    print("Welcome to the Hangman Game!")
    
    while max_attempts > 0 and unique_letters != guessed_letters:
        print(show_hangman(max_attempts))
        print("Current word: ", " ".join([letter if letter in guessed_letters else '_' for letter in secret_word]))
        print("Your guesses: ", " ".join(guessed_letters))
        
        guess = input("Please enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in unique_letters:
            print("Nice job! That letter is in the word.")
        else:
            max_attempts -= 1
            print(f"Oops! That letter is not in the word. You have {max_attempts} attempts left.")
    
    if unique_letters == guessed_letters:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(show_hangman(max_attempts))
        print(f"Sorry, you've lost. The correct word was: {secret_word}")

if __name__ == "__main__":
    run_hangman_game()