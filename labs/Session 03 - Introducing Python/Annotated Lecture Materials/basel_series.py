#!/usr/bin/env python3
# basel_series.py

import math

# import module that has functions we can call


def sum(n):
    # function defined similar to harmonic_series sum, difference is noted below
    s = 0
    for k in range(1, n + 1):
        s += 1 / k**2
        # exponent: "**"
        # s = s + 1/k^2
    return s


def main():
    # function that is executed by python interpreter from command
    # line
    terms = 1_000_000
    # can easily tell that the number above is one million because
    # of underscores. Also give a value to variable "terms"
    sigma = sum(terms)
    # call the sum function, pass in "term" as input
    print(f"Sum of first {terms:>7,} terms = {sigma:.14f}")
    # f string, "terms" placeholder is right justified, 7 point spacing,
    # commas used. "terms" has 14 digits after decimal.
    print(f"Magic number = {math.sqrt(sigma *6):.7f}")
    # call sqrt function from math library: math.sqrt


if __name__ == "__main__":
    main()
