#!/usr/bin/env python3
# prime_racer1.py

import random
import time


def init_samples(
    num_samples, min_sample, max_sample
):  # function that gives us the list
    # of random numbers between min and max
    samples = [None] * num_samples  # list with 1e4 blank entries
    for idx, _ in enumerate(samples):  # iterate through samples list
        samples[idx] = random.randint(min_sample, max_sample)  # assign random number
        # between min and mix at the idx index
    return samples  # function outputs randomized list


def is_prime(n):
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True


def count_primes(samples):  # input randomized list into count_primes()
    num_primes = 0  # counter
    for _, val in enumerate(samples):  # we only care about specifying a random number
        # not that numbers index. Iterate through samples list
        if is_prime(val):  # if is_prime() returns true
            num_primes += 1  # add one to counter
    return num_primes  # returns counter


def main():
    random.seed(2016)  # imported random number generator, initial value of 2016

    num_samples = int(1e4)  # 10,000 samples
    min_sample_val = int(1e5)  # minimum sample value of 100,000
    max_sample_val = int(1e6)  # maximum sample value of 1,000,000

    samples = init_samples(num_samples, min_sample_val, max_sample_val)  # pass above
    # local variables into init_samples(), assign to variable samples

    print(
        f"Counting the number of primes in {num_samples:,} random samples\n"
        f"with each sample having a value between {min_sample_val:,} "
        f"and {max_sample_val:,} inclusive . . .",
    )

    start_time = time.process_time()  # start the stop watch
    num_primes = count_primes(samples)  # we are timing count_primes(), assigning that
    # value to the variable num_primes
    elapsed_time = time.process_time() - start_time  # pause the stop watch

    print(f"Number of primes found: {num_primes:,}")  # print num_primes in the f string
    # with commas
    print(f"Total run time (sec): {elapsed_time:.3f}\n")  # print elapsed time in f
    # string with three decimal places, blank line following printed line


if __name__ == "__main__":
    main()
