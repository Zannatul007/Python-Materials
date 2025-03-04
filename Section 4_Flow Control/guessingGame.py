import random
highest = 10
answer = random.randint(1,highest)
print(answer)
guess = int(input("Guess the number between 1 to {}".format(highest)))
find = False
while(guess!=answer):
    if(guess<answer):
        guess = int(input("Please Select Higher Value :"))
    elif(guess>answer):
        guess = int(input("Please Select Lower Number :"))

print("Yess you find it")


