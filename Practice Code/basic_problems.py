import math
def add(num1,num2):
    return num1+num2

def factorial(n):
    result = 1
    for i in range(1,int(n+1)):
        result*=i
    return result

def simple_interest(p: float,t: float,r: float)->float:
    output = (p*t*r)/100
    return output


# num1 = float(input())
# num2 = float (input())
# print("Sum of {} {} is {} ".format(num1,num2,add(num1,num2)))

# print("Maximum Number is {}".format(max(num1,num2)))

# print("Factorial of {} is {}".format(num1,factorial(num1)))

# p,t,r = input(),input(),input()
# p,t,r = float(p),int(t),int(r)

print("The simple interest is {} %".format(simple_interest(p,t,r)))