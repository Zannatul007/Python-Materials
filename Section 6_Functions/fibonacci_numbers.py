def fibonacci(n):
    """Return: `n`th fibonacci term , for positive `n` number
    """
    if 0<= n <=1:
        return n
    n_minus_1 = 1
    n_minus_2 = 0

    for i in range(n-1):
        result = n_minus_1+n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = result
    return n_minus_1
    


for i in range(36):
    print("{} : Fibonacci {}".format(i,fibonacci(i)))