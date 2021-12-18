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
    

word = random.choice(word_list)

#Generate the box for visuals
box = ""
box_item = "□"
for n in word:
    box = box + " " + box_item
   
print ("Welcome to Hangman! Try to guess this word:")
print(box)

wrong = 0
remaining_attempts = 6
guess_storage = ""

#Play the game until 7 incorrect choices

while wrong < 7:
    guess = input("Which letter are you going to guess?\n").lower()
    indices = [
    index
    for index, element in enumerate(list(word))
    if element == guess
    ]
    
    if guess in guess_storage:
       print ("You cannot use the same letter again. Pick another letter")
       continue

    guess_storage += guess + ", " 
    
    if guess in word:
        if len(indices) == 1:
             box = replace(box, indices[0]*2 + 1, guess)
             print (box)
             print("Congratulations! You've managed to guess one of the letters")
             print(f"You've already used these letters: {guess_storage.capitalize()}") 

        if len(indices) > 1:     
           for i in indices:
               
              box = replace(box, i * 2 + 1, guess) 
              
           print(box)       
           print("Congratulations! You've managed to guess one of the letters")
           print(f"You've already used these letters: {guess_storage.capitalize()}") 
 
        if not (box_item) in box:
            print("Well done, you've won the game! To play again, press F5.") 
            sys.exit()
            
    else:
        if remaining_attempts > 0:
         wrong += 1
         remaining_attempts -= 1
         print(stages[remaining_attempts])

         if remaining_attempts > 1:
            print(f"Oh no, you guessed wrong. You've got: {remaining_attempts +1} remaining attempts")
            
         if remaining_attempts == 1:
            print("This is your last try!")
         print(f"You've already used these letters: {guess_storage.capitalize()}") 
         print(box)

        elif remaining_attempts == 0:
         print("GGWP, you lost")
         sys.exit()   
 
   
   




