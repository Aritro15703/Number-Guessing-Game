import random
from logo import logo

def diffi(difficulty):
   
   if difficulty=='e':
      print("You have 10 guesses\n")
   elif difficulty=='h':
      print("You have 7 guesses.\n")
   else:
      print("Enter a valid code.\n")


numbers=list(range(1,101))
comp_num=random.choice(numbers)

print(logo)
print("\n")
print("I'm thinking of a number between 1 and 100. ")
difficulty=input('Choose a difficulty. Press e for Easy, h for Hard: ').lower()
diffi(difficulty)
if difficulty=='e':
   guess=10
elif difficulty=='h':
   guess=7

gameover= False

while gameover is not True:
   user_num= int(input('Make a guess: '))

   if comp_num > user_num:
      print("Its lower than the number I'm thinking, try again.\n")
      guess-=1
      if guess==0:
         print("You lose! Out of guesses.")
         gameover=True
      else:
         print(f"You have {guess} guesses left")
   elif comp_num < user_num:
      print("Its higher than the number I'm thinking, try again.\n")
      guess-=1
      if guess==0:
         print("You lose! Out of guesses.")
         gameover=True
      else:
         print(f"You have {guess} guesses left")
   else:
      print("You got it! Congratulations.\n")
      print(f"You completed the game with {guess} guesses left. WOW!")   
      gameover=True
   







   


