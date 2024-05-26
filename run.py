import random

def print_rules():
    print("\nHangman Rules:")
    print("1. The game is divided into two parts: the human guesses the computer's word, and the computer guesses the human's word.")
    print("2. For each part, you will try to guess the word one letter at a time or guess the entire word.")
    print("3. Each correct guess will reveal the letter in the word.")
    print("4. Each incorrect guess will draw a part of the hangman figure.")
    print("5. You have a limited number of incorrect guesses (7).")
    print("6. The game ends when you either guess the word correctly or the hangman is fully drawn.")
    print("7. You can ask for a hint if you are stuck, but use them wisely!")
    print("Good luck!\n")

def play_game():
    print("Welcome to Hangman")
    print("--------------------------------------------")

    player_name = input("Please enter your name: ").strip()

    # Ask if the user wants to see the rules
    see_rules = input(f"Hi {player_name}, would you like to see the rules? (yes/no): ").strip().lower()
    if see_rules == 'yes':
        print_rules()

    # Dictionary of words and their hints for the game
    wordDictionary = {
        "graze": "What cows do in a field.",
        "tooth": "Found in your mouth, used for chewing.",
        "paper": "You write on it.",
        "warning": "A cautionary notice.",
        "presentation": "A display or demonstration of information.",
        "nuclear": "Related to atomic energy.",
        "parking": "Finding a space for your car.",
        "performance": "How well someone does something.",
        "surgeon": "A doctor who performs operations.",
        "trust": "Reliance on someone or something.",
        "denial": "Refusing to accept reality.",
        "bathroom": "A room for bathing.",
        "campaign": "A series of actions to achieve a goal.",
        "equation": "A mathematical statement.",
        "swipe": "A swift movement or to steal.",
        "discourage": "To make someone less confident.",
        "wine": "An alcoholic drink made from grapes.",
        "image": "A visual representation.",
        "snail": "A slow-moving mollusk.",
        "management": "The process of dealing with people or things.",
        "tray": "A flat container for carrying items.",
        "trail": "A path or track.",
        "studio": "A place for recording or creating art.",
        "south": "One of the cardinal directions."
    }

    # Choose a random word from the dictionary for the human to guess
    randomWord, hint = random.choice(list(wordDictionary.items()))

    # Ask the human player to select a word and a hint for the computer to guess
    humanWord = input("Enter a word for the computer to guess: ").strip().lower()
    humanHint = input("Enter a hint for the word: ").strip()

    # Function to print the hangman figure based on the number of wrong guesses
    def print_hangman(wrong):
        if wrong == 0:
            print("\n+---+")
            print("    |")
            print("    |")
            print("    |")
            print("   ===")
        elif wrong == 1:
            print("\n+---+")
            print("O   |")
            print("    |")
            print("    |")
            print("   ===")
        elif wrong == 2:
            print("\n+---+")
            print("O   |")
            print("|   |")
            print("    |")
            print("   ===")
        elif wrong == 3:
            print("\n+---+")
            print(" O   |")
            print("/|   |")
            print("     |")
            print("   ===")
        elif wrong == 4:
            print("\n+---+")
            print(" O   |")
            print("/|\  |")
            print("     |")
            print("   ===")
        elif wrong == 5:
            print("\n+---+")
            print(" O   |")
            print("/|\  |")
            print(" |   |")
            print("   ===")
        elif wrong == 6:
            print("\n+---+")
            print(" O   |")
            print("/|\  |")
            print("/    |")
            print("   ===")
        elif wrong == 7:
            print("\n+---+")
            print(" O    |")
            print("/|\   |")
            print("/ \   |")
            print("   ===")

    # Function to print the word with correct guesses filled in
    def printWord(word, guessedLetters):
        rightLetters = 0
        for char in word:
            if char in guessedLetters:
                print(char, end=" ")
                rightLetters += 1
            else:
                print("_", end=" ")
        return rightLetters

    # Function to print lines underneath the word
    def printLines(word):
        print("\n")
        for char in word:
            print("\u203E", end=" ")
        print("\n")

    # Function to check if the letter has been guessed before
    def letter_already_guessed(letter, guessedLetters):
        return letter in guessedLetters

    # Function for the computer to guess a letter
    def computer_guess(guessedLetters):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        available_letters = [letter for letter in alphabet if letter not in guessedLetters]
        return random.choice(available_letters)

    # Function to display the selected word at the end of the game
    def display_selected_word(word):
        print("The word was:", word)

    # Human guesses computer's word
    print(f"\nPart 1: {player_name} guesses the computer's word")

    human_wrong_guesses = 0
    human_letters_guessed = []
    human_correct_letters = 0

    length_of_computer_word = len(randomWord)

    while human_wrong_guesses != 7 and human_correct_letters != length_of_computer_word:
        print("\nLetters guessed so far:")
        for letter in human_letters_guessed:
            print(letter, end=" ")

        letterGuessed = input("\nGuess a letter, guess the word, or type 'hint' for a hint: ").strip().lower()

        if letterGuessed == 'hint':
            print(f"Hint: {hint}")
            continue

        if len(letterGuessed) > 1:
            # If the player is guessing the whole word
            if letterGuessed == randomWord:
                human_correct_letters = length_of_computer_word
                break
            else:
                print("Incorrect word guess.")
                human_wrong_guesses += 1
                print_hangman(human_wrong_guesses)
                continue

        if letter_already_guessed(letterGuessed, human_letters_guessed):
            print("You have already guessed that letter. Please guess a different letter.")
            continue

        if letterGuessed in randomWord:
            human_letters_guessed.append(letterGuessed)
            human_correct_letters = printWord(randomWord, human_letters_guessed)
            printLines(randomWord)
        else:
            human_wrong_guesses += 1
            human_letters_guessed.append(letterGuessed)
            print_hangman(human_wrong_guesses)
            human_correct_letters = printWord(randomWord, human_letters_guessed)
            printLines(randomWord)

    if human_correct_letters == length_of_computer_word:
        print(f"Congratulations {player_name}! You've guessed the computer's word!")
    else:
        print(f"Sorry {player_name}, you've not guessed the computer's word.")

    display_selected_word(randomWord)

    # Computer guesses human's word
    print("\nPart 2: Computer guesses the human's word")

    computer_wrong_guesses = 0
    computer_letters_guessed = []
    computer_correct_letters = 0

    length_of_human_word = len(humanWord)

    while computer_wrong_guesses != 7 and computer_correct_letters != length_of_human_word:
        letterGuessed = computer_guess(computer_letters_guessed)
        print(f"\nComputer guessed: {letterGuessed}")

        if letter_already_guessed(letterGuessed, computer_letters_guessed):
            print("Computer guessed a letter that was already guessed. It loses its turn.")
        else:
            if letterGuessed in humanWord:
                computer_letters_guessed.append(letterGuessed)
                computer_correct_letters = printWord(humanWord, computer_letters_guessed)
                printLines(humanWord)
            else:
                computer_wrong_guesses += 1
                computer_letters_guessed.append(letterGuessed)
                print_hangman(computer_wrong_guesses)
                computer_correct_letters = printWord(humanWord, computer_letters_guessed)
                printLines(humanWord)

    if computer_correct_letters == length_of_human_word:
        print("The computer has guessed your word!")
    else:
        print("The computer did not guess your word.")

    display_selected_word(humanWord)

    # Ask if the user wants to play again
    play_again = input(f"{player_name}, would you like to try again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print(f"Thank you for playing, {player_name}! Goodbye!")

# Start the game
play_game()
