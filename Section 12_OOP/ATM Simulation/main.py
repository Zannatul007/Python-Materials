from atm_simulation import *

zane = Account("Zane", 10000, "123")
authenticated = False
while True:
    pin = input("Please Enter a new pin :")
    if zane.authenticate(pin):
        authenticated = True
        break
    print("Incorrect PIN! Please try again.")
if authenticated == True:
    zane.check_balance()
    zane.deposite(500)
    zane.deposite(1000)
    zane.withdraw(500)
    zane.show_transaction_history()
