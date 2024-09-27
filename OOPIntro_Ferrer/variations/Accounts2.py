"""
    Accounts2.py
"""

class Accounts2():  # create the class
    def __init__(self):
        self.account_number = 0
        self.account_firstname = ""
        self.account_lastname = ""
        self.current_balance = 0.0
        self.address = ""
        self.email = ""

    def update_address(self, new_address):
        self.address = new_address

    def update_email(self, new_email):
        self.email = new_email
