import math

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        # Get the number of digits of form the largest number  
        digits = max(int(math.log10(x) + 1), int(math.log10(y) + 1))

        # Get digits divided by 2 rounded up
        digits_2 = int(math.ceil(digits / 2))

        # Add 1 to digits if digits is an uneven number
        digits = digits if digits % 2 == 0 else digits + 1

        # Calculate a, b, c, and d
        a, b = divmod(x, 10**digits_2)
        c, d = divmod(y, 10**digits_2)

        # Apply recursive steps
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_bc = karatsuba((a + b), (c + d)) - ac - bd

        # Performs the multiplication 
        return (((10**digits) * ac) + bd + ((10**digits_2) * (ad_bc)))

# Calculate the result of 1234 * 3456, using karatsuba multiplication
result = karatsuba(1234, 3456)
print(result)
