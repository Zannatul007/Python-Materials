with open("D:\Python Materials\Reading and Writing Files\jabber.txt","r") as f:
    line = f.readline().rstrip()

chars = "'Twasevb"
print(line)
no_aposhtrope = line.strip(chars)
print(no_aposhtrope)

for character in line:
    if character in chars:
        print(f"removing : {character}")
    else:
        break
print("*"*80)
for character in line[::-1]:
    if character in chars:
        print(f"removing : {character}")
    else:
        break
