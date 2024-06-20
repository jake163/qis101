#!/usr/bin/env python3
# hero_abilities.py

import numpy as np
import random


def calc_stats_1d20(num_rolls):  # roll a 20 sided die once
    prng_state = random.getstate()  # current state of random number generator
    mean = 0  # counts total value of all rolls
    for n in range(0, num_rolls):  # roll 1 million times
        roll = random.randint(3, 18)  # randomly pick number from desired range
        mean += roll  # add number to mean counter
    mean /= num_rolls  # calculate mean
    random.setstate(prng_state)  # recall the random number already generated
    variance = 0  # new counter
    for n in range(0, num_rolls):
        roll = random.randint(3, 18)  # same random number as above
        variance += pow(roll - mean, 2)  # calculate difference squared of roll and mean
    variance /= num_rolls  # calculate variance
    std_dev = np.sqrt(variance)  # square root it for std_dev
    return mean, std_dev  # returns tuple


def calc_stats_3d6(num_rolls):  # roll a 6 sided die three times
    prng_state = random.getstate()  # current state of random number generator
    mean = 0
    for n in range(0, num_rolls):
        roll = (
            random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        )  # roll 3
        # times
        mean += roll  # add roll to counter
    mean /= num_rolls  # calculate mean
    random.setstate(prng_state)  # remember previous state of random number generator
    variance = 0
    for n in range(0, num_rolls):
        roll = (
            random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        )  # same
        # random numbers as above
        variance += pow(roll - mean, 2)
    variance /= num_rolls  # calculate variance
    std_dev = np.sqrt(variance)  # calculate std. dev
    return mean, std_dev  # returns tuple


def main():
    random.seed(2016)  # random number generator, initial value of 2016

    num_rolls = int(1e6)  # integer number of rolls, 1 million

    print(f"Rolling abilities for {num_rolls:,} heroes...")

    m1, s1 = calc_stats_1d20(num_rolls)  # unpack tuple generated by calc_stats_1d20()
    m3, s3 = calc_stats_3d6(num_rolls)  # unpack tuple generated by calc_stats_sd6()

    #both functions give about the same mean, but the 20 sided die gives higher variance,
    #therefore 20 sided die is better if you want to roll higher numbers
    print(
        f"Mean ability (1d20): {m1:.2f}"
    )  # prints means from two functions, two digits
    # to right of decimal
    print(f"Mean ability (3d6):  {m3:.2f}")

    print(f"Standard Deviation ability (1d20): {s1:.2f}")  # same but for std. dev.
    print(f"Standard Deviation ability (3d6) : {s3:.2f}")


if __name__ == "__main__":
    main()