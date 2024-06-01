# Hangman

Hangman is a game usually played by two or more people, where one person thinks of a word while the others guess what the word is by guessing one letter at a time until the whole word is revealed.
For this project I wanted to create a version of this game that you can play against the computer rather than playing against another person.
This is done by using python to generate the word and check if the user's guesses are correct, incorrect, invalid or if the user has already guessed the letter.

<img src ="images/responsive screenshot.png" alt="image of app on different sized screens">
[Click here to go to the live website!](https://hangman-jb060-d0d13762f512.herokuapp.com/)

### Objectives

- I want to create a game that is easy to navigate. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - This was achieved by using a simple 1 for yes or 2 for no for each time the user needs to make a choice other than when they are choosing a letter as their guess.  
                        
 - I want the game to run in a smooth loop to allow the user to keep playing as many times as they'd like to. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - If a play either loses or wins the game it will ask them if they would like to play again 1 for yes and 2 for no. If the user decides they don't want to play anymore it will show a message saying GoodBye but also state that if they would like to carry on playing all they need to do is either refresh the page or click on the run program button above.

- To make it clear to the user how many tries they have left until the game is over.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - When the user gets a guess wrong the number of tries left is printed and each round if they get the answer right or wrong it will print out the traditional hangman image that shows how many tries the user has left in the game.

- I want to give the user a choice of how hard they would like to challenge themselves.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - To achieve this I created two lists, one with shorter words making them easier to guess and one with longer words making them a bit harder to guess. I then made a function called get_word, within this function I asked the user what level they would like to play at. If they chose easy it would generate a word from the easier list if they chose hard it would generate a word from the harder list. 
