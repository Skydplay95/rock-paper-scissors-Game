rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#import module random
import random

#list of choice
choice = [rock, paper, scissors]

#user choice
#int input to be sure user enter a number not a number as string
user_choice = int(
    input(
        "What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)

#computer choice
computer_choice = random.randint(0, 2)

#determine if user win
#if user make a choice which is not in the range of options
if user_choice < 0 or user_choice >= 3:
  print("You have make a choice that didn't exist... Humanity lose")
else:
  
  #if statement for draw
  if user_choice == computer_choice:
    print(choice[user_choice])
    print(choice[computer_choice])
    print("It's a draw")
  else:
    #if statement for win, else == lose
    if user_choice == 0 and computer_choice == 2:
      print(choice[user_choice])
      print(choice[computer_choice])
      print("You win, congrats, you beat Robots, Humanity will live !")
      
    elif user_choice == 1 and computer_choice == 0:
      print(choice[user_choice])
      print(choice[computer_choice])
      print("You win, congrats, you beat Robots, Humanity will live !")
      
    elif user_choice == 2 and computer_choice == 1:
      print(choice[user_choice])
      print(choice[computer_choice])
      print("You win, congrats, you beat Robots, Humanity will live !")
    else:
      print(choice[user_choice])
      print(choice[computer_choice])
      print("You lose, Robots took over Humanity, no one haven't survive...")
    