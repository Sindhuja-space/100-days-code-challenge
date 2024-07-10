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
game_images = [rock, paper, scissors]
game_result = ["Rock", "Paper", "Scissors"]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n"))

if user_choice < 0 or user_choice >= 3:
    print("Invalid number. You lose")
else:
    print(f"You chose: {game_result[user_choice]}")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)

    print(f"Computer chooses: {game_result[computer_choice]} ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw")