#!/usr/bin/env python3
# archimedes_spiral.py

import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os
import sys

# This source shows how to compute the arc length of a polar curve without converting to
# cartesian:https://web.ma.utexas.edu/users/m408s/m408d/CurrentWeb/LM10-4-4.php

# However doing an integral is optional, we only need the final angle (8pi) to find arc length
# via the equation found here https://mathworld.wolfram.com/ArchimedesSpiral.html


def f(x):
    f = np.sqrt(x**2 + 1)  # integrand of arc length integral, polar coordinates
    return f


def arc_length(a, b):
    spiral_length1 = itg.quad(f, a, b)[0]
    return spiral_length1


def arc_length_eqn(x):
    spiral_length2 = (1 / 2) * (
        (x * np.sqrt(1 + x**2)) + np.log(x + np.sqrt(1 + x**2))
    )
    return spiral_length2


def plot(ax):
    theta = np.linspace(0, 8 * np.pi, 1000)
    r = theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y)
    ax.set_title(rf"$r = \theta$", fontsize=20)
    ax.set_xlabel("x", fontsize=16)  # label x axis as x
    ax.set_ylabel("y", fontsize=16)

    # ax.grid()  # add gridbars
    ax.axhline(0, color="black")  # make the x axis line black
    ax.axvline(0, color="black")

    ax.set_aspect(
        "equal"
    )  # laptops have higher resolution along x, we want pixels to be
    # square, equalize x and y resolutions for our graph


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    print(
        rf"The arc length is {arc_length(0, 8*np.pi)} when computed"
        f" using integration. The arc length is {arc_length_eqn(8*np.pi)} when computed using"
        f" the arc length formula."
    )
    plot(ax)  # pass in ax, executes plot(ax)
    plt.show()  # show the plot


if __name__ == "__main__":
    main()
