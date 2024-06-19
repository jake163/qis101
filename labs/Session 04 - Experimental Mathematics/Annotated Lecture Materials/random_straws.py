#!/usr/bin/env python3
# random_straws.py

import numpy as np


def run_trial():
    length = straws = 0.0  # we start at zero straws, zero length, specifying
    # decimals
    while length <= 1.0:  # iterate until 1.0 is minimally exceeded
        length += np.random.random()  # totally random number generator
        straws += 1  # accumulate straws by increments of 1
    return straws


def main():  # function executed via the command line
    np.random.seed(2016)  # generates random numbers based on initial value
    # of 2016

    num_trials = int(1e7)  # number in parenthesis is integer, number of trials

    print(f"Performing {num_trials:,} trials...")

    total_straws = 0  # keeps track of how many straws needed to reach 1

    for _ in range(0, num_trials):  # underscore means we don't care about
        # giving the variable a name. Iterate over list from 0 to num_trials - 1
        total_straws += run_trial()  # function that helps us accumulate straws

    mean = total_straws / num_trials  # average number of straws, decimal

    print(f"Mean straws per trial     : {mean:.6f}")
    print(f"Base of natural logarithm : {np.e:.6f}")  # e is base of natural log,
    # given by numpy. 6 digits after the decimal point


if __name__ == "__main__":
    main()
