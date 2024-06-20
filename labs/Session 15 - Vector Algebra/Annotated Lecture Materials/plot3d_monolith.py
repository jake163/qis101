#!/usr/bin/env python3
# plot3d_monolith_instructor.py

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import (
    Poly3DCollection,
)  # imported module poly3dcollection
import sys
import os


def plot(ax):
    length = 40  # X direction #declare spatial variables
    width = 10  # Y direction
    height = 90  # Z direction

    vertices = [None] * 8  # list of 8 empty slots

    vertices[0] = (0, 0, 0)  # Front Left Bottom #tuples
    vertices[1] = (length, 0, 0)  # Front Right Bottom
    vertices[2] = (length, width, 0)  # Back Right Bottom
    vertices[3] = (0, width, 0)  # Back Left Bottom

    vertices[4] = (0, 0, height)  # Front Left Top
    vertices[5] = (length, 0, height)  # Front Right Top
    vertices[6] = (length, width, height)  # Back Right Top
    vertices[7] = (0, width, height)  # Back Left Top

    facets = [None] * 6  # this object has 6 faces

    facets[0] = (
        vertices[0],
        vertices[1],
        vertices[2],
        vertices[3],
    )  # Bottom #group the vertices into faces
    facets[1] = (
        vertices[4],
        vertices[5],
        vertices[6],
        vertices[7],
    )  # Top #use your right hand, curl fingers
    # to establish a winding order with thumb outward to define facets
    facets[2] = (vertices[0], vertices[4], vertices[7], vertices[3])  # Left
    facets[3] = (vertices[1], vertices[2], vertices[6], vertices[5])  # Right
    facets[4] = (vertices[0], vertices[1], vertices[5], vertices[4])  # Front
    facets[5] = (vertices[2], vertices[3], vertices[7], vertices[6])  # Back

    p = Poly3DCollection(
        facets, linewidth=3, edgecolors=["Blue"], facecolors=["None"]
    )  # create polygon,
    # pass in list of faces, set linewidth, colors

    ax.add_collection3d(p)  # add the collection to the axis

    ax.view_init(azim=-45)  # pick a camera location (a meaningful one)
    ax.set_xlabel("x")  # specify axis labels
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_xlim3d(xmin=-100, xmax=100)  # set axis limits
    ax.set_ylim3d(ymin=-100, ymax=100)
    ax.set_zlim3d(
        zmin=0, zmax=100
    )  # set zmin to zero, because polygon sits on the floor


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
