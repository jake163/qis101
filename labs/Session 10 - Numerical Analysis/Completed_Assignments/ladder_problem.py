#!/usr/bin/env python3
# ladder_problem.py

import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os
import sys


def f(x: float) -> float:  # height of the ladder as a function of theta
    f = (2 / np.sin(x)) + (1 / np.cos(x))
    return f


def compute_max():
    y_max = opt.minimize(
        lambda x: f(x), 1.57
    )  # Finds the critical point of f(x). 1.57 is the initial guess. Putting in a
    # guess of 0 or pi / 2 leads to convergence failure, which isn't surprising because that leads to division by 0. All other
    # guesses that I've tried, between 0 and pi/2, have worked.
    parse_y = str(y_max).split(
        "\n"
    )  # opt.minimize() outputs a lot of information (print opt.minimize(lambda x: f(x), 1.57))
    # to see it. That's why I convert it to to a string, and parse it.
    just_ymax = parse_y[0].split(" ")
    crit_x = parse_y[9].split(" ")
    crit_x1 = crit_x[9].split("array([")
    just_crx = crit_x1[1].split("])")
    return [float(just_ymax[7]), float(just_crx[0])]  # returns [y_max, x_crit]


def plot(ax):
    x = np.linspace(
        0.021, 1.56, 1000
    )  # i.e., the domain is (0, pi/2) exclusive, exclusive.
    y = f(x)
    ax.plot(x, y)
    ax.set_title(
        rf"$f (\theta) = \frac{{2}}{{\sin{{\theta}}}}+\frac{{1}}{{\cos{{\theta}}}}$",  # LaTeX code for f(x)
        fontsize=20,
    )
    ax.set_xlabel(rf"$\theta \ (rad)$", fontsize=16)  # LaTeX code for x axis label
    ax.set_ylabel(rf"$f(\theta)$", fontsize=16)
    ax.xaxis.set_major_locator(MultipleLocator(0.2))  # x axis tick spacings
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.plot(
        compute_max()[1],
        compute_max()[0],
        color="red",
        marker="o",
        label="Critical Point",
    )  # manually identify creitical point
    ax.axhline(
        compute_max()[0], color="red", linestyle="--"
    )  # dashed line at critical point
    ax.legend()  # shows label for critical point


def main():
    fig = plt.figure(
        os.path.basename(sys.argv[0])
    )  # the identifier for this figure, here it is the script path
    gs = fig.add_gridspec(1, 1)  # 1 by 1 figure space
    ax = fig.add_subplot(gs[0, 0])  # first (only) plot in the figure space
    print(
        f"The maximum ladder height is {compute_max()[0]:.4f} meters for the"
        f" angle {compute_max()[1]:.5f} rad"
    )
    plot(ax)  # pass in ax, executes plot(ax)
    plt.show()  # show the plot


if __name__ == "__main__":
    main()
