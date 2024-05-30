import random


def print_rules():
    print("\nHangman Rules:")
    print("1. The game is divided into two parts:")
    print("2. The human guesses the computer's word, ")
    print("   and the computer guesses the human's word.")
    print("3. For each part, you will try to guess the word,")
    print("   one letter at a time.")
    print("4. Each correct guess will reveal the letter in the word.")
    print("5. Each incorrect guess will draw a part of the hangman figure.")
    print("6. You have a limited number of incorrect guesses (7).")
    print("7. The game ends when you either guess the word correctly")
    print("   or the hangman is fully drawn.")
    print("8. You can ask for a hint if you are stuck, but use them wisely!")

    print("   Good luck!\n")


def get_player_name():
    while True:
        player_name = input("Please enter your name: ").strip()
        if player_name:
            return player_name
        else:
            print("Name cannot be empty. Please enter your name.")


def get_yes_or_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def play_game():
    print("Welcome to Hangman")
    print("--------------------------------------------")

    player_name = get_player_name()

    # Ask if the user wants to see the rules
    see_rules = get_yes_or_no(
        f"Hi {player_name}, would you like to see the rules? (yes/no): "
    )
    if see_rules == "yes":
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
        "south": "One of the cardinal directions.",
    }

    def print_hangman(wrong):
        stages = [
            """
            +---+
                |
                |
                |
               ===
            """,
            """
            +---+
            O   |
                |
                |
               ===
            """,
            """
            +---+
            O   |
            |   |
                |
               ===
            """,
            """
            +---+
             O   |
            /|   |
                 |
               ===
            """,
            """
            +---+
             O   |
            /|\\  |
                 |
               ===
            """,
            """
            +---+
             O   |
            /|\\  |
             |   |
               ===
            """,
            """
            +---+
             O   |
            /|\\  |
            /    |
               ===
            """,
            """
            +---+
             O    |
            /|\\   |
            / \\   |
               ===
            """,
        ]
        print(stages[wrong])

    def printWord(word, guessedLetters):
        rightLetters = 0
        for char in word:
            if char in guessedLetters:
                print(char, end=" ")
                rightLetters += 1
            else:
                print("_", end=" ")
        print()
        return rightLetters

    def printLines(word):
        print("\n" + "\u203E " * len(word) + "\n")

    def letter_already_guessed(letter, guessedLetters):
        return letter in guessedLetters

    def computer_guess(guessedLetters):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        available_letters = [
            letter for letter in alphabet if letter not in guessedLetters
        ]
        return random.choice(available_letters)

    def display_selected_word(word):
        print("The word was:", word)

    def display_word_length(word):
        print(f"The word has {len(word)} letters.")

    def is_valid_guess(letter):
        return len(letter) == 1 and letter.isalpha()

    human_score = 0
    computer_score = 0
    rounds = 5

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number} of {rounds}")
        print(f"Score - {player_name}: {human_score}, Computer: {computer_score}")

        randomWord, hint = random.choice(list(wordDictionary.items()))

        humanWord = input("Enter a word for the computer to guess: ").strip().lower()
        humanHint = input("Enter a hint for the word: ").strip()

        display_word_length(humanWord)

        print(f"\nPart 1: {player_name} guesses the computer's word")

        human_wrong_guesses = 0
        human_letters_guessed = []
        human_correct_letters = 0

        length_of_computer_word = len(randomWord)

        while (
            human_wrong_guesses != 7
            and human_correct_letters != length_of_computer_word
        ):
            print("\nLetters guessed so far:")
            for letter in human_letters_guessed:
                print(letter, end=" ")
            print()

            letterGuessed = (
                input("Guess a letter, guess the word, or type 'hint' for a hint: ")
                .strip()
                .lower()
            )

            if letterGuessed == "hint":
                print(f"Hint: {hint}")
                continue

            if not is_valid_guess(letterGuessed):
                print("Invalid input. Please enter a single letter and no numbers.")
                continue

            if len(letterGuessed) > 1:
                if letterGuessed == randomWord:
                    human_correct_letters = length_of_computer_word
                    break
                else:
                    print("Incorrect word guess.")
                    human_wrong_guesses += 1
                    print_hangman(human_wrong_guesses)
                    continue

            if letter_already_guessed(letterGuessed, human_letters_guessed):
                print(
                    "You have already guessed that letter. Please guess a different letter."
                )
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
            human_score += 1
        else:
            print(f"Sorry {player_name}, you've not guessed the computer's word.")

        display_selected_word(randomWord)

        print("\nPart 2: Computer guesses the human's word")

        computer_wrong_guesses = 0
        computer_letters_guessed = []
        computer_correct_letters = 0

        length_of_human_word = len(humanWord)

        while (
            computer_wrong_guesses != 7
            and computer_correct_letters != length_of_human_word
        ):
            letterGuessed = computer_guess(computer_letters_guessed)
            print(f"\nComputer guessed: {letterGuessed}")

            if letter_already_guessed(letterGuessed, computer_letters_guessed):
                print(
                    "Computer guessed a letter that was already guessed. It loses its turn."
                )
            else:
                if letterGuessed in humanWord:
                    computer_letters_guessed.append(letterGuessed)
                    computer_correct_letters = printWord(
                        humanWord, computer_letters_guessed
                    )
                    printLines(humanWord)
                else:
                    computer_wrong_guesses += 1
                    computer_letters_guessed.append(letterGuessed)
                    print_hangman(computer_wrong_guesses)
                    computer_correct_letters = printWord(
                        humanWord, computer_letters_guessed
                    )
                    printLines(humanWord)

        if computer_correct_letters == length_of_human_word:
            print("The computer has guessed your word!")
            computer_score += 1
        else:
            print("The computer did not guess your word.")

        display_selected_word(humanWord)

    print(f"\nFinal Score - {player_name}: {human_score}, Computer: {computer_score}")
    if human_score > computer_score:
        print(f"Congratulations {player_name}, you win!")
    elif human_score < computer_score:
        print("The computer wins!")
    else:
        print("It's a tie!")

    play_again = get_yes_or_no(
        f"{player_name}, would you like to try again? (yes/no): "
    )
    if play_again == "yes":
        play_game()
    else:
        print(f"Thank you for playing, {player_name}! Goodbye!")


play_game()

