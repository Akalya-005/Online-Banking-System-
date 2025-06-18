class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Available Balance: ₹{self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("\n--- Transaction History ---")
            for t in self.transactions:
                print(t)

    def export_transactions(self):
        filename = f"transactions_{self.account_number}.txt"
        with open(filename, "w") as file:
            file.write(f"Transaction History for {self.account_holder}\n")
            file.write(f"Account Number: {self.account_number}\n\n")
            for t in self.transactions:
                file.write(f"{t}\n")
        print(f"Transaction history exported to '{filename}' successfully!")


def main():
    print("Welcome to the Online Banking System!")
    acc_num = input("Enter your account number: ")
    acc_holder = input("Enter account holder name: ")
    account = BankAccount(acc_num, acc_holder)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Export Transactions to File")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: ₹"))
            account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amt)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            account.show_transactions()
        elif choice == '5':
            account.export_transactions()
        elif choice == '6':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
