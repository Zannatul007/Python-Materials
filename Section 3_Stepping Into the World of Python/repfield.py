age = 26
print("My age is {}".format(age))

print("There are {0} days in {1},{2},{3}".format(31,"Jan","Mar","Apr"))
days = 31
months = ['jan','mar','may']
print(f"There are {days} days in {months[0]},{months[1]},{months[2]}")

print("There are {0} days in Feb\t{2}days in jan,mar,may\t{1} days in april,nov".format(28,30,31))


#Formatting 

for i in range(1,12):
    print("No. {0}'s squared is {1} and cube is {2} ".format(i,i**2,i**3)) # alignment is not correct

for i in range(1,12):
    print("No. {0}'s squared is {1:3} and cube is {2:4} ".format(i,i**2,i**3))#now for square value 3 space occupied and for cube 4 space is occupied

for i in range(1,12):
    print("No. {0}'s squared is {1:<3} and cube is {2:<4} ".format(i,i**2,i**3))#now left aligned 
for i in range(1,12):
    print("No. {0}'s squared is {1:^3} and cube is {2:^4} ".format(i,i**2,i**3))#now centre aligned


print("Pi is {}".format(22/7))