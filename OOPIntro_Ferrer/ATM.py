"""
    ATM.py
"""

class ATM(): # create the class
    serial_number = 0
    
    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        print("Deposit Complete")
        
    def withdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        print("Withdraw Complete")

    def check_currentbalance(self, account):
        print(account.current_balance)