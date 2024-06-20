#!/usr/bin/env python3 #shebang, run from command line with python3 interpreter
# fermat_derivative.py #name of the file

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator  # specify major/minor ticks
import sys
import os


def f(x):  # cos(x)
    return np.cos(x)


def f_prime(x, h):  # f'(x)
    return (f(x + h) - f(x)) / h  # lim as h -> 0 of this is derivative


def plot(ax):
    a = -4 * np.pi  # interval is from -4pi to 4pi
    b = 4 * np.pi
    n = 500  # 500 subdomains

    x = np.linspace(a, b, n)

    y = f(x)
    y_prime = f_prime(x, (b - a) / n)  # for every x, we estimate slope of tangent line

    ax.plot(x, y, label="y")  # plot x and y
    ax.plot(
        x, y_prime, label=r"$\frac{dy}{dx}$"
    )  # plot x and numeric y', using latex display

    ax.set_title(r"$y = cos(x)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.xaxis.set_major_locator(
        MultipleLocator(2)
    )  # set major tick marks at multiple of 2, x
    # axis
    ax.yaxis.set_major_locator(
        MultipleLocator(0.2)
    )  # major tick marks of 0.2 on y axis
    ax.legend(loc="upper right")  # legend is at upper right corner

    ax.axhline(0, color="black", linestyle="-")  # black axes
    ax.axvline(0, color="black", linestyle="-")


def main():
    fig = plt.figure(
        os.path.basename(sys.argv[0])
    )  # parse out name of file, first argument
    # in argument vector
    gs = fig.add_gridspec(1, 1)  # 1 column 1 row figure space

    ax = fig.add_subplot(gs[0, 0])  # top left subplot figure space
    plot(ax)  # plot graph

    plt.show()  # show graph


if __name__ == "__main__":
    main()
