#!/usr/bin/env python3
# uniform_variance.py

import random


def run_trial(trial_num):
    trial_lower = random.randint(0, int(1e3))  # random lower bound up to 1000
    trial_upper = 2 * trial_lower + random.randint(
        0, int(1e3)
    )  # generate upper bound with
    # lower bound
    trial_size = random.randint(int(1e6), int(2e6))  # random trial size

    print(f"{trial_num:>10}", end="")
    print(f"{trial_lower:>10,}", end="")  # print off above numbers
    print(f"{trial_upper:>10,}", end="")
    print(f"{trial_size:>14,}", end="")

    prng_state = random.getstate()  # get current state of random number generator
    mean = 0
    for n in range(0, trial_size):
        roll = random.randint(
            trial_lower, trial_upper
        )  # randomly pick number between upper
        # and lower trial number
        mean += roll
    mean /= trial_size  # calculate overall mean

    random.setstate(prng_state)
    variance = 0
    for n in range(0, trial_size):
        roll = random.randint(
            trial_lower, trial_upper
        )  # randomly pick number between upper
        # and lower trial number
        variance += pow(roll - mean, 2)  # calculate variance per roll
    variance /= trial_size  # overall variance

    print(f"{mean:>14.3f}", end="")
    print(
        f"{variance:>14.3f}", end=""
    )  # print the above number (3 digits after decimal)

    magic_number = (
        pow(trial_upper - trial_lower, 2) / variance
    )  # calculate magic number
    # pow puts the two as the exponent
    print(f"{magic_number:>14.3f}")  # print magic_number


def main():  # executable from command line
    random.seed(2016)  # random number generator, initial value of 2016

    print(f"{'Trial #':>10}", end="")
    print(
        f"{'Lower':>10}", end=""
    )  # column headers, right justified, stay on same line
    print(f"{'Upper':>10}", end="")
    print(f"{'Size':>14}", end="")
    print(f"{'Mean':>14}", end="")
    print(f"{'Variance':>14}", end="")
    print(f"{'Magic':>14}")

    for trial_num in range(1, 16):  # go from 1 to 15 for our trial number
        run_trial(trial_num)


if __name__ == "__main__":
    main()
