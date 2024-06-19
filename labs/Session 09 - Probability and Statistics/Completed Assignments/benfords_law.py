#!/usr/bin/env python3
# benfords_law.py

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import random
import sys
import os


def prob_MSD():  # Warning: this function is slower then than the below function that is
    # commented out, but it still works. When you run this file the plot is on the left.
    p = np.zeros(10)
    for _ in range(100_000):
        n = random.randint(1, 1_000_000) ** 100
        while (
            n >= 10
        ):  # repeatedly divide by 10 until whats left is a number less than 10
            n = n // 10  # rounds down each division, gives us MSD
        p[int(n)] += 1  # adds 1 at the appropriate index
    p = p[1:]  # 0 isn't a leading digit
    p = p / 100_000  # vectorized, each number in p is normalized
    print(p)
    return p


def p_MSD():  # This is the function from TA Time on 06/17, when you run this file the plot
    # is on the right
    p = np.zeros(10)
    for _ in range(100_000):
        n = random.randint(1, 1_000_000) ** 100
        p[int(str(n)[0])] += 1
    p = p[1:]
    p = p / 100_000
    print(p)
    return p


def plot1(ax1):

    ax1.bar(range(1, 10), prob_MSD(), zorder=2.0)

    ax1.grid()

    ax1.set_title(f"Benford's Law")
    ax1.set_xlabel("Most Significant Digit (MSD)")
    ax1.set_ylabel("Probability of MSD")

    ax1.xaxis.set_major_locator(MultipleLocator(1))


def plot2(ax2):

    ax2.bar(range(1, 10), p_MSD(), zorder=2.0)

    ax2.grid()

    ax2.set_title(f"Benford's Law")
    ax2.set_xlabel("Most Significant Digit (MSD)")

    ax2.xaxis.set_major_locator(MultipleLocator(1))


def main():
    print("Calculating... this can take 13 seconds or more")
    random.seed(2016)

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 2)

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    plot1(ax1)
    plot2(ax2)
    # I didn't use the same randomly generated integers to make both plots, that's why the plots
    # look a little different.

    plt.show()


if __name__ == "__main__":
    main()
