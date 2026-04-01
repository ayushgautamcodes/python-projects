import random

choices = ["1","2","3","4","5","6","7","8","9","10"]

computer_choice = random.choice(choices)

print("Guess the any number between 1 to 10" \
"if your choice is correct you will win")
player_choice = input("enter your choice: ")

print("computer chooses",computer_choice)
print(" you chooses",player_choice)

if player_choice == computer_choice:
    print(" You won!")
elif player_choice != computer_choice:
    print(" You lost!")
else:
    print("invalid choice!")