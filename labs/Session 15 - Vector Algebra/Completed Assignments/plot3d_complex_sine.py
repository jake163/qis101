#!/usr/bin/env python3
# plot3d_complex_sine.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import (
    LinearLocator,
)  # another tick mark locator, where you specify the number of ticks

# but not necessarily where the ticks go or their spacing
import sys
import os


def f(z):
    return abs(np.sin(z))


def plot(ax):  # plotting function, pass in ax
    x = np.linspace(-2.5, 2.5, 1000)  # x domain is from -2.5 to 2.5, 100 subintervals
    y = np.linspace(-1, 1, 1000)

    X, Y = np.meshgrid(x, y)  # tensor product of x and y

    Z = f(X + Y * 1j)  # pass x,y array into the function z (vectorized)

    surf = ax.plot_surface(
        X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False
    )  # cmap stands for
    # color map, where the color is based on height.

    ax.zaxis.set_major_locator(
        LinearLocator(10)
    )  # z axis has 10 and only 10 tick marks
    ax.zaxis.set_major_formatter(
        "{x:.02f}"
    )  # tick mark numbers have two decimal places

    plt.colorbar(
        surf, ax=ax, shrink=0.5, aspect=5
    )  # colorbar is like the legend for the z axis
    ax.view_init(azim=-45)
    ax.set_xlabel(r"$x \in \mathbb{R}$", fontsize=16)
    ax.set_ylabel(r"$y \in \mathbb{I}$", fontsize=16)
    ax.set_zlabel(r"$f(z) = |\sin({z})|$", fontsize=16)
    ax.set_title("Complex Sine", fontsize=20)


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
