import random

print("Welcome to Hangman")
print("--------------------------------------------")

# List of words for the game
wordDictionary =  ["apple", "banana", "grape", "orange", "strawberry", "watermelon", "melon", "peach", "cherry", "blueberry",
         "raspberry", "pineapple", "apricot", "blackberry", "cantaloupe", "coconut", "cranberry", "dragonfruit",
         "fig", "grapefruit", "kiwi", "lemon", "lime", "mango", "nectarine", "papaya", "passionfruit", "pear",
         "persimmon", "plum", "pomegranate", "quince", "tangerine", "avocado", "tomato", "carrot", "broccoli",
         "spinach", "kale", "cabbage", "lettuce", "cauliflower", "radish", "turnip", "squash", "pumpkin", "zucchini",
         "cucumber", "eggplant", "pepper", "onion", "garlic", "potato", "sweetpotato", "yam", "beet", "artichoke",
         "asparagus", "celery", "corn", "peas", "greenbeans", "mushroom", "leek", "shallot", "scallion", "ginger",
         "fennel", "parsley", "cilantro", "dill", "rosemary", "thyme", "oregano", "basil", "sage", "mint",
         "lavender", "marjoram", "chives", "bayleaf", "tarragon", "savory", "coriander", "cardamom", "cinnamon",
         "clove", "nutmeg", "paprika", "saffron", "turmeric", "vanilla", "anise", "allspice", "peppercorn",
         "mustard", "sesame", "flax", "poppy", "chia", "quinoa", "barley", "oat", "rice", "wheat", "rye", "buckwheat",
         "millet", "sorghum", "cornmeal", "teff", "amaranth", "spelt", "durum", "farro", "freekeh", "bulgur",
         "kamut", "triticale", "fonio", "bread", "pasta", "noodle", "bagel", "biscuit", "croissant", "donut",
         "muffin", "pretzel", "sandwich", "tortilla", "wrap", "pancake", "waffle", "cracker", "cookie", "pie",
         "cake", "brownie", "cupcake", "scone", "soda", "juice", "tea", "coffee", "smoothie", "milkshake",
         "lemonade", "beer", "wine", "cocktail", "vodka", "whiskey", "rum", "gin", "brandy", "champagne",
         "cider", "liqueur", "mead", "sake", "tequila", "bacon", "sausage", "steak", "chicken", "turkey",
         "duck", "beef", "pork", "lamb", "ham", "venison", "salmon", "tuna", "trout", "halibut", "cod",
         "shrimp", "lobster", "crab", "oyster", "clam", "scallop", "mussel", "octopus", "squid", "cuttlefish",
         "anchovy", "sardine", "herring", "mackerel", "milk", "cheese", "butter", "yogurt", "cream", "icecream",
         "sorbet", "gelato", "custard", "pudding", "buttermilk", "kefir", "paneer", "ricotta", "mozzarella",
         "cheddar", "gouda", "brie", "camembert", "roquefort", "gorgonzola", "parmesan", "bluecheese", "feta"]


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

# Function to check if the letter has been guessed before
def letter_already_guessed(letter, guessedLetters):
    return letter in guessedLetters

# Function to display the randomly selected word at the end of the game
def display_selected_word():
    print("The word was:", randomWord)

# Main game loop
while(amount_of_times_wrong != 7 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed so far:")
    for letter in current_letters_guessed:
        print(letter, end =" ")
    
    # Prompt user for input
    letterGuessed = input("\nGuess a letter:")
    
    # Check if the guessed letter has already been guessed
    if letter_already_guessed(letterGuessed, current_letters_guessed):
        print("You have already guessed that letter. Please guess a different letter.")
        continue
    
    # Check if the guessed letter is correct
    if (randomWord[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_wrong)
        current_guess_index +=1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    else:
        amount_of_times_wrong += 1
        current_letters_guessed.append(letterGuessed)
        print_hangman(amount_of_times_wrong)
        current_letters_right = printWord(current_letters_guessed)
        printLines()

# Display the selected word at the end of the game
display_selected_word()

# End of the game
print("Game is over!")



   




      
         
        



   
    

