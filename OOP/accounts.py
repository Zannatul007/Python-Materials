class Account(object):
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance 
    def deposite(self,amount):
        self.balance+=amount
        self.show_amount()
    def withdraw(self,amount):
        if(0<amount<=self.balance):
            self.balance-= amount
            self.show_amount()
        else:
            print("It's not sufficient amount of money to withdraw deposite more")
    def show_amount(self):
        print(f"Account has now {self.balance}")

if __name__ == '__main__':
    zane = Account("Zane",5000)
    zane.show_amount()
    zane.deposite(1000)
    zane.withdraw(400)
 
