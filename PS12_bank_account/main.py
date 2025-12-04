# Create a BankAccount class with deposit, withdraw, and balance check.

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"Current balance: {self.balance}")


def main():
    owner = input("Enter account owner name: ")
    account = BankAccount(owner)
    actions = {"d": account.deposit, "w": account.withdraw, "b": lambda _: account.show_balance()}
    while True:
        choice = input("Choose action - (d)eposit, (w)ithdraw, (b)alance, (q)uit: ").lower()
        if choice == 'q':
            break
        if choice in {'d', 'w'}:
            amount = float(input("Enter amount: "))
            actions[choice](amount)
        elif choice == 'b':
            actions[choice](0)
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
