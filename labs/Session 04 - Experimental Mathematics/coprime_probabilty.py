#!/usr/bin/env python3
# coprime_probability.py

import numpy as np


def main():
    np.random.seed(2021)  # imported random number generator, (nonrandom)
    # initial value of 2021. Library: np, module: random, function: seed

    num_coprime_pairs = 0

    num_iterations = 1_000_000  # how many times we randomly pick integers
    # and check gcd.

    for i in range(num_iterations):  # iterate over list going from 0 to n-1
        a = np.random.randint(100_000)  # pick random int in list from 0 to n-1
        b = np.random.randint(100_000)  # same as above
        if np.gcd(a, b) == 1:  # imported gcd function checks if a,b are coprime
            num_coprime_pairs += 1  # if true, our counter goes up by one

    p = num_coprime_pairs / num_iterations  # calculate probability

    print(f"Coprime Probability = {p:.4f}")
    print(f"Hidden constant     = {np.sqrt(6 / p):.4f}")  # f string, placeholder
    # is imported square root function taking '6/p' as input, 4 digits after
    # decimal point.


if __name__ == "__main__":
    main()
