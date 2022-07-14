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

#   Code begins here

play_game = False

user_name = input("Hello what is your name?\n").title()

start_game = input("Would you like to play the game. Yes or No: \n").title()

if start_game == "Yes":
    play_game = True
else:
    pass

while play_game:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

    # List of values holds the variables rock, paper and scissors.
    list_of_values = [rock, paper, scissors]

    computer_choice = random.choice(list_of_values)
    print(f"Computer chose: \n {computer_choice}")

    user_choice = list_of_values[user_choice]
    print(f"You chose: \n {user_choice}")

    if user_choice == rock:
        if computer_choice == paper:
            print("You lose")
        elif computer_choice == scissors:
            print("You win")
        elif computer_choice == rock:
            print(f"It's a draw {user_name}")

    if user_choice == paper:
        if computer_choice == rock:
            print("You win")
        if computer_choice == paper:
            print(f"Its a draw {user_name}")
        if computer_choice == scissors:
            print("You lose")

    if user_choice == scissors:
        if computer_choice == rock:
            print("You lose")
        if computer_choice == paper:
            print("You win")
        if computer_choice == scissors:
            print(f"Its a draw {user_name}")

    play_game = False
