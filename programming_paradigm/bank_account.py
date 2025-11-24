class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.account_balance += amount
    
    def withdraw(self, amount):
        """withdraw money if balance is sufficient."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Print the current account balance."""
        print(f"Current balance: ${self.account_balance}")