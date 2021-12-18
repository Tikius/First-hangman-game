import random
import sys
from hangman_words_list import word_list
from hangman_art import stages

# String replacement function
def replace(s, index, c): 
    chars = list(s)
    chars[index] = c
    res = "".join(chars)
    return res
    
#Returns all the indexes of a specific character
def indexes2(my_list, desired_element):
    for index, element in enumerate(my_list):
        if element == desired_element:
            yield index    

word = random.choice(word_list)

#Generate the box for visuals
box = ""
for n in word:
    box = box + " □"
   
print ("Welcome to Hangman! Try to guess this word:")
print(box)

wrong = 0
remaining_attempts = 6
guess_storage = ""

#Play the game until 7 incorrect choices

while wrong < 7:
    guess = input("Which letter are you going to guess?\n").lower()
    indeksai = list(indexes2(word, guess))
      
  
    if guess in word:
        if len(indeksai) == 1:
             box = replace(box, indeksai[0]*2 + 1, guess)
             print (box)
             print("Congratulations! You've managed to guess one of the letters")
             print(f"You've already used these letters: {guess_storage}") 

        if len(indeksai) > 1:     
           for i in indeksai:
               
              box = replace(box, i * 2 + 1, guess) 
              
           print(box)       
           print("Congratulations! You've managed to guess one of the letters")
           print(f"You've already used these letters: {guess_storage}") 
 
        if not (" □") in box:
            print("Well done, you've won the game! To play again, press F5.") 
            sys.exit()
            
    else:
        if remaining_attempts > 0:
         wrong+=1
         remaining_attempts-= 1
                
         print(stages[remaining_attempts])
         if remaining_attempts > 1:
            print(f"Oh no, you guessed wrong. You've got: {remaining_attempts +1} remaining attempts")
         elif remaining_attempts == 1:
            print("This is your last try!")
         print(f"You've already used these letters: {guess_storage}") 
         print(box)

        elif remaining_attempts == 0:
         print("GGWP, you lost")
         sys.exit()   
 
    if guess not in guess_storage.capitalize():
       guess_storage = guess_storage + guess.capitalize() + ", "
    else:
        print("You can't use this letter anymore!\n")  




