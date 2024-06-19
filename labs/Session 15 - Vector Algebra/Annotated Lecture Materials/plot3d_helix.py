#!/usr/bin/env python3
# plot3d_helix.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def plot(ax):
    theta = np.linspace(0, 20 * np.pi, 2000)  # poloidal angle, interval from 0 to 20 pi, 2000 subdomains

    x = theta * np.cos(theta)
    y = theta * np.sin(theta)
    z = theta #set the height equal to theta

    ax.plot(x, y, z) #connect the three-coordinate dots

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True) #constrained layout avoids adding
    #white space around the outside of plot, so matplotlib gives maximum priority to showing data points

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d") #extra parameter sets projection to 3d

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
