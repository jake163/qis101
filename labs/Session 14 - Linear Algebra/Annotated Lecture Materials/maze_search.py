#!/usr/bin/env python3
# maze_search.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection, PatchCollection
from matplotlib.patches import Rectangle
import pickle
import os
import sys


def plot_cell_walls(ax, maze):
    for y in range(10):
        bottom = (9 - y) * 10
        top = bottom + 10
        for x in range(10):
            left = x * 10
            right = left + 10
            cell = maze[y, x]
            if cell & 1 == 1:
                lc = LineCollection(
                    [[(left, top), (right, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)
            if cell & 2 == 2:
                lc = LineCollection(
                    [[(right, bottom), (right, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)
            if cell & 4 == 4:
                lc = LineCollection(
                    [[(left, bottom), (right, bottom)]], color="black", linewidth=3
                )
                ax.add_collection(lc)
            if cell & 8 == 8:
                lc = LineCollection(
                    [[(left, bottom), (left, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)


def plot_steps(ax, steps):
    for s in steps:  # iterate through steps lists
        y, x, _ = s
        bottom = (9 - y) * 10
        left = x * 10
        patch = Rectangle((left + 4, bottom + 4), 2, 2)
        ax.add_collection(
            PatchCollection([patch], facecolor="blue")
        )  # every step that was taken,
        # and didn't require backtracking, show blue rectangular patch


def plot_maze(ax, file_name, maze, steps):
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_xlim(-5, 105)
    ax.set_ylim(-5, 105)
    base = os.path.basename(file_name)
    maze_name = os.path.splitext(base)[0]
    ax.set_title(f"{maze_name} ({len(steps)} steps)")

    # Plot enter and exit cells
    entrance = Rectangle((0, 90), 10, 10)
    ax.add_collection(PatchCollection([entrance], facecolor="tan"))
    exit = Rectangle((90, 0), 10, 10)
    ax.add_collection(PatchCollection([exit], facecolor="orange"))

    # Plot cell corner circles
    for x in range(0, 110, 10):
        for y in range(0, 110, 10):
            ax.scatter(x, y, color="black")

    plot_steps(ax, steps)  # function that plots steps

    plot_cell_walls(ax, maze)


def in_path(steps, y, x):  # goes through steps list in reverse order
    for s in reversed(steps):
        sy, sx, _ = s
        if sy == y and sx == x:
            return True  # if the step has been found, we have already been there
    return False


def search_maze(
    maze, steps
):  # keep calling this function in main() until return true (at the end)
    y, x, dir = steps.pop()  # every time we search, we remove our current position

    if x == 9 and y == 9:  # if you've reached the end of the maze, you're done
        steps.append((9, 9, 0))
        return True

    if dir == 0:  # try north for any cell we just arrived in
        steps.append((y, x, 1))
        if maze[y, x] & 1 != 1:  # if no wall, then move
            if not in_path(
                steps, y - 1, x
            ):  # check if we've gone north from that location before
                steps.append((y - 1, x, 0))
        return False  # we keep taking steps until true

    if dir == 1:  # if we tried going north and couldn't
        steps.append((y, x, 2))  # go east
        if maze[y, x] & 2 != 2:  # if no east wall
            if not in_path(steps, y, x + 1):  # if we haven't gone this way before
                steps.append((y, x + 1, 0))  # record this step
        return False  # we have to keep taking steps until true

    if dir == 2:  # if we have tried going north and east
        steps.append((y, x, 4))  # go south
        if maze[y, x] & 4 != 4:  # if no south wall
            if not in_path(steps, y + 1, x):
                steps.append((y + 1, x, 0))
        return False

    if dir == 4:  # if we tried going north, east, and south
        steps.append((y, x, 8))  # go west
        if maze[y, x] & 8 != 8:  # if no west wall
            if not in_path(steps, y, x - 1):
                steps.append((y, x - 1, 0))
        return False

    return False


def main(file_name):
    global total_steps  # keep track of the total steps, including backtracking, global function
    total_steps = 0
    with open(file_name + ".pickle", "rb") as file_in:  # load in the pickle file
        maze = pickle.load(file_in)  # define variable maze as a loaded pickle file

    # Steps is list of tuples, where each tuple contains the
    # (y, x, last direction tried) for each step along current path
    steps = [(0, 0, 0)]
    # This list of tuples grows as we progress through maze, backtracking will cause a removal of tuples

    while not search_maze(maze, steps):
        pass
    # pass is a non operation, pass allows you to comply with scope requirement

    fig = plt.figure(file_name)
    fig.set_size_inches(8, 8)  # print the maze
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])

    plot_maze(
        ax, file_name, maze, steps
    )  # draw the maze and the path taken, minus backtracking

    plt.show()  # show the maze and path


if __name__ == "__main__":
    file_name = None
    if len(sys.argv) == 1:
        file_name = os.path.dirname(sys.argv[0]) + "/maze.csv"
    else:
        file_name = sys.argv[1]

    main(file_name)
