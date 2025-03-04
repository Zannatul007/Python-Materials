import pytz
import datetime
class Account(object):
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance 
        self.transaction_list = []
    def deposite(self,amount):
        self.balance+=amount
        self.show_amount()
        self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow())),amount)
    def withdraw(self,amount):
        if(0<amount<=self.balance):
            self.balance-= amount
            self.show_amount()
        else:
            print("It's not sufficient amount of money to withdraw deposite more")
    def show_amount(self):
        print(f"Account has now {self.balance}")
    def show_transactions(self):
        tran_type
        for date,amount in self.transaction_list():
            if amount>0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"

            print("In this {:.6f} ")

if __name__ == '__main__':
    zane = Account("Zane",5000)
    zane.show_amount()
    zane.deposite(1000)
    zane.withdraw(400)
 
