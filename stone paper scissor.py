import random

choices = ["stone","paper","scissor"]

computer_choice = random.choice(choices)

player_choice = input("enter your choice: ")

print("computer chooses",computer_choice)
print("you chooses",player_choice)

if computer_choice == player_choice:
    print("Its a tie!")

elif computer_choice == "stone":
    if player_choice == "paper":
       print("You win")
    else:
       print("computer wins")

elif computer_choice == "paper":
    if player_choice == "scissor":
        print("You win")
    else:
        print("computer wins")

elif computer_choice == "scissor":
    if player_choice == "stone":
        print("You win")
    else:
        print("computer wins")
    
else:
    print("invalid choice! try again")