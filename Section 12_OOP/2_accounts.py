import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.balance = balance
        self.transaction_list = [(Account.current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account.current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account.current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()
    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(2000)
    tim.show_transactions()

    # steph = Account("Steph", 800)
    # steph.balance = 200
    # steph.deposit(100)
    # steph.withdraw(200)
    # steph.show_transactions()
    # steph.show_balance()
    # print(steph.__dict__)
    # steph._Accountbalance = 40
    # steph.show_balance()
