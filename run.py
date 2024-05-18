import random

print ("welcome to Hangman")
print ("--------------------------------------------")

wordDictionary +["graze""tooth""paper""warning""presentation""nuclear""parking""performance""surgeon""trust""denial"
"bathroom""campaign""equation""swipe""discourage""wine""image""snail""management""tray""trail""studio""south"]

### choose a random word 
randomWord = random.choice(wordDictionary)


for x in randomWord:
    print ("_", end=" ")

def print_hangman(wrong):
    if (wrong == 0):
        print ("/n+---+")
        print ("    |")
        print ("    |")
        print ("    |")
        print ("   ===")
      elif(wrong == 1):
        print ("/n+---+")
        print ("O   |")
        print ("    |")
        print ("    |")
        print ("   ===")
      elif(wrong == 2):
        print ("/n+---+")
        print ("O   |")
        print ("|   |")
        print ("    |")
        print ("   ===")
      elif(wrong == 3):
        print ("/n+---+")
        print (" O   |")
        print ("/|   |")
        print ("     |")
        print ("   ===")
     elif(wrong == 4):
        print ("/n+---+")
        print (" O   |")
        print ("/|\  |")
        print ("     |")
        print ("   ===")
        elif(wrong == 5):
            print ("/n+---+")
        print (" O   |")
        print ("/|\  |")
        print (" |   |")
        print ("   ===")
     elif(wrong == 6):
        print ("/n+---+")
        print (" O   |")
        print ("/|\  |")
        print ("/    |")
        print ("   ===")
     elif (wrong ==7):
        print ("/n+---+")
        print (" O    |")
        print ("/|\   |")
        print ("/ \   |")
        print ("   ===")
      
   def printWord("guessedLetters"):
      counter=0
      rightLetters=0
      for char in randomWord:
         if (char in guessedLetters):
            print(randomWord[counter], end=" ")
            rightLetters+=1
         else:
           print(" ", end=" ")
         counter +=1
      return rightLetters

   def printLines():
     print("\r")
     for char in randomWord
      print("\u203E", end=" ")

   lenght_of_of_word_to_guess = len(randomWord)
   amount_of_times_wrong = 0
   current_guess_index = 0



      
         
        



   
    

