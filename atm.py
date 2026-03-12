import json
import os

if os.path.exists("users.json"):
    with open("users.json","r") as file:
        user = json.load(file)
else:
    user = {}

def save_users():
    with open("users.json","w") as file:
        json.dump(user,file,indent=4)

while True:
    print("\n-------ATM SYSTEM-------")
    print("1 -> Login")
    print("2 -> New Registration")
    print("3 -> Exit")
    main_choice = int(input("Choose option (1/2/3): "))
    if main_choice == 1:
        card_no = (input("Enter the card no.: "))
        pin = (input("Enter the PIN: "))
    
        if card_no in user:
            if user[card_no]["pin"] == int(pin):
  
                while True:
                    print("-------ATM-------")
                    print(f"Welcome {user[card_no]['name']}")
                    print("1 ->Deposite Or Withdraw Money")
                    print("2 ->Check Balance")
                    print("3 ->Change PIN")
                    print("4 ->Transaction history")
                    print("5 ->exit")
                    choice = int(input("Type (1/2/3/4/5) for choosing the option: "))
                    if choice == 1:
                        print("1 -> Deposite: ")
                        print("2 -> Withdraw: ")
                        sub_choise = int(input("Type (1/2) for choosing the option: "))
                        if sub_choise == 1:
                            while True:
                                Deposite_amount = int(input("Enter the amount you want to Deposite: "))
                                if Deposite_amount < 0:
                                    print("Amount can not be entered in minus(-)")
                                else:
                                    user[card_no]["balance"] =  user[card_no]["balance"] + Deposite_amount
                                    user[card_no]["history"].append(f"Deposit: +${Deposite_amount}")
                                    save_users()
                                    print("Amount deposited.")
                                    break

                        elif sub_choise == 2:
                            while True:
                                Withdraw_amount = int(input("Enter the amount you want to Withdraw: "))
                                if Withdraw_amount > user[card_no]["balance"] :
                                    print("Insufficient Balance!")
                                else:
                                    user[card_no]["balance"] =  user[card_no]["balance"] - Withdraw_amount
                                    user[card_no]["history"].append(f"Withdraw: -${Withdraw_amount}")
                                    save_users()
                                    print("Amount Withdrawed.")
                                    break
                        else:
                            print("Invalid choice! Try again")

                    elif choice == 2:
                        print(f"Your account balance is ${user[card_no]['balance']}")
                 
                    elif choice == 3:
                        while True:
                            old_pin = int(input("Enter the current PIN: "))
                            if old_pin == user[card_no]['pin']:
                                renew_pin = int(input("Enter your new PIN: "))
                                new_pin = int(input("Confirm your new PIN: "))
                                if renew_pin == new_pin:
                                    user[card_no]['pin'] = new_pin
                                    print("PIN Updated")
                                    save_users()
                                    break
                                else:
                                    print("Confirm PIN does not matched Try again")
                            else:
                                print("Incorrect PIN")
                    elif choice == 4:
                        print("\n--- Transaction History ---")
                        if user[card_no]["history"]:
                            for transaction in user[card_no]["history"]:
                                print(transaction)
                        else:
                            print("No transaction yet!")
                    elif choice == 5:
                        print("Thank you for using the ATM ")
                        break
        else:
            print("invalid PIN or Card no.! Try again ")

    elif main_choice == 2:
        print("\n-------New user Registration-------")
        new_card = input("Enter the new Card Number: ")
        if new_card in user:
            print("Card Number already Exist! enter the new Card Number ")
        else:
            new_pin = input("Enter the new PIN: ")
            if not new_pin.isdigit():
                print("PIN must be in digit only!")
            else:
                name = input("Enter your Name: ")
                balance = int(input("You have to deposite the initial amount to create a acount: "))
            user[new_card] = {"pin": int(new_pin),"balance":balance,"name":name,"history":[f"Account created with ${balance}"]}
            save_users()
            print("New Registration is successful")
    elif main_choice == 3:
        print("thank you for using ATM")       
        break