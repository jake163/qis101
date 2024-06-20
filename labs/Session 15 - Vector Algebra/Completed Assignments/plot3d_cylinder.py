#!/usr/bin/env python3
# plot3d_sphere.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import random


def plot(ax):  # define the plotting function
    num = num = random.randint(-100, -1)
    v = np.linspace(0, 2 * np.pi, -num)  # toroidal angle 0 to 2pi in 30 subdomains
    h = np.linspace(num, -num, -num)

    x = 30 * np.cos(v)  # compute tensor product of the sines of u and v for x
    y = 30 * np.sin(v)
    z = np.outer(
        h, np.ones_like(h)
    )  # tensor product of h and an array of 1's of the same
    # dimension of h

    ax.set_xlabel(r"$x = 30\cos{\theta}$", fontsize=16)
    ax.set_ylabel(r"$y = 30\sin{\theta}$", fontsize=16)
    ax.set_zlabel(rf"${num} \leq z \leq {-num}$", fontsize=16)
    ax.set_title("Cylinder", fontsize=20)

    ax.plot_wireframe(x, y, z)


def main():
    fig = plt.figure(
        os.path.basename(sys.argv[0]), constrained_layout=True
    )  # constrained layout means that
    # "graphing power" is focused just on the object itself, and not the space outside the object

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")  # need 3d projection

    plot(ax)  # plot function, pass in variable ax

    plt.show()


if __name__ == "__main__":
    main()
