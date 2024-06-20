#!/usr/bin/env python3
# sort_race.py

import numpy as np
import timeit  # measures execution time of small code snippits
from numba import jit  # jit function in numba module can compile functions to

# machine language, so they run faster


@jit(nopython=True)  # @jit tells numba to compile the following function
def init_samples():
    np.random.seed(2021)
    samples = np.arange(50_000, 0, -1)  # array that starts at zero, ends at 0, in
    # increments of 1
    return samples


@jit(nopython=True)
def bubble_sort(a):  # bubble sort in compiled code
    last_index = len(a) - 1
    is_sorted = False
    while not is_sorted:
        swap_needed = False
        for i in range(last_index):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                swap_needed = True
        if not swap_needed:
            is_sorted = True
        else:
            last_index -= 1
    return


@jit(nopython=True)
def median_of_three(a, lo, hi):
    mid = (lo + hi) // 2
    x, y, z = a[lo], a[mid], a[hi]
    if x < y:
        if y < z:
            return mid
        elif x < z:
            return hi
        else:
            return lo
    else:
        if x < z:
            return lo
        elif y < z:
            return hi
        else:
            return mid


@jit(nopython=True)
def quick_sort_partition(a, lo, hi):  # This function splits the array into
    # sublists

    pi = median_of_three(a, lo, hi)  # pivot index, look at first, last, and
    # middle value. Start quicksort with the middle value of the three
    p = a[pi]  # pivot value

    while True:  # decide what goes to left list, what goes to right list
        while a[lo] <= p and lo < pi:
            lo += 1
        while a[hi] > p and hi > pi:
            hi -= 1
        if lo == pi and hi == pi:
            return pi

        # Swap array values at lo and hi indexes
        a[lo], a[hi] = a[hi], a[lo]

        if lo == pi:
            pi = hi
        elif hi == pi:
            pi = lo


@jit(nopython=True)
def quick_sort(
    a, lo, hi
):  # This function takes in array a, left and right index of where
    # sublist is
    if lo < hi:  # when lower index less then higher index
        p = quick_sort_partition(a, lo, hi)  # call quick_sort_partition()
        if p > 0:
            quick_sort(a, lo, p - 1)
        quick_sort(a, p + 1, hi)
    return


@jit(nopython=True)
def bubble_sort_once():
    samples = init_samples()
    bubble_sort(samples)


@jit(nopython=True)
def quicksort_once():
    samples = init_samples()
    quick_sort(samples, 0, len(samples) - 1)


def main():
    print("Running tests . . .")

    time = timeit.timeit(bubble_sort_once, number=10)
    print(f"Bubble sort time: {time/10:.3f} secs")

    time = timeit.timeit(quicksort_once, number=100)
    print(f"Quicksort time  : {time/100:.3f} secs")


if __name__ == "__main__":
    main()
