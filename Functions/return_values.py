import random

def get_integer(prompt):

    """    Get an integer from the Standard Input (stdin).

    The function will continue looping, and prompting the user ,
    untill a valid `int` is entered \n
    `Args`: prompt : The string that the user will see,when they're prompted to enter the value.\n
    `Returns`:
        The integer that the user enters
    """

    while True:
        input1 = input(prompt)
        if(input1.isnumeric()):
            return int(input1)
highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))
 
while guess != answer:
    guess = get_integer(": ")
 
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
