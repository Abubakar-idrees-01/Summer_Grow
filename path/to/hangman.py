import random

def choose_word():
    """Chooses a random word from a list."""
    words = ["apple", "banana", "cherry", "date", "fig"]
    return random.choice(words)

def play_hangman():
    """Plays the Hangman game."""
    word = choose_word()
    word_length = len(word)
    guesses = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("I'm thinking of a word.")

    while attempts_left > 0 and "_" * word_length not in guesses:
        print("\nWord:", " ".join(["_" if letter not in guesses else word[guesses.index(letter)] for letter in word]))
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guesses:
            print("You already guessed that letter!")
            continue

        guesses.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts_left -= 1
            print("Incorrect!")

    if "_" * word_length not in guesses:
        print("\nI'm sorry, you ran out of attempts.")
        print("The word was:", word)
    else:
        print("\nCongratulations! You guessed the word:", word)


if __name__ == "__main__":
    play_hangman()
