#!/usr/bin/env python3
# herons_method.py
import random  # this random module
from numpy import mean  # from numpy module import mean function


def heron_root():
    s = random.randint(
        1e6, 2e6
    )  # randomly generate a integer greater than 1 million but less than 2 million, using randint
    # function
    e = 1e-8  # error threshold
    x = s / 2  # initial value of x
    while (
        abs(s - x**2) > e
    ):  # iterate until estimate it at or below the error threshold
        x = (s / x + x) / 2  # iteratively calculate x
    print(f"The square root of {s} is estimated to be {x:.8f}")


def main():  # executable from command line
    heron_root()


if __name__ == "__main__":
    main()
