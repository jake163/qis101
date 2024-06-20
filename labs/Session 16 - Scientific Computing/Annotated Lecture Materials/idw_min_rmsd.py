#!/usr/bin/env python3
# idw_min_rmsd.py

import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import sys
import os


def act_height(x, y):
    # Calculate the height of the "actual" ocean at (x,y)
    return (
        30 * np.sin(y / 40) * np.cos(x / 40) + 50 * np.sin(np.sqrt(x * x + y * y) / 40)
    ) - 800


def init_samples():
    np.random.seed(2016)

    global ocean_size, num_intervals, num_samples
    ocean_size, num_intervals, num_samples = 390, 65, 220

    global grid_x, grid_y, grid_z
    grid_x, grid_y = np.mgrid[
        0 : ocean_size : complex(0, num_intervals),
        0 : ocean_size : complex(0, num_intervals),
    ]
    grid_z = act_height(grid_x, grid_y)

    global samples_x, samples_y, samples_z
    samples_x = np.random.uniform(0, ocean_size, num_samples)
    samples_y = np.random.uniform(0, ocean_size, num_samples)
    samples_z = act_height(samples_x, samples_y)


@jit(nopython=True)
def calc_idw_height(xi, yi, p):
    sum_weight = 0.0
    sum_height_weight = 0.0
    for si in range(num_samples):
        distance = np.hypot(
            grid_x[xi, xi] - samples_x[si], grid_y[yi, yi] - samples_y[si]
        )
        if distance == 0:
            return samples_z[si]
        weight = 1 / np.power(distance, p)
        sum_weight += weight
        sum_height_weight += samples_z[si] * weight
    return sum_height_weight / sum_weight


def est_height(p):
    global est_z
    est_z = np.zeros_like(grid_x)
    for xi in range(num_intervals):
        for yi in range(num_intervals):
            est_z[xi, yi] = calc_idw_height(xi, yi, p)
    return est_z


def calc_rmsd(p):
    sum_errors = 0.0
    for xi in range(num_intervals):
        for yi in range(
            num_intervals
        ):  # iterate through x in num intervals, for each x iterate through y
            act = grid_z[xi, yi]
            est = calc_idw_height(xi, yi, p)
            sum_errors += (
                act - est
            ) ** 2  # calculate distance squared between actual and estimate
    rmsd = np.sqrt(sum_errors / num_samples**2)  # calculate rmsd
    return rmsd


def plot(ax):  # plot
    p = np.linspace(1.0, 9.0, 50)  # raise the power term from 1 to 9 in steps of 50
    calc_rmsd_vec = np.vectorize(calc_rmsd)  # calculate rmsd
    rmsd = calc_rmsd_vec(p)  # pass p into calc_rmsd_vec

    min_rmsd = np.amin(rmsd)  # minimizes the rmsd
    best_p = p[np.argmin(rmsd)]  # the best p value is the one that minimizes the error

    ax.plot(p, rmsd)  # makes a plot with rmsd vs p
    ax.scatter(best_p, min_rmsd, color="red")  # plot the best p

    ax.set_title("Inverse Distance Weighting (p vs RMSD)")
    ax.set_xlabel("p (Power) term")
    ax.set_ylabel("RMSD (Act vs. Est)")

    ax.text(5.0, 3.0, f"best p = {best_p:.4f}", ha="left")  # shows message


def main():

    init_samples()

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
