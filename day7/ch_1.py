import random
import words_hangman
import hangman_art
import sys, subprocess
# word_list = ["advark", "baboon", "camel"]
# improving functionality by adding lots of words

print(hangman_art.logo)
x= random.choice(words_hangman.word_list)
#Testing code
print("The solution is ", x)


leng = len(x)
display = []
lives = 6
end_of_game = False

#Create blanks
for _ in range(leng):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    subprocess.run("cls", shell=True)
    # subprocess.run(cls shell true is used to clear the screen after that step.)
    if guess in display:
        print(f"You have already guessed {guess}")
    #Check guessed letter
    for n in range(leng):
        letter = x[n]
        if letter == guess:
            display[n] = letter
            
        
#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."  
    if guess not in x:
        print(f"You guessed {guess}, that's not in the word. you lose a life! ")
        
        lives = lives -1
        if lives == 0:
            end_of_game = True
    
            print("YOU LOSE ")
            print("The solution is ", x)

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    

        

    if "_" not in display:
        end_of_game = True
        print("You win")


#TODO-3: - print the ASCII art from 'stages' 
# that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])





