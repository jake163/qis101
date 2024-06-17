#!/usr/bin/env python3
# prime_racer4.py

import numpy as np
import random
import time


def init_samples(num_samples, min_sample, max_sample):
    samples = [None] * num_samples
    for idx, _ in enumerate(samples):
        samples[idx] = random.randint(min_sample, max_sample)
    return samples


def is_primes(min_sample, max_sample):
    primes = []
    for num in range(min_sample, max_sample):
        prime = True
        for i in range(2, int(np.sqrt(num))):
            if num % i == 0:
                prime = False
        if prime:
            primes.append(num)
    return primes


def count_primes(samples, primes):
    current_prime = [0]
    num_primes = 0
    for _, val in enumerate(samples): #iterate through samples
        for _, num in enumerate(primes): #iterate through primes
            if val == current_prime[0]:  # if the value in samples is the current known prime
                num_primes += 1  # add to counter and move on
                break
            if val == num:  # check if value is in list of known primes
                num_primes += 1  # add to counter 
                current_prime[0] = val  # that number becomes the current known prime
    return num_primes


def main():
    random.seed(2016)

    num_samples = int(1e4)
    min_sample_val = int(1e5)
    max_sample_val = int(1e6)

    samples = init_samples(num_samples, min_sample_val, max_sample_val)

    primes = is_primes(min_sample_val, max_sample_val)

    print(
        f"Counting the number of primes in {num_samples:,} random samples\n"
        f"with each sample having a value between {min_sample_val:,} "
        f"and {max_sample_val:,} inclusive . . .",
    )

    start_time = time.process_time()
    num_primes = count_primes(samples, primes)
    elapsed_time = time.process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
