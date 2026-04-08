import tkinter as tk
from tkinter import messagebox
import json
import os

# ------------------ Load Data ------------------
if os.path.exists("users.json"):
    with open("users.json", "r") as file:
        users = json.load(file)
else:
    users = {}

def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# ------------------ Main Window ------------------
root = tk.Tk()
root.title("ATM System")
root.geometry("400x400")

current_user = None

# ------------------ Clear Frame ------------------
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# ------------------ Login Screen ------------------
def login_screen():
    clear()

    tk.Label(root, text="ATM Login", font=("Arial", 18)).pack(pady=10)

    tk.Label(root, text="Card Number").pack()
    card_entry = tk.Entry(root)
    card_entry.pack()

    tk.Label(root, text="PIN").pack()
    pin_entry = tk.Entry(root, show="*")
    pin_entry.pack()

    def login():
        global current_user
        card = card_entry.get()
        pin = pin_entry.get()

        if card in users and users[card]["pin"] == int(pin):
            current_user = card
            dashboard()
        else:
            messagebox.showerror("Error", "Invalid Card or PIN")

    tk.Button(root, text="Login", command=login).pack(pady=5)
    tk.Button(root, text="Register", command=register_screen).pack()

# ------------------ Register Screen ------------------
def register_screen():
    clear()

    tk.Label(root, text="New Registration", font=("Arial", 18)).pack(pady=10)

    card_entry = tk.Entry(root)
    card_entry.pack()
    card_entry.insert(0, "Card Number: ")

    pin_entry = tk.Entry(root)
    pin_entry.pack()
    pin_entry.insert(0, "PIN: ")

    name_entry = tk.Entry(root)
    name_entry.pack()
    name_entry.insert(0, "Name: ")

    balance_entry = tk.Entry(root)
    balance_entry.pack()
    balance_entry.insert(0, "Initial Deposit: ")

    def register():
        card = card_entry.get()
        pin = pin_entry.get()
        name = name_entry.get()
        balance = balance_entry.get()

        if card in users:
            messagebox.showerror("Error", "Card already exists")
            return

        if not pin.isdigit():
            messagebox.showerror("Error", "PIN must be digits")
            return

        users[card] = {
            "pin": int(pin),
            "name": name,
            "balance": int(balance),
            "history": [f"Account created with ${balance}"]
        }

        save_users()
        messagebox.showinfo("Success", "Account Created")
        login_screen()

    tk.Button(root, text="Register", command=register).pack(pady=10)
    tk.Button(root, text="Back", command=login_screen).pack()

# ------------------ Dashboard ------------------
def dashboard():
    clear()

    tk.Label(root, text=f"Welcome {users[current_user]['name']}", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Check Balance", command=check_balance).pack(pady=5)
    tk.Button(root, text="Deposit", command=deposit).pack(pady=5)
    tk.Button(root, text="Withdraw", command=withdraw).pack(pady=5)
    tk.Button(root, text="Change PIN", command=change_pin).pack(pady=5)
    tk.Button(root, text="History", command=show_history).pack(pady=5)
    tk.Button(root, text="Logout", command=login_screen).pack(pady=10)

# ------------------ Functions ------------------
def check_balance():
    messagebox.showinfo("Balance", f"Your balance is ${users[current_user]['balance']}")

def deposit():
    amount = tk.simpledialog.askinteger("Deposit", "Enter amount:")
    if amount and amount > 0:
        users[current_user]["balance"] += amount
        users[current_user]["history"].append(f"Deposit +${amount}")
        save_users()
        messagebox.showinfo("Success", "Amount Deposited")

def withdraw():
    amount = tk.simpledialog.askinteger("Withdraw", "Enter amount:")
    if amount and amount <= users[current_user]["balance"]:
        users[current_user]["balance"] -= amount
        users[current_user]["history"].append(f"Withdraw -${amount}")
        save_users()
        messagebox.showinfo("Success", "Amount Withdrawn")
    else:
        messagebox.showerror("Error", "Insufficient Balance")

def change_pin():
    new_pin = tk.simpledialog.askstring("Change PIN", "Enter new PIN:")
    if new_pin and new_pin.isdigit():
        users[current_user]["pin"] = int(new_pin)
        save_users()
        messagebox.showinfo("Success", "PIN Updated")

def show_history():
    history = "\n".join(users[current_user]["history"])
    messagebox.showinfo("Transaction History", history)

# ------------------ Start App ------------------
login_screen()
root.mainloop()