import random

print("Welcome to Hangman")
print("--------------------------------------------")

# List of words for the game
wordDictionary = ["graze", "tooth", "paper", "warning", "presentation", "nuclear", "parking", "performance", "surgeon", "trust", "denial",
                  "bathroom", "campaign", "equation", "swipe", "discourage", "wine", "image", "snail", "management", "tray", "trail", "studio", "south"]

# Choose a random word from the dictionary
randomWord = random.choice(wordDictionary)

# Print initial underscores for the word to guess
for x in randomWord:
    print("_", end=" ")

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
            print(randomWord[counter], end=" ")
            rightLetters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightLetters

# Function to print lines underneath the word
def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")

# Length of the word to guess
length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

# Main game loop
while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed so far:")
    for letter in current_letters_guessed:
        print(letter, end =" ")
    
    # Prompt user for input
    letterGuessed = input("\nGuess a letter:")
    
    # Check if the guessed letter is correct
    if (randomWord[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_wrong)
        current_guess_index +=1
        current_letters_guessed .append(letterGuessed)
        current_letters_right =  (current_letters_guessed)
        printLines()
    else:
        amount_of_times_wrong +=1 
        current_letters_guessed .append(letterGuessed)
        print_hangman(amount_of_times_wrong)
        current_letters_right = printWord(current_letters_guessed)
        printLines()

# End of the game
print ("Game is over!")



   




      
         
        



   
    

