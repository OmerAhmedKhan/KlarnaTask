import logging
from decorator import hawk_eye

logging.basicConfig(filename='error.log',level=logging.ERROR)


ERROR1 = "Invalid Argument"
ERROR2 = "Argument limit exceeds"

@hawk_eye
def get_fab(n):
    """Get Fibonacci of a given number"""
    x = 0
    y = 1

    if not isinstance(n, int):
        return ERROR1

    for i in range(n):
        tmp = y
        y = x + y
        x = tmp

    return x


@hawk_eye
def get_ack(m, n):
    """Get Ackermann number from provided arguments"""

    if not isinstance(m, int):
        return ERROR1

    if not isinstance(n, int):
        return ERROR1


    if m == 0:
        return n + 1
    elif m == 1:
        return n+2
    elif m == 2:
        return 2*n+3
    elif m == 3:
        return 2**(n+3)-3
    else:
        return ERROR2

@hawk_eye
def get_fact(n):
    """Get factorial of a number"""
    result = 1

    if not isinstance(n, int):
        return ERROR1

    for x in range(1, n + 1):
        result = result * x

    return result