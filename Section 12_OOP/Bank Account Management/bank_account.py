class BankTransferException(Exception):
    pass


class BankAccount(object):
    def __init__(self, name, balance):
        self.account_holder = name
        self.balance = balance
        print("The Account of `{}` created \nBalance = ${}".format(name, balance))

    def get_balance(self):
        print(
            "The Account of `{}` has \nBalance = ${}".format(
                self.account_holder, self.balance
            )
        )

    def deposite(self, amount):
        self.balance += amount
        print("${} has been deposited".format(amount))
        self.get_balance()

    def viable_transaction(self, amount):
        if amount >= self.balance:
            raise BankTransferException(
                f"\nSorry, account '{self.account_holder}' only has a balance of ${self.balance:.2f}"
            )
        else:
            return

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("Withdrawn Successful")
            self.get_balance()
        except BankTransferException as error:
            print("Withdawn is interrupted {}".format(error))

    def transfer(self, amount, account):
        print("**********\n \nTransfer is beginning ✈️")
        try:
            self.withdraw(amount)
            account.deposite(amount)
            print("\nTransfer complete! ✅\n\n**********")
        except BankTransferException as error:
            print("Transfer is interrupted {}".format(error))

    
