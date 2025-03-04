def multiply (x,y):
    """
    This function multiply two elements.
    Although this function intended to multiply two numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    Args:
        x (any): The first number to multiply.
        y (any): The number to multiply `x` by.

    Returns:
        any: product of `x`and`y`
    """
    return x*y

mul1 = multiply(2,3)
print(mul1)

def palindrome(string):
    """
    Check if a string is palindrome or not.
    A palindome is a string that reads the string same as backward and forward

    Args:
        string (str): the string to check
    Returns:
        bool: True if string is true otherwise return false
    """
    return string[::-1].casefold()==string.casefold()

str1 = "racecar"
if(palindrome(str1)):
    print("Yes {} is palindrom".format(str1))