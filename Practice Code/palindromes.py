sentence1 = input()
sentence2 = input()
flag = False
for i in sentence1:
    if(i==sentence2[::-1]):
        flag = True
    else:
        flag = False

if (flag):
    print("Sentence1 and sentence 2 both are palindrome")
else:
    print("No")
# sentence_word_list = sentence.split(" ")
# print(sentence_word_list[::-1])
# new_string = ""
# for i in sentence_word_list[::-1]:
#     new_string += i
#     new_string += " "
# print(new_string)





