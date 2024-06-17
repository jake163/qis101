#!/usr/bin/env python3
# plot_circle.py

import matplotlib.pyplot as plt
import numpy as np
import sys
import os


def plot(ax):
    radius = 250  # want to plot circle of radius 250
    theta = np.linspace(0, 2 * np.pi, 1000)  # polar angle domain is 0 to 2pi, 1000
    # subintervals, np.linspace() returns an array of 1000 values
    x = radius * np.cos(theta)  # x = rcos(theta) as usual, vectorized operator on theta
    y = radius * np.sin(theta)  # y = rsin(theta) as usual, vectorized operator on theta

    ax.plot(x, y)  # connects points

    ax.set_title(f"$x^2 + y^2 = {radius}$")  # equation of the circle, LaTeX, f string
    # allows replacement fields
    ax.set_xlabel("x")  # label x axis as x
    ax.set_ylabel("y")

    ax.grid()  # add gridbars
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
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
