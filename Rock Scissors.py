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

img = [rock, scissors, paper]

choice = input("Choose 0 for Rock, 1 for Scissors, 2 for Paper: ")

if choice not in ["0", "1", "2"]:
    print("Invalid input! Please choose 0, 1, or 2.")
else:
    player_choice = int(choice)
    computer_choice = random.randint(0, 2)

    print("You chose:")
    print(img[player_choice])

    print("Computer chose:")
    print(img[computer_choice])

    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 0 and computer_choice == 1) or \
         (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 0):
        print("You win!")
    else:
        print("You lose!")
