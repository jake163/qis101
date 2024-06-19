#!/usr/bin/env python3
# plot_multigraphs.py

import matplotlib.pyplot as plt
import sys
import os

import plot_parabola  # this function and following functions are imported python scripts,

# can simply import if in same folder. We have already made these plots
import plot_polynomial
import plot_rings
import plot_rose_curves


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(2, 2)  # 2 rows and 2 columns, 4 graphs

    ax = fig.add_subplot(gs[0, 0])  # top left
    plot_parabola.plot(ax)  # plot parabola at 0,0

    ax = fig.add_subplot(gs[0, 1])  # top row, second column
    plot_polynomial.plot(ax)  # plot polynomial there

    ax = fig.add_subplot(gs[1, 0])  # bottom left
    plot_rings.plot(ax)  # plot rings

    ax = fig.add_subplot(gs[1, 1], projection="polar")  # bottom right, polar projection
    plot_rose_curves.plot(ax)  # plot rose curves

    plt.show()


if __name__ == "__main__":
    main()
