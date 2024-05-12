import random

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

game_image = [rock, paper, scissors]
user_choice = int(input("choose 0 for rock, 1 for paper, 2 for scissors. \n"))
print(game_image[user_choice])

computer_choice = random.randint(0, 2)
print(game_image[computer_choice])
if user_choice >= 3 or user_choice < 0:
  print("you typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2 : 
 print("youb win")
elif computer_choice == 1 and user_choice == 0 :
 print("you loose")
elif computer_choice == 0 and user_choice == 1 :
 print("you win")
elif computer_choice == 2 and user_choice == 1 :
 print("you loose")
elif computer_choice == 1 and user_choice == 2 :
 print("you win")
elif computer_choice == user_choice :
 print(" game draw")
  