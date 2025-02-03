string_1 = "we win"

for i in string_1:
    print(i)

str2 = "   Zannatul Fardaush"
print(str2[:])
print(str2[0:3])


print(str2.upper())
print(str2.lower())
print(str2.replace("a","aa"))
print(str2.strip())
print(str2.split(" "))

##F-string 
##A placeholder {} can contain variables, operations, functions, and modifiers to format the value
age = 26
internship = "3 months"
a,b = 3,6.5667
mul = a*b

print(f"{str2} is {age} years old but now she is just in a {internship} internship")
print(f"The sum of a=12 b=3 is {12+3}")
print(f"The multiplication = {mul:.2f}")


#negative slicing

str3 = "Newroz Technology"
print(str3[::-1])
print(str3[-1:-9:-1])