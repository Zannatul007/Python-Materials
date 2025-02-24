#Write a function that takes a string and returns a dictionary where keys are characters and values are their frequencies.
#Character Frequency Counter
def alphabet_counter(string1:str):
    alphabet_counter = {}
    string1 = string1.casefold()
    for i in string1:
        if i.isnumeric() or i.isalpha():
            alphabet_counter[i] = alphabet_counter.setdefault(i,0)+1
    return alphabet_counter

input_str = input("Take an Input String \n")
counter = alphabet_counter(input_str)
for item,count in counter.items():
    print(f"{item} : {count}")

#Word Frequency Counter 

def word_counter(sentence1:str):
    word_counter = {}
    sentence1 = sentence1.casefold()
    for word in sentence1.split():
        word_counter[word] = word_counter.setdefault(word,0)+1
    return word_counter


input_sentence1 = input("Please write a sentence : \n")
counter_word = word_counter(input_sentence1) 

for key,value in counter_word.items():
    print(f"[{key}]:{value}")
    


#Anagram Checker
#Write a function that takes two strings and returns True if they are anagrams (i.e., they contain the same letters with the same frequency), otherwise False.

def anagram_checker(string1:str,string2:str):
    string1_counter = {}
    string2_counter = {}
    flag = False
    for i in string1.casefold():
        if(i.isalnum() or i.isnumeric()):
            string1_counter[i] = string1_counter.setdefault(i,0)+1
    for j in string2.casefold():
        if(j.isalnum() or j.isnumeric()):
           string2_counter[j] = string2_counter.setdefault(j,0)+1
    for key,value in sorted(string1_counter.items()):
        if(string1_counter[key] == string2_counter[key]):
            flag = True
        else:
            flag = False
            break


    return flag

input_str1,input_str2 = input("\n"),input("\n")
if(anagram_checker(input_str1,input_str2)):
    print("Yes both strings are anagram")
else:
    print("No they are not anagram")


#Most Frequented Alphabet 
def most_frequented_alphabet(string1:str):
    alphabet_counter = {}
    
    for i in string1.casefold():
        if i.isnumeric() or i.isalpha():
            alphabet_counter[i] = alphabet_counter.setdefault(i,0)+1
    alphabet_counter_sorted = dict(sorted(alphabet_counter.items(),key = lambda x : x[1], reverse=True))
    print(alphabet_counter_sorted)
    

# input_s = input("Check the most frequented alphabet\n")
# most_frequented_alphabet(input_s)