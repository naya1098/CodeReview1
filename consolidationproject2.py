#  consolidation_project#2 

#word guessing game 

import random

def choose_word(): 
    # random words in word bank
    word_bank = ["dog", "cat", "fish", "hamster", "turtle"]
    return random.choice(word_bank)

def display_word(word, guessed_letters):
    #displays the word with the guessed letters
    display = ""
    for letter in word: 
        if letter in guessed_letters:
            display += letter + " "
        else: 
            display += "_ "
    return display.strip()

def play_game(): 
    word = choose_word()
    guessed_letters = []
    attempts = 0 
    word_guesses = 0
    
    current_player = 1 

    print("Welcome to the Word Guessing Game")
    print("Your job is to guess the secret word!")
    print("Player 1, you'll start first, Good luck!")
    
    while word_guesses < 3: 
        print("\nWord:", display_word(word, guessed_letters))
        guess = input(f"Player {current_player}, enter a letter or guess the whole word: ").lower()
    #switch player after each turn
        current_player = 1 if current_player == 2 else 2

        if len(guess) == 1: # Guess a letter
            if guess in guessed_letters:
                print("You've guessed that letter already!")
            else: 
                guessed_letters.append(guess)
                attempts += 1
                #count occurences of guessed letters
                count = word.count(guess)
                if count > 0:
                    print("Yes, the letter", guess, "appears", count, " time (s) in the word.")
                else: 
                    print("No, there are no instances of the letter", guess, "in the word.")

                #increment word guesses
                word_guesses += 1


                print("The word has", len(word), "letters.")

                if all(letter in guessed_letters for letter in word): 
                    print("You've guessed the word in", attempts, "attempts, Congratulations!")
                    break
        else: # Guessing the word
            word_guesses += 1 
            attempts += 1
            #counts correct letters
            correct_letters = sum( 1 for guessed, secret in zip(guess, word) if guessed == secret)
            if guess == word:
                print("You've guessed the word in", attempts, "attempts, Congratulations!")
                break
            else: 
                print("Unfortunately, that is not the word :( ")
                if word_guesses >= 3: 
                    print("Oh No! You used all your guesses. The word was", word)
                    break

if __name__ == "__main__":
    play_game()
