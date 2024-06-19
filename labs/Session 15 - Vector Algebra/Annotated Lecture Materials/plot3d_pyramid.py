#!/usr/bin/env python3
# plot3d_pyramid_instructor.py

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math
import sys
import os


def plot(ax):
    golden_ratio = (1 + math.sqrt(5)) / 2  # define the golden ratio

    length = 150  # X direction
    width = 150  # Y direction
    height = length * golden_ratio  # Z direction

    vertices = [
        None
    ] * 5  # pre-declare an array with 5 empty slots, reference slots with index number
    vertices[0] = (0, 0, 0)  # Base Front Left
    vertices[1] = (length, 0, 0)  # Base Front Right
    vertices[2] = (length, width, 0)  # Base Back Right
    vertices[3] = (0, width, 0)  # Base Back Left
    vertices[4] = (length / 2, width / 2, height)  # Apex

    facets = [None] * 5
    facets[0] = (
        vertices[0],
        vertices[1],
        vertices[2],
        vertices[3],
    )  # Base, #base is a square
    facets[1] = (
        vertices[0],
        vertices[3],
        vertices[4],
    )  # Left #there are four sides, all triangles
    # using right hand rule to define facets, facets can have three or more vertices
    facets[2] = (vertices[0], vertices[1], vertices[4])  # Front
    facets[3] = (vertices[1], vertices[2], vertices[4])  # Right
    facets[4] = (vertices[2], vertices[3], vertices[4])  # Back

    p = Poly3DCollection(
        facets, linewidth=3, edgecolors=["darkgoldenrod"], facecolors=["gold"]
    )  # it's possible to specific specific colors for specific faces/edges

    ax.add_collection3d(p)

    ax.view_init(azim=-79, elev=28)  # specify starting location of camera
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim3d(xmin=-10, xmax=200)
    ax.set_ylim3d(ymin=-10, ymax=200)
    ax.set_zlim3d(zmin=0, zmax=350)


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
