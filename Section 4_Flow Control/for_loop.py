str1 = """Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?"""
#itering over character by character
for i in str1:
    if(i.isupper()):
        print(i)

#iterating over range of values--> range(start,end,step) where endValue = end-1 

for i in range(1,10):
    print("The no {:2}'s squared is {:3} and cube is {:4}".format(i,i**2,i**3))

for i in range(0,100,7):
    print(i)


#Nested loop 

for i in range(1,10):
    for j in range(1,10):
        print("{0} * {1} = {2}".format(i,j,i*j))
        if(j==9):
            print("--"*43)

#For loop challenge

for i in range(0,100,7):
    if(i>0 and i%11 ==0):
        print("The wanted number is {}".format(i))
        break

for i in range(0,20):
    if(i>0 and (i%3==0 or i%5==0)):
        continue

    print("The numbers are {}".format(i))