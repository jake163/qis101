#!/usr/bin/env python3
# herons_formula.py

import numpy as np  # import the numpy module using the alias "np"


def is_triangle(triangle):  # this function takes tuple defined in main()
    a, b, c = triangle  # unpack tuple
    return a + b > c and a + c > b and b + c > a  # verifies that triangle
    # passes triangle inequality (returns true or false), and allows for
    # degenerate triangles


def area(triangle):
    a, b, c = triangle
    s = (a + b + c) / 2
    return np.sqrt(s * (s - a) * (s - b) * (s - c))


def main():  # function executed by python interpreter via command line
    np.random.seed(2016)  # start imported random number generator at
    # initial value of 2016
    for n in range(10):  # iterate over list from 0 to 9, step of 1 (10 random
        # triangles).
        while not is_triangle(t := np.random.randint(1, 100, 3)):  # imported
            # randint chooses 3 numbers at random from list going from 1 to
            # 99, packs them into a tuple, this is assigned to the variable t
            # via walrus operator ':='. This 'while not' loop means we
            # provide instructions for when we randomly get invalid triangles.
            continue  # jump back to top of loop for invalid triangles, else
        # result gets printed
        print(f"{t} {area(t):>9.4f}")  # print f string, tuple of area of
        # valid triangles that is right justified with 4 digits after decimal


if __name__ == "__main__":
    main()
