#!/usr/bin/env python3
# euclid_gcd.py


def gcd(a, b):
    if a < b:
        a, b = b, a  # This tuple conveniently swaps the values of the variables
        # because we need a greater than b
    c = a - b
    while c > 0:  # iterate until c = 0
        if c > b:
            a = c  # c becomes a if bigger than b
        else:  # if c is less than b
            a = b
            b = c
        c = a - b
    return b  # returns b for c = 0


def main():  # executable from command line
    a = 182
    b = 231
    print(f"The GCD of {a} and {b} = {gcd(a,b)}")  # gcd function with variable
    # values assigned in main()


if __name__ == "__main__":
    main()
