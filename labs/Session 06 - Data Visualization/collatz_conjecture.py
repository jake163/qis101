#!/usr/bin/env python3
# collatz_conjecture.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator  # tell pyplot to figure out appropriate

# number of minor ticks, don't get minor ticks unless you import it
from numba import numba, jit, prange  # numba, @jit allow for functions to be read as

# compiler code. CPUs have multiple independent cores, prange distributes tasks across
# these cores
import sys
import os


@jit(nopython=True)  # function is in compiler code
def stop_time(n):  # number of iterations before reaching 1
    counter = 0
    while n > 1:  # stop iterating at n = 1
        if n % 2 == 0:  # if n is even, we halve it
            n = n // 2
        else:
            n = 3 * n + 1  # otherwise for n odd, calculate 3n + 1
        counter += 1  # for each step where n > 1, we count that step
    return counter


@jit(
    nopython=True, parallel=True
)  # function is in compiler code, split tasks and run them
# in parallel across cpu cores
def stop_times(max_n):
    y = np.zeros(
        max_n, dtype=numba.int64
    )  # give array of zeros of dimension max_n, each
    # zero has same data type numba 64 bit integer (lists can have heterogeneous data
    # #type)
    for i in prange(
        max_n
    ):  # split max n into chunck, iterate through each chunk on each
        # core
        y[i] = stop_time(i)  # store stop time in y, location number is the stop time of
        # that number
    return y


def plot(ax):
    max_n = 1_000_000  # assign int(1e6) to variable max_n

    print(
        "Calculating the Collatz stopping time for"
        f" the first {max_n:,} natural numbers . . ."
    )

    y = stop_times(max_n)  # pass in max_n to function stop_times(), stop time for each
    # n up to max_n

    ax.set_title(f"Collatz Conjecture (n < {max_n:,})")
    ax.set_xlabel("Stopping Time")
    ax.set_ylabel("Count")

    ax.hist(y, bins=500, color="blue")  # bin y numbers into 500 subintervals

    ax.yaxis.set_minor_locator(AutoMinorLocator())  # on the y axis, turn on minor ticks
    # and let pyplot set the number of minor ticks


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
