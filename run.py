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
    word_dictionary = {
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

    def print_word(word, guessed_letters):
        right_letters = 0
        for char in word:
            if char in guessed_letters:
                print(char, end=" ")
                right_letters += 1
            else:
                print("_", end=" ")
        print()
        return right_letters

    def print_lines(word):
        print("\n" + "\u203E " * len(word) + "\n")

    def letter_already_guessed(letter, guessed_letters):
        return letter in guessed_letters

    def computer_guess(guessed_letters):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        available_letters = [
            letter for letter in alphabet if letter not in guessed_letters
        ]
        return random.choice(available_letters)

    def display_selected_word(word):
        print("The word was:", word)

    def display_word_length(word):
        print(f"The word has {len(word)} letters.")

    def is_valid_guess(letter):
        return len(letter) == 1 and letter.isalpha()

    def play_computer_guess(human_word):
        computer_wrong_guesses = 0
        computer_letters_guessed = []
        computer_correct_letters = 0

        length_of_human_word = len(human_word)

        while (
            computer_wrong_guesses != 7
            and computer_correct_letters != length_of_human_word
        ):
            print(f"\nTries left: {7 - computer_wrong_guesses}")
            letter_guessed = computer_guess(computer_letters_guessed)
            print(f"\nComputer guessed: {letter_guessed}")

            if letter_already_guessed(letter_guessed, computer_letters_guessed):
                print(
                    "Computer guessed a letter that was already guessed. It loses its turn."
                )
            else:
                if letter_guessed in human_word:
                    computer_letters_guessed.append(letter_guessed)
                    computer_correct_letters = print_word(
                        human_word, computer_letters_guessed
                    )
                    print_lines(human_word)
                else:
                    computer_wrong_guesses += 1
                    computer_letters_guessed.append(letter_guessed)
                    print_hangman(computer_wrong_guesses)
                    computer_correct_letters = print_word(
                        human_word, computer_letters_guessed
                    )
                    print_lines(human_word)

        if computer_correct_letters == length_of_human_word:
            print("The computer has guessed your word!")
            return True
        else:
            print("The computer did not guess your word.")
            return False

    human_score = 0
    computer_score = 0
    rounds = 5

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number} of {rounds}")
        print(f"Score - {player_name}: {human_score}, Computer: {computer_score}")

        random_word, hint = random.choice(list(word_dictionary.items()))

        human_word = input("Enter a word for the computer to guess: ").strip().lower()
        human_hint = input("Enter a hint for the word: ").strip()

        display_word_length(human_word)

        print(f"\nPart 1: {player_name} guesses the computer's word")

        human_wrong_guesses = 0
        human_letters_guessed = []
        human_correct_letters = 0

        length_of_computer_word = len(random_word)

        while (
            human_wrong_guesses != 7
            and human_correct_letters != length_of_computer_word
        ):
            print(f"\nTries left: {7 - human_wrong_guesses}")
            print("Letters guessed so far:")
            for letter in human_letters_guessed:
                print(letter, end=" ")
            print()

            letter_guessed = (
                input("Guess a letter, guess the word, or type 'hint' for a hint: ")
                .strip()
                .lower()
            )

            if letter_guessed == "hint":
                print(f"Hint: {hint}")
                continue

            if not is_valid_guess(letter_guessed):
                print("Invalid input. Please enter a single letter and no numbers.")
                continue

            if len(letter_guessed) > 1:
                if letter_guessed == random_word:
                    human_correct_letters = length_of_computer_word
                    break
                else:
                    print("Incorrect word guess.")
                    human_wrong_guesses += 1
                    print_hangman(human_wrong_guesses)
                    continue

            if letter_already_guessed(letter_guessed, human_letters_guessed):
                print(
                    "You have already guessed that letter. Please guess a different letter."
                )
                continue

            if letter_guessed in random_word:
                human_letters_guessed.append(letter_guessed)
                human_correct_letters = print_word(random_word, human_letters_guessed)
                print_lines(random_word)
            else:
                human_wrong_guesses += 1
                human_letters_guessed.append(letter_guessed)
                print_hangman(human_wrong_guesses)
                human_correct_letters = print_word(random_word, human_letters_guessed)
                print_lines(random_word)

        if human_correct_letters == length_of_computer_word:
            print(f"Congratulations {player_name}! You've guessed the computer's word!")
            human_score += 1
        else:
            print(f"Sorry {player_name}, you've not guessed the computer's word.")

        display_selected_word(random_word)

        # Ask if the player wants the computer to guess their word
        play_computer = get_yes_or_no("Would you like the computer to guess your word? (yes/no): ")
        if play_computer == "yes":
            print("\nPart 2: Computer guesses the human's word")
            if play_computer_guess(human_word):
                computer_score += 1

        display_selected_word(human_word)

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


