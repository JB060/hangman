# Hangman

Hangman is a game usually played by two or more people, where one person thinks of a word while the others guess what the word is by guessing one letter at a time until the whole word is revealed.
For this project I wanted to create a version of this game that you can play against the computer rather than playing against another person.
This is done by using python to generate the word and check if the user's guesses are correct, incorrect, invalid or if the user has already guessed the letter.

<img src ="images/responsive screenshot.png" alt="image of app on different sized screens">
Click here to go to the live website!: https://hangman-jb060-d0d13762f512.herokuapp.com/

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
        - The game was given a first to 5 and If a player either loses or wins the game, it will ask them if they would like to play again "YES" or "NO".
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

### Welcome page
- This is the first page you see when the app loads. On this page, there is a 
  welcome message and a question to the user. 
  The question asks the user if
  they want to see the instructions or if they are happy to go ahead and play without seeing them.
<img src="/images/1.png" alt= "">

### Rules
- Here the player is asked whether or not they would like to see the rules of the game a simple "Yes" or No" is typed.
  - if the player types "yes" The game rules will be printed in the terminal.
  - if the player types "No" the game will proceed to the next stage without seeing the rules. 
  <img src="/images/2.png" alt= "">

### Player picks a word for the computer to guess.
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
- the player has chosen to use his "hint" and the hint has been printed in the terminal as:(Found in your mouth for chewing.
<img src="/images/6.png" alt= "">
<img src="/images/7.png" alt= "">
<img src="/images/8.png" alt= "">
<img src="/images/9.png" alt= "">
<img src="/images/10.png" alt= "">
<img src="/images/11.png" alt= "">
<img src="/images/12.png" alt= "">
<img src="/images/13.png" alt= "">
<img src="/images/14.png" alt= "">
<img src="/images/15.png" alt= "">
<img src="/images/16.png" alt= "">



  


  
