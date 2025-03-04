def is_palindrome(string):
    string = str.upper(string)
    return string[::-1]== string
def is_palindrome_sentence(string):
    str1 = ""
    for i in string:
        if(i.isalnum()):
            str1+=i
    return is_palindrome(str1)

str_sentence= input("Please write a sentence\n")
if is_palindrome_sentence(str_sentence):
    print("'{}' is a palindrome".format(str_sentence))
else:
    print("'{}' is not a palindrome".format(str_sentence))