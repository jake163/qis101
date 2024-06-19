#!/usr/bin/env python3
# plot3d_surface.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import (
    LinearLocator,
)  # another tick mark locator, where you specify the number of ticks

# but not necessarily where the ticks go or their spacing
import sys
import os


def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


def plot(ax):  # plotting function, pass in ax
    x = np.linspace(-5, 5, 100)  # run x, y from -5 to 5, 100 subdomains
    y = np.linspace(-5, 5, 100)

    x, y = np.meshgrid(x, y)  # tensor product of x and y

    z = f(x, y)  # pass x,y array into the function z (vectorized)

    surf = ax.plot_surface(
        x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False
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


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
