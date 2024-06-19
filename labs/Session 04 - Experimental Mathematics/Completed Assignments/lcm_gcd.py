#!/usr/bin/env python3
# lcm_gcd.py
import numpy as np  # imported module 'numpy' using alias 'np'


def find_lcm(a, b):  # a can be greater or less than b
    GCD = np.gcd(a, b)  # use numpy's GCD function
    LCM = (
        a * b
    ) / GCD  # To get the greatest common multiple, we would multiply the two numbers and divide by the lowest
    # common divisor, which would be 1 for positive integers. This implies that the lowest common multiple is obtained by
    # dividing the product of the two numbers by the greatest common divisor, which is greater than or equal to one for positive
    # integers.
    print(int(LCM))  # gets rid of "LCM.0" output


def main():  # executable from command line
    find_lcm(447618, 2011835)  # function finds lcm for the two input numbers


if __name__ == "__main__":
    main()
