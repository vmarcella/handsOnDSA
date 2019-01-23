def factorial(n):
    '''
        Calculate the factorial of n recursively

        Arguments:
            :n: an integer greater than or equal to 0
    '''
    # test for a base case
    if n == 0:
        return 1
    else:
        f = n * factorial(n - 1)

    return f

print(factorial(4))
