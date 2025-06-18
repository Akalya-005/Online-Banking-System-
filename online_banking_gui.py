import tkinter as tk
from tkinter import messagebox
import datetime

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"{datetime.datetime.now()}: Deposited ₹{amount}")
            return f"₹{amount} deposited successfully."
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        else:
            self.balance -= amount
            self.transactions.append(f"{datetime.datetime.now()}: Withdrawn ₹{amount}")
            return f"₹{amount} withdrawn successfully."

    def check_balance(self):
        return f"Available Balance: ₹{self.balance}"

    def get_transactions(self):
        return "\n".join(self.transactions) if self.transactions else "No transactions yet."


# ---- GUI CODE ----

# Bank Account object will be created after form is filled
account = None

def create_account():
    global account
    acc_num = entry_acc_number.get()
    acc_holder = entry_acc_holder.get()
    if acc_num and acc_holder:
        account = BankAccount(acc_num, acc_holder)
        messagebox.showinfo("Success", "Account created successfully!")
    else:
        messagebox.showerror("Error", "Please enter account number and holder name.")

def deposit_money():
    if account:
        try:
            amt = float(entry_amount.get())
            msg = account.deposit(amt)
            messagebox.showinfo("Deposit", msg)
        except:
            messagebox.showerror("Error", "Enter a valid amount.")
    else:
        messagebox.showerror("Error", "Create an account first.")

def withdraw_money():
    if account:
        try:
            amt = float(entry_amount.get())
            msg = account.withdraw(amt)
            messagebox.showinfo("Withdraw", msg)
        except:
            messagebox.showerror("Error", "Enter a valid amount.")
    else:
        messagebox.showerror("Error", "Create an account first.")

def check_balance():
    if account:
        msg = account.check_balance()
        messagebox.showinfo("Balance", msg)
    else:
        messagebox.showerror("Error", "Create an account first.")

def view_transactions():
    if account:
        msg = account.get_transactions()
        messagebox.showinfo("Transactions", msg)
    else:
        messagebox.showerror("Error", "Create an account first.")

# ---- TKINTER LAYOUT ----

root = tk.Tk()
root.title("🏦 Online Banking System")
root.geometry("400x500")
root.config(padx=15, pady=15)

# Account Form
tk.Label(root, text="Account Number").pack()
entry_acc_number = tk.Entry(root)
entry_acc_number.pack()

tk.Label(root, text="Account Holder Name").pack()
entry_acc_holder = tk.Entry(root)
entry_acc_holder.pack()

tk.Button(root, text="Create Account", command=create_account, bg="#4CAF50", fg="white").pack(pady=10)

# Transaction Input
tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

# Buttons
tk.Button(root, text="Deposit", command=deposit_money, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(root, text="Withdraw", command=withdraw_money, bg="#f44336", fg="white").pack(pady=5)
tk.Button(root, text="Check Balance", command=check_balance, bg="#9C27B0", fg="white").pack(pady=5)
tk.Button(root, text="View Transactions", command=view_transactions, bg="#FF9800", fg="white").pack(pady=5)

root.mainloop()
