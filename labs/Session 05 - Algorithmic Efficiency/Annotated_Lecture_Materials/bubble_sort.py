#!/usr/bin/env python3
# bubble_sort.py

import numpy as np
import time


def init_samples():  # define a function, no input
    samples = []  # make a empty list
    for i in range(100):
        samples.append(np.random.randint(1, 101))  # get a list with a hundred
        # random numbers. For each i, a random number is added to the end of
        # the list.
    return samples


def bubble_sort(samples):
    last_index = len(samples) - 1  # defines where you need to start for a given
    # pass, i.e. don't have to start at the beginning of the list each time.
    is_sorted = False  # assume that the list is not sorted
    while not is_sorted:  # While true (not false)
        swap_needed = False  # assign bool "false" to "swap needed"
        for i in range(last_index):  # iterate over list from 0 to len(samples)
            # - 2.
            if samples[i] > samples[i + 1]:  # if two numbers out of order
                temp = samples[i]  # temporary variable
                samples[i] = samples[i + 1]  # bigger number is moved back
                samples[i + 1] = temp  # smaller number moved up
                swap_needed = True  # keep looping if something needed to be
                # swapped
        if not swap_needed:  # if we have completed all swapping
            is_sorted = True  # leave the while loop
        else:
            last_index -= 1  # shift the starting point up by one
    return samples


def main():
    np.random.seed(2021)  #

    samples = init_samples()  # creating list of random numbers
    print(f"Unsorted: {samples}")

    samples = bubble_sort(samples)  # sort the numbers in the list
    print(f"Sorted: {samples}")

    num_trials = 10_000  # run this algorithm 10,000 times
    print(f"Running {num_trials:,} trials . . .")
    start_time = time.process_time()

    for _ in range(num_trials):  # iterate through list of length 10,000
        samples = init_samples()  # create a list of random numbers
        samples = bubble_sort(samples)  # sort that list by number size

    elapsed_time = time.process_time() - start_time

    print(f"Total run time: {elapsed_time:.3f} s")


if __name__ == "__main__":
    main()
