#!/usr/bin/env python3
# plot_parabola.py

import matplotlib.pyplot as plt  # open module.function as alias
import numpy as np  # import module as alias
import sys  # interrogate runtime
import os  # presents structured filesystem


def plot(ax):
    x = np.linspace(-4, 5, 100)  # specifies x and y domain, with 100 equally spaced
    # subintervals, includes endpoints
    y = np.power(x, 2) + 1  # y = x^2 + 1 , eliminates needing to write for loop

    # Plot the graph on the main axes
    ax.plot(x, y)  # pass x and y variables into ax() to plot on axes

    # Give the graph a title and axis labels
    ax.set_title("$y = x^2+1$")  # LaTeX format
    ax.set_xlabel("x")  # the x axis is called x
    ax.set_ylabel("y")

    # Center the graph on appropriate range
    ax.set_xlim(-6, 6)  # set the range of the x axis
    ax.set_ylim(-3, 30)

    # Turn on the grid, and add decorations
    ax.grid()  # optionally activate grid
    ax.plot(0, 1, color="red", marker="o")  # manually identify x = 0
    ax.axhline(1, color="gray", linestyle="--")  # line at y = 1


def main():
    fig = plt.figure(
        os.path.basename(sys.argv[0])
    )  # basename(path) returns tail of path
    # in python
    gs = fig.add_gridspec(1, 1)  # we are making 1 graph

    ax = fig.add_subplot(gs[0, 0])  # it is the first/only subplot
    plot(ax)  # pass in ax, adds axes

    plt.show()  # shows the complete plot


if __name__ == "__main__":
    main()
