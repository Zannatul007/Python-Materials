from bank_account import *

zane = BankAccount("Zane", 2000)
kane = BankAccount("Kane", 20000)
zane.get_balance()
zane.deposite(1000)
zane.withdraw(1000000)
zane.transfer(200000, kane)
