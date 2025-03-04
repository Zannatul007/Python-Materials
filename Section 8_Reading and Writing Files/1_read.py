#file path = D:\Python Materials\Reading and Writing Files\jabber.txt
# jabber = open("D:\Python Materials\Reading and Writing Files\jabber.txt",'r')
# for line in jabber:
#     print(line.strip())
#     print(line,end = "")

#using 'with'
# with open("D:\Python Materials\Reading and Writing Files\jabber.txt","r") as jabber:
#     for line in jabber:
#         print(line.rstrip())

#Read file by read,readline and readlines
#Readlines -> works on line

with open('.\Reading and Writing Files\jabber.txt') as jabber:
     
     lines = jabber.readlines()

for line in reversed(lines):
    print(line,end='')

# #Read -> works on string 
# with open("D:\Python Materials\Reading and Writing Files\jabber.txt","r") as jabber:
#     lines_with_read = jabber.read()
# for line in reversed(lines_with_read):
#     print(line,end='')
