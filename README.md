# Hangman

Welcome to the Hangman Game! This project implements a classic Hangman game where both the human and the computer take turns guessing each other's words. 
The game is designed for interactive play and features a simple text-based interface.

<img src ="images/responsive screenshot.png" alt="image of app on different sized screens">
Click here to go to the live website!: https://hangman-jb060-d0d13762f512.herokuapp.com/

## Table of contents
- Plans and structure
- How to Play
- Rules
- Features
- Objectives
- Changes throughout the process
- Features
   - Welcome page
   - Rules
   - The player picks a word for the computer to guess
   - Hint (Computer)
   - 1st selection (Correct)
   - Part 1, Player's Turn
     - Hint (Player)
     - 1st selection (Correct)
     - Area for guessed letters
     - 2nd selection (incorrect)
     - Player Guesse's Word correctly
  - Part 2, Computers Turn
  - Game End       


### How to Play
1. Starting the Game: Run the script to start the game. You will be prompted to enter your name.
2. Viewing the Rules: You can choose to view the game rules at the start.
3. Game Rounds: The game consists of 5 rounds, and in each round, you will:
-Guess the Computer's Word: The computer selects a random word from its dictionary, and you attempt to guess it letter by letter.
-Computer Guesses Your Word: You provide a word for the computer to guess. The computer will attempt to guess your word letter by letter.

### Rules
1. You will guess the computer's word one letter at a time.
2. The computer will guess your word one letter at a time.
3. Each correct guess reveals the letter in the word.
4. Each incorrect guess draws a part of the hangman figure.
5. You have a maximum of 7 incorrect guesses per word.
6. You can ask for a hint if you are stuck.
7. The game ends when either the word is guessed correctly or the hangman is fully drawn.


### Objectives

- I want to create a game that is easy to navigate. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - This was achieved by using a simple  yes or no each time the user needs to make a choice other than when they are choosing a letter as their guess.  
                        
 - I want the game to run in a smooth loop to allow the user to keep playing as many times as they'd like to. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - The game was written as first to 5 and If a player either loses or wins the game, it will ask them if they would like to play again "YES" or "NO".
        - If the user decides they don't want to play anymore it will show a message saying GoodBye but also state that if they would like to carry on playing all they need to do is either refresh the page or click on the run program button above.

- To make it clear to the user how many tries they have left until the game is over.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - When the user gets a guess wrong the number of tries left is printed and each round if they get the answer right or wrong it will print out the traditional hangman image that shows how many tries the user has left in the game.

- I want to give the user and the computer a choice of words to choose for each other to guess.
   - Was this achieved?
      - Yes both the computer and the player can pick a random word and a hint to match the word in case the user feels the word is too hard for them to guess.

### Changes throughout the process 

Throughout the process of making this project, I decided to change a couple of things due to the time limit I had to make the game.
- originally I was going to go with the old-school way of both player and computer guessing the same word.
- I then went with player choice for the computer and vice versa, this also was the same with the "hints" in the game.

## Features
 - Interactive gameplay with clear prompts and responses.
 - Random word selection from a predefined dictionary.
 - The ability for the computer to guess user-provided words.
 - Hint functionality to assist in guessing.
 - ASCII art to display the hangman figure progressively.

   
### Welcome page
- This is the first page you see when the app loads. On this page, it gives you a welcome message "Welcome to hangman" and asks the player to input their name.
  The player must enter a name for the game to proceed.
<img src="/images/1.png" alt= "">

### Rules
- Here the player is asked whether or not they would like to see the rules of the game a simple "Yes" or No" is typed.
  - if the player types "yes" The game rules will be printed in the terminal.
  - if the player types "No" the game will proceed to the next stage without seeing the rules. 
  <img src="/images/2.png" alt= "">

### The player picks a word for the computer to guess.
- On this screen, the player has typed "yes" to observe the game rules and the next step is for the player to pick any word from
  the English dictionary for the computer to guess, after picking the word, it will show in the terminal how many letters the word contains. 
<img src="/images/3.png" alt= "">

### Hint (Computer)
- On this screen, the player will type in a hint for the word they have selected previously for the computer to guess.
  the word we picked was "Pink", so I would have given a hint of "Barbie's favorite color".
<img src="/images/4.png" alt= "">

### Part 1, Player's Turn 
- On this screen, The computer has chosen a word from the dictionary of words we have given the game, the word has also been loaded with a hint
  and the player can use this hint if necessary by typing in the word "Hint" where the prompt is in the terminal.
<img src="/images/5.png" alt= "">

### Hint (Player)
- The player has chosen to use his "hint" and the hint has been printed in the terminal as:(Found in your mouth for chewing).
<img src="/images/6.png" alt= "">

### 1st selection (Correct)
- As we can see on the screen we start off with "7" tries to guess the word the computer has chosen for us.
  on this selection, the player has chosen correctly the letter "T" and the letter has been printed in the word selected, and to the
  "letters guessed" area of the terminal and we get to keep all our tries.
<img src="/images/7.png" alt= "">

### Area for guessed letters 
<img src="/images/14.png" alt= "">

### 2nd selection (incorrect)
- The player has made an incorrect selection of the letter "A" and the 1st part of the hangman has been drawn to the terminal to show
  us that this is the situation, also the letter "A" has been printed to the "letters guessed" area of the terminal showing us that we have
  already guessed these letters as to ensure we don't guess again.
<img src="/images/8.png" alt= "">

### Player Guesse's Word correctly
- In the screen below the player has gone on and correctly solved the computer word and we get a"congratulations" message
  and it also displays what the word was that the computer has chosen for us to solve.
  It then proceeds to ask us whether would like the computer to solve the word we have selected for the computer!
<img src="/images/9.png" alt= "">

### Part 2, Computers Turn 
- In the image below we can see the computer has correctly guessed the last
  letter of the word "K" and this is printed to the terminal but as the computer proceeds on with its tries
  we can see that it has incorrectly guessed the rest of its tries.
<img src="/images/10.png" alt= "">

### Game End 
- As this is a best-to-5 game I've here is what the final screen looks like when either the player or computer wins.
  it states the final score,
  it states a congratulatory message and asks if you would like to try again.
  if the player enters "yes" then the process repeats itself, but if the player inputs no the player gets a message stating:
  "Thank you for playing, 'JASON!' Goodbye!" 
<img src="/images/13.png" alt= "">


### Code Structure
The main functions and their purposes are as follows:

 - print_rules(): Displays the game rules.
 - get_player_name(): Prompts the player to enter their name.
 - get_yes_or_no(prompt): Prompts the player for a 'yes' or 'no' response.
 - print_hangman(wrong): Displays the hangman figure based on the number of wrong guesses.
 - print_word(word, guessed_letters): Displays the word with guessed letters revealed.
 - print_lines(word): Prints a line of underscores for each letter in the word.
 - letter_already_guessed(letter, guessed_letters): Checks if a letter has already been guessed.
 - computer_guess(guessed_letters): Generates a guess for the computer.
 - display_selected_word(word): Displays the word after the game round.
 - display_word_length(word): Displays the length of the word to be guessed.
 - is_valid_guess(letter): Validates the player's letter guesses.
 - play_computer_guess(human_word): Manages the computer's guessing process.


## Testing

### Python
Python was tested using PEP8ci [PEP8ci validator] https://pep8ci.herokuapp.com/#

<img src="images/Errors after testing.png" alt= "errors shown from the validator">

## Deployment 
There were many steps to deploying this project to Heroku:

1. If I had installed any packages to Gitpod, I would need to add them to a list of requirements. 
- To do this I would have typed pip3 freeze > requirements.txt and hit enter, this would update the requirements.txt file.
- I'd need to commit and push this to Github.
- Heroku will use this list to install the dependencies into the application before the project is run.
- However, I didn't need to do this as I had no packages installed.
2. I went over to my Heroku dashboard and clicked on 'Create a new app'.
3. I chose a name for my app; every app must have a unique name so I couldn't call it Hangman as this was already taken so I went for hang-the-guy.
4. Select my region and click Create an app. 
5. I then went to the tab at the top of the page and clicked on settings. 
6. Some apps will include sensitive data in the gitpod workspace that isn't in the GitHub repository because it has been deliberately protected in the gitnore. file. I didn't have any sensitive data to protect but if I had done, I would have needed to create a config var to allow Heroku access to this data. 
 - To do this, I would have clicked reveal config vars.
 - Filled in the key for example: CREDS
 - Then copy and paste the contents of that 'CREDS' file into the value field and click add. 
7. I added the build packs needed by clicking on the build pack button.
 - Here I selected Python and pressed save changes.
 - Then repeated the same process but selected nodejs this time.
 - making sure it was done in that order with Python at the top and nodejs under.
8. I scrolled back up to the tab at the top and clicked deploy.
9. I selected GitHub as the deployment method and clicked connect to GitHub.
10. Once this is selected, I then searched for my GitHub repository name and connected to the correct repository.
11. Then I scrolled down, here there were two options.
 - The first option is to enable automatic deployment, which means that Heroku will rebuild the app every time I push a change to Git Hub.
 - The other option is to manually deploy, which is the choice I went for with this project.
12. When all the code is received from GitHub there is a view button that a links to the running app, I clicked this to make sure everything was running as expected.


### Manual Testing
 - Initial Setup: Verify that the game starts correctly and prompts the user for their name.
 - Rules Display: Check that the rules are displayed if the user opts to see them.
 - Word Guessing: Ensure the player can guess letters and receive feedback on correct or incorrect guesses.
 - Computer Guessing: Test the computer's ability to guess the user's word and handle repeated letters and invalid inputs.
 - Scoring: Confirm that scores are tracked correctly and displayed at the end of each round.
 - Hints: Validate that hints are provided correctly when requested.
 - Game Flow: Check the overall flow of the game, including transitions between rounds and the end-game scenario.

### Bugs Squashed
 - Fixed a bug where the computer guessed previously guessed letters.
 - Resolved issues with invalid input handling, ensuring only single alphabetic characters are accepted.
 - Corrected scoring logic to accurately reflect the results of each round.
 - Improved hint functionality to provide relevant hints without revealing too much information.


### Future Improvements
 - Enhance the computer's guessing algorithm to be more intelligent.
 - Add more words and hints to the dictionary for greater variety.
 - Implement a graphical user interface (GUI) for a more user-friendly experience.

### Conclusion
 - This Hangman game offers an engaging way to challenge yourself and the computer in a classic word-guessing game. 
   Enjoy playing and improving your vocabulary!

## Credits 
- [Lucid chart](https://www.lucidchart.com/pages/) - This was used to create the flow chart in the planning process for this project. 
- [code beautifier](https://codebeautify.org/python-formatter-beautifier) - made the code look beautiful (as described LOL).
- [PEP8ci validator](https://pep8ci.herokuapp.com/#)- was used to check the code was valid.
- Youtube - I watched many different YouTube videos on how to make a hangman using Python and learnt a lot from many people.
- Marcel - My mentor Marcel was extremely helpful as always helping me feel confident in what I have made.





  


  
