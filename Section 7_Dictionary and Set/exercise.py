input_str = input("Write a string : ")
input_str = input_str.casefold()
count_alphabet = {}

for i in input_str:
    if i.isalnum() or i.isnumeric():
        count_alphabet[i] = count_alphabet.setdefault(i,0)+1

for alphabet, count in count_alphabet.items():
    print(f"{alphabet}:{count}")
