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

print(choice[user_choice])

#computer choice
computer_choice = random.randint(0, 2)
print(choice[computer_choice])

#determine if user win

#if statement for draw
if user_choice == computer_choice:
  print("It's a draw")
else:
  #if statement for win, else == lose
  if user_choice == 0 and computer_choice == 2:
    print("You win, congrats, you beat Robots, Humanity will live !")
  elif user_choice == 1 and computer_choice == 0:
    print("You win, congrats, you beat Robots, Humanity will live !")
  elif user_choice == 2 and computer_choice == 1:
    print("You win, congrats, you beat Robots, Humanity will live !")
  else:
    print("You lose, Robots took over Humanity, no one haven't survive...")
  