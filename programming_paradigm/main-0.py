deposit:50
withdraw:20
withdraw:150
from bank_account import BankAccount
# Create a BankAccount instance with an initial balance of 100
account = BankAccount(100)
# Deposit 50 into the account
account.deposit(50)
# Withdraw 20 from the account
account.withdraw(20)
# Attempt to withdraw 150 from the account (should fail)
account.withdraw(150)
# Display the final balance
account.display_balance()