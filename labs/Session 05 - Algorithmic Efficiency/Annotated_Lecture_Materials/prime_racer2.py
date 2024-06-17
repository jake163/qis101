#!/usr/bin/env python3
# prime_racer2.py

import random
import time


def init_samples(num_samples, min_sample, max_sample):
    samples = [None] * num_samples
    for idx, _ in enumerate(samples):
        samples[idx] = random.randint(min_sample, max_sample)
    return samples


def is_prime(n):
    if n % 2 == 0:
        return False  # test n for being even, if even we don't do anything
    for factor in range(3, n, 2):  # iterate through list going from 3 to n-1, increment
        # 2. We do not divide by 1, 2, or n.
        if n % factor == 0:  # divide by factors in above list, check for no remainder
            return False  # it can't be prime if it has a remainder
    return True  # if we can't find a factor, then it's prime


def count_primes(samples):
    num_primes = 0
    for _, val in enumerate(samples):
        if is_prime(val):
            num_primes += 1
    return num_primes

    # run time is cut down by half, which make sense because we halved the for loops
    # that we need to do


def main():
    random.seed(2016)

    num_samples = int(1e4)
    min_sample_val = int(1e5)
    max_sample_val = int(1e6)

    samples = init_samples(num_samples, min_sample_val, max_sample_val)

    print(
        f"Counting the number of primes in {num_samples:,} random samples\n"
        f"with each sample having a value between {min_sample_val:,} "
        f"and {max_sample_val:,} inclusive . . .",
    )

    start_time = time.process_time()
    num_primes = count_primes(samples)
    elapsed_time = time.process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
