#!/usr/bin/env python3
# quicksort.py

import numpy as np
import time


def init_samples():
<<<<<<< HEAD
    samples = np.random.randint(1, 101, 100)
=======
    samples = np.random.randint(
        1, 101, 100
    )  # getting back a numpy array of 100 numbers
    # all between 1 and 100
>>>>>>> 09efffcfbb028c8b77c33772285a978b2c071a9a
    return samples


def main():
<<<<<<< HEAD
    np.random.seed(2021)

    samples = init_samples()
    print(f"Unsorted: {samples}")

    samples = np.sort(samples)
    print(f"Sorted: {samples}")

    num_trials = 10_000
    print(f"Running {num_trials:,} trials . . .")
    start_time = time.process_time()

    for _ in range(num_trials):
        samples = init_samples()
        samples = np.sort(samples)

    elapsed_time = time.process_time() - start_time
=======
    np.random.seed(2021)  # numpy random number generator with initial value of
    # 2021

    samples = init_samples()  # generate unsorted lists
    print(f"Unsorted: {samples}")  # prints the output array of init_samples()

    samples = np.sort(samples)  # sort the unsorted lists with numpy.sort()
    print(f"Sorted: {samples}")  # prints sorted array

    num_trials = 10_000  #
    print(f"Running {num_trials:,} trials . . .")
    start_time = time.process_time()  # start timing

    for _ in range(num_trials):  # iterate 10,000 times
        samples = init_samples()  # initialize samples
        samples = np.sort(samples)  # use numpy.sort to sort samples

    elapsed_time = time.process_time() - start_time  # finish timing
>>>>>>> 09efffcfbb028c8b77c33772285a978b2c071a9a

    print(f"Total run time: {elapsed_time:.3f} s")


if __name__ == "__main__":
    main()
