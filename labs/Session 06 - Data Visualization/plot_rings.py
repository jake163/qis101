#!/usr/bin/env python3
# plot_rings.py

import matplotlib.pyplot as plt
import numpy as np
import sys
import os


def plot(ax):
    radius = 25
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    x_offset = 5 / 2 * radius  # shift x array values by 5r/2 factor
    y_offset = radius  # shift y array values by r

    ax.plot(x, y, color="black", linewidth=12)
    ax.plot(
        x - x_offset, y, color="blue", linewidth=12
    )  # shift x values to the right of
    # origin, this circle is blue, thick border
    ax.plot(x + x_offset, y, color="red", linewidth=12)
    # shift x values to the left of origin, make this circle red, thick border
    ax.plot(
        x - x_offset / 2, y - y_offset, color="yellow", linewidth=12
    )  # shift x values
    # to the right of origin by half of red circle, y values shifted down by r, thick
    # border
    ax.plot(
        x + x_offset / 2, y - y_offset, color="green", linewidth=12
    )  # shift x values
    # to the left of origin by half of red circle, y values shifted down by r, thick
    # border

    ax.set_title("The Olympic Rings")  # the title of the graph is "The Olympic Rings"
    ax.set_aspect("equal")  # x and y pixel resolution equal
    ax.axis("off")  # we don't want to see x and y axes


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
