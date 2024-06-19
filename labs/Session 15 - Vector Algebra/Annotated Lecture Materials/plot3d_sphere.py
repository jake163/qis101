#!/usr/bin/env python3
# plot3d_sphere.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def plot(ax):  # define the plotting function
    u = np.linspace(0, np.pi, 30)  # poloidal angle, 0 to pi chopped up
    # into 30 subintervals
    v = np.linspace(0, 2 * np.pi, 30)  # toroidal angle, 0 to 2pi chopped
    # up into 30 subintervals

    x = np.outer(np.sin(u), np.sin(v))  # compute x matrix with formula (r = 1)
    # by tensor product of sinu and sinv matrices
    y = np.outer(np.sin(u), np.cos(v))
    z = np.outer(np.cos(u), np.ones_like(v))  # compute z matrix (r = 1) by
    # computing tensor product of cosu and an array of 1s in the shape of v

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # TODO: Uncomment the following lines one-by-one
    # ax.scatter(x, y, z)
    ax.plot_wireframe(x, y, z)
    # ax.plot_surface(x, y, z)


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
