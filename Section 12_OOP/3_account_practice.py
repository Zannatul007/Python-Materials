import datetime
import pytz

class Account:

    @staticmethod
    def current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transactions = [(Account.current_time(),self.balance)]
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            self.transactions.append((Account.current_time(),amount))
            self.show_deposite()
    def withdrawn(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            self.show_deposite()
            self.transactions.append((Account.current_time(),-amount))
    def show_deposite(self):
        print(f'The account has now {self.balance} dollar')
    def show_transactions(self):
        for date,amount in self.transactions:
            if(amount>0):
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    zane = Account('Zannatul',2000)
    zane.deposite(2000)
    zane.deposite(4000)
    zane.withdrawn(500)
    zane.show_transactions()


    
