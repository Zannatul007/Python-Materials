class ErrorException(Exception):
    pass


try:
    x = None
    if x is None:
        raise ErrorException("x should not be None!")
    print(x)
except ErrorException as error:
    print(f"Custom Error: {error}")
