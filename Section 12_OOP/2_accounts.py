import datetime
import pytz


class Account():
    def __init__(self,name,balance):
        self.__name = name 
        self.__balance = balance
        self.__transactions_list = [[Account.current_time(),balance]]

        self.show_balance()
    @staticmethod
    def current_time():
        time = datetime.datetime.utcnow()
        return pytz.utc.localize(time)

    def deposite(self,amount):
        if(amount>0):
            self.__balance +=amount
        self.__transactions_list.append([Account.current_time(),amount])
        # self.show_balance()
    def withdraw(self,amount):
        if(0<amount<=self.__balance):
            self.__balance-=amount
        self.__transactions_list.append([Account.current_time(),-amount])
        # self.show_balance()
    def show_balance(self):
        print('The account has {}'.format(self.__balance))
    def manage_transactions(self):
        for date, value in self.__transactions_list:
            if(value >0):
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                value *=-1
            print("{:6} {} on {} (local time was {})".format(value, tran_type, date, date.astimezone()))

        
        
if __name__ =='__main__':
    zane = Account('zane',800)
    # zane.show_balance()
    zane.deposite(200)
    zane.withdraw(100)
    zane.deposite(300)

    zane.manage_transactions()
    zane.show_balance()


    tim = Account('Tim',0)
    tim.balance = 200
    tim.deposite(300)
    tim.withdraw(100)
    tim.deposite(500)
    tim.manage_transactions()
    tim.show_balance()
    print(tim.__dict__)

