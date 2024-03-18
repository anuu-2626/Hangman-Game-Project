import random

def choose_word(theme):
    words = {
        'animals': ['elephant', 'tiger', 'lion', 'zebra', 'giraffe'],
        'countries': ['india', 'usa', 'canada', 'australia', 'japan'],
        'fruits': ['apple', 'banana', 'orange', 'grapes', 'kiwi']
    }
    return random.choice(words[theme])

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '-'
    return display

def check_guess(word, guessed_letter):
    return guessed_letter in word

def update_game_state(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def display_hangman(incorrect_guesses):
    hangman_parts = [
        '  ____\n |    |\n      |\n      |\n      |\n______|______',
        '  ____\n |    |\n O    |\n      |\n      |\n______|______',
        '  ____\n |    |\n O    |\n |    |\n      |\n______|______',
        '  ____\n |    |\n O    |\n/|    |\n      |\n______|______',
        '  ____\n |    |\n O    |\n/|\\   |\n      |\n______|______',
        '  ____\n |    |\n O    |\n/|\\   |\n/     |\n______|______',
        '  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n______|______'
    ]
    print(hangman_parts[incorrect_guesses])

def calculate_score(incorrect_guesses, word_length):
    # Score calculation based on the number of incorrect guesses
    # Adjust the formula as needed
    return (word_length - incorrect_guesses) * 10

def hangman():
    theme = 'animals'
    word = choose_word(theme)
    guessed_letters = []
    max_guesses = 6
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_guesses:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        guessed_letters.append(guess)
        if check_guess(word, guess):
            print("Correct!")
            print(display_word(word, guessed_letters))
            if update_game_state(word, guessed_letters):
                print("Congratulations! You've guessed the word correctly!")
                score = calculate_score(incorrect_guesses, len(word))
                print("Your score:", score)
                break
        else:
            print("Incorrect!")
            incorrect_guesses += 1
            display_hangman(incorrect_guesses)
            print(display_word(word, guessed_letters))

hangman()
