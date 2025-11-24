class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if balance is sufficient."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print("Current Balance:", self.__account_balance)
# Example usage:
if __name__ == "__main__":
    account = BankAccount(100)
    account.display_balance()  # Output: Current Balance: 100
    account.deposit(50)
    account.display_balance()  # Output: Current Balance: 150
    success = account.withdraw(20)
    print("Withdrawal successful:", success)  # Output: Withdrawal successful: True
    account.display_balance()  # Output: Current Balance: 130
    success = account.withdraw(150)
    print("Insufficient funds:", success)  # Output: Withdrawal successful: False
    account.display_balance()  # Output: Current Balance: 130