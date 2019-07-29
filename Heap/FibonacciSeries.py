# encoding-utf-8
"""Iterative Fibonacci numbers generator Python implementation."""


def fibonacci(i):
    """Get i-th number from Fibonacci Series.

           | 1 if i = 0
    F(i) = { 2 if i = 1
           | F(i - 1) + F(i - 2) if i >= 2
    """
    if i == 0:
        return 1
    elif i == 1:
        return 2
    else:
        f_minus_1 = 2
        f_minus_2 = 1
        for j in range(i - 2):
            f_minus_2, f_minus_1 = f_minus_1, f_minus_1 + f_minus_2
        return f_minus_1 + f_minus_2


if __name__ == "__main__":
    # Generate first 100 Fibonacci numbers
    for x in range(100):
        print("F({0})=".format(x), fibonacci(x))
