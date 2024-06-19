#!/usr/bin/env python3
# plot_ellipse.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import random


def plot(ax, a, b):  # pass in object ax
    while a == b:  # this would mean that it's a circle, not an ellipse
        a = random.randint(1, 10)  # generate random a and b
        b = random.randint(1, 10)

    theta = np.linspace(
        0, 2 * np.pi, 1000
    )  # array of thetas, theta ranges from 0 to 2pi,
    # 1000 subdomains (array has 1000 elements)

    radius = np.sqrt(1 / ((np.cos(theta) / a) ** 2 + (np.sin(theta) / b) ** 2))
    # ellipse function for given a and b

    r = random.randint(0, 256)  # randomly generated r,g,b values
    g = random.randint(0, 256)
    bl = random.randint(0, 256)
    for f in range(140, 256):
        while (
            r == f and g == f and bl == f
        ):  # don't want transparent axis labels and graph
            r = random.randint(0, 256)
            g = random.randint(0, 256)
            bl = random.randint(0, 256)

    values = [
        (r / 255),
        (g / 255),
        (bl / 255),
    ]  # have to pass in 'normalized' rgb values to
    # ax.plot

    ax.plot(theta, radius, color=values)

    ax.set_title(
        rf"$\frac{{ab}}{{\sqrt{{b^2\cos^2{{\theta}}+a^2\sin^2{{\theta}}}}}}$",
        fontsize=26,
        color=values,  # print equation
    )
    ax.set_xlabel(
        f"a = {a} and b = {b}"  # print other useful information on the x axis
        f" \n RGB = {r}, {g}, {bl}",
        fontsize=16,
        color=values,
    )
    ax.set_aspect("equal")
    ax.axis()


def main():
    a = random.randint(1, 10)  # generate random a and b
    b = random.randint(1, 10)
    fig, ax = plt.subplots(
        subplot_kw={"projection": "polar"}
    )  # change projection to be
    # polar, dictionary data type
    fig.canvas.set_window_title(os.path.basename(sys.argv[0]))  # give the figure
    # the filename
    plot(ax, a, b)  # make graph
    plt.show()  # show graph


if __name__ == "__main__":
    main()
