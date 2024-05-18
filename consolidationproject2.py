import random

# Function to choose a random word from the word bank
def choose_word():
    """
    Chooses a random word from the word bank.
    """
    word_bank = ["dog", "cat", "fish", "hamster", "turtle"]
    return random.choice(word_bank)

# Function to display the word with guessed letters revealed and unrevealed letters shown as underscores
def display_word(word, guessed_letters):
    """
    Displays the word with the guessed letters. Unrevealed letters are shown as underscores.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Main function to play the word guessing game
def play_game():
    """
    Main function to play the word guessing game.
    """
    word = choose_word()  # Randomly select a word from the word bank
    guessed_letters = []  # List to store guessed letters
    attempts = 0  # Counter for attempts
    word_guesses = 0  # Counter for word guesses
    
    current_player = 1  # Starting player

    print("Welcome to the Word Guessing Game")
    print("Your job is to guess the secret word!")
    print("Player 1, you'll start first, Good luck!")
    
    while word_guesses < 3:  # Each player gets up to 3 word guesses
        print("\nWord:", display_word(word, guessed_letters))
        guess = input(f"Player {current_player}, enter a letter or guess the whole word: ").lower()
        
        # Switch player after each turn
        current_player = 1 if current_player == 2 else 2

        if len(guess) == 1:  # Guess a letter
            if guess in guessed_letters:
                print("You've guessed that letter already!")
            else:
                guessed_letters.append(guess)
                attempts += 1  # Increment attempts counter

                # Count occurrences of guessed letter in the word
                count = word.count(guess)
                if count > 0:
                    print("Yes, the letter", guess, "appears", count, "time(s) in the word.")
                else:
                    print("No, there are no instances of the letter", guess, "in the word.")

                print("The word has", len(word), "letters.")

                # Check if the word is fully guessed
                if all(letter in guessed_letters for letter in word):
                    print("You've guessed the word in", attempts, "attempts, Congratulations!")
                    break
        else:  # Guessing the whole word
            word_guesses += 1  # Increment word guesses counter
            attempts += 1  # Increment attempts counter
            
            # Count correct letters in the guessed word
            correct_letters = sum(1 for guessed, secret in zip(guess, word) if guessed == secret)
            if guess == word:
                print("You've guessed the word in", attempts, "attempts, Congratulations!")
                break
            else:
                print("Unfortunately, that is not the word :(")
                if word_guesses >= 3:  # Check if maximum word guesses reached
                    print("Oh No! You used all your guesses. The word was", word)
                    break

if __name__ == "__main__":
    play_game()

# Question: Should we limit the number of attempts for guessing letters as well, 
# or is it okay to let players keep guessing letters indefinitely as long as they don't guess the whole word?
