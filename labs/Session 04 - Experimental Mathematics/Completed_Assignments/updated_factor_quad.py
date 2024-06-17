#!/usr/bin/env python3
# updated_factor_quad.py
import numpy as np


def factor_quadratic(J, K, L):  # define the factor function, takes in quadratic
    # coeffs ints.
    counter = 0
    print("Given the quadratic q:")
    print(f" {J}x^2 + ({K})x + ({L}) = 0")

    for a in range(1, J + 1):  # we want to include J in the list of numbers
        # iterated over
        if J % a == 0:  # i.e. is 'a' a factor of 'J'?
            c = J // a  # "//" integer division: rounds down decimal
            for b in range(1, L + 1):  # similar process for b
                if L % b == 0:
                    d = L // b
                    if a * d + b * c == K:  # check that a and b (and hence
                        # c and d) yield K
                        if a <= c:  # eliminates commutative interchanges of the factors
                            counter += 1
                            print(f" q = ({a}x + ({b}))" f"({c}x + ({d}))")
    if counter == 0:  # we couldn't compute a single K with any a,b,c,d found
        print("Quadratic q cannot be factored")


def main():
    factor_quadratic(115425, 3254121, 379020)  # function has j,k,l integer inputs
    # and is executable from the command line


if __name__ == "__main__":
    main()
