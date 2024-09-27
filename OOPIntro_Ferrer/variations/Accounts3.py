"""
    Accounts3.py
"""

class Accounts():  # create the class
    def __init__(self, account_number, account_firstname, account_lastname, current_balance, address, email):
        self.account_number = account_number
        self.account_firstname = account_firstname
        self.account_lastname = account_lastname
        self.current_balance = current_balance
        self.address = address
        self.email = email

    def update_address(self, new_address):
        self.address = new_address

    def update_email(self, new_email):
        self.email = new_email

