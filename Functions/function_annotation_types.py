def multiply (x:float,y: float):
    """
    This function multiply two elements.
    This function intended to multiply two numbers

    Args:
        x (float): The first number to multiply.
        y (float): The number to multiply `x` by.

    Returns:
        float: product of `x`and`y`
    """
    return x*y

mul1 = multiply(2,3)
print(mul1)
print(type(mul1))

def palindrome(string:str)-> bool:
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