import random

def print_rules():
    print("\nHangman Rules:")
    print("1. The computer randomly selects a word from a predefined list.")
    print("2. You will try to guess the word one letter at a time.")
    print("3. Each correct guess will reveal the letter in the word.")
    print("4. Each incorrect guess will draw a part of the hangman figure.")
    print("5. You have a limited number of incorrect guesses (7).")
    print("6. The game ends when you either guess the word correctly or the hangman is fully drawn.")
    print("7. You can ask for a hint if you are stuck, but use them wisely!")
    print("Good luck!\n")

def play_game():
    print("Welcome to Hangman")
    print("--------------------------------------------")

    # Ask if the user wants to see the rules
    see_rules = input("Would you like to see the rules? (yes/no): ").strip().lower()
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

    # Choose a random word from the dictionary
    randomWord, hint = random.choice(list(wordDictionary.items()))

    # Print initial underscores for the word to guess
    for x in randomWord:
        print("_", end=" ")
    print("\n")

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
    def printWord(guessedLetters):
        counter = 0
        rightLetters = 0
        for char in randomWord:
            if char in guessedLetters:
                print(char, end=" ")
                rightLetters += 1
            else:
                print("_", end=" ")
            counter += 1
        return rightLetters

    # Function to print lines underneath the word
    def printLines():
        print("\n")
        for char in randomWord:
            print("\u203E", end=" ")
        print("\n")

    # Length of the word to guess
    length_of_word_to_guess = len(randomWord)
    amount_of_times_wrong = 0
    current_letters_guessed = []
    current_letters_right = 0

    # Function to check if the letter has been guessed before
    def letter_already_guessed(letter, guessedLetters):
        return letter in guessedLetters

    # Function to display the randomly selected word at the end of the game
    def display_selected_word():
        print("The word was:", randomWord)

    # Main game loop
    while amount_of_times_wrong != 7 and current_letters_right != length_of_word_to_guess:
        print("\nLetters guessed so far:")
        for letter in current_letters_guessed:
            print(letter, end=" ")

        # Prompt user for input
        letterGuessed = input("\nGuess a letter or type 'hint' for a hint: ").strip().lower()

        if letterGuessed == 'hint':
            print(f"Hint: {hint}")
            continue

        # Check if the guessed letter has already been guessed
        if letter_already_guessed(letterGuessed, current_letters_guessed):
            print("You have already guessed that letter. Please guess a different letter.")
            continue

        # Check if the guessed letter is correct
        if letterGuessed in randomWord:
            current_letters_guessed.append(letterGuessed)
            current_letters_right = printWord(current_letters_guessed)
            printLines()
        else:
            amount_of_times_wrong += 1
            current_letters_guessed.append(letterGuessed)
            print_hangman(amount_of_times_wrong)
            current_letters_right = printWord(current_letters_guessed)
            printLines()

    # End of the game
    if current_letters_right == length_of_word_to_guess:
        print("Congratulations! You've guessed the correct word!")
    else:
        print("Sorry, you've not guessed the correct word.")

    display_selected_word()

    # Ask if the user wants to play again
    play_again = input("Would you like to try again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thank you for playing! Goodbye!")

# Start the game
play_game()








   




      
         
        



   
    

