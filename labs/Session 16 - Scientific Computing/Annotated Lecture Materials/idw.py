#!/usr/bin/env python3
# idw.py

import numpy as np
import mayavi.mlab as mlab  # mayavi.mlab is for visualization
from numba import jit


def act_height(x, y):  # generate 220 random heigh points
    # Calculate the height of the "actual" ocean at (x,y)
    return (
        30 * np.sin(y / 40) * np.cos(x / 40) + 50 * np.sin(np.sqrt(x * x + y * y) / 40)
    ) - 800  # function that represents our "actual" ocean floor depth


def init_samples():
    np.random.seed(2016)

    global ocean_size, num_intervals, num_samples
    ocean_size, num_intervals, num_samples = (
        390,
        65,
        220,
    )  # 220 random dots, 65 intervals per side, 390 units
    # to a side

    global grid_x, grid_y, grid_z  # mesh grid, x and y meet at 90 degrees
    grid_x, grid_y = np.mgrid[
        0 : ocean_size : complex(0, num_intervals),
        0 : ocean_size : complex(0, num_intervals),
    ]
    grid_z = act_height(
        grid_x, grid_y
    )  # for each grid_x and grid_y, we get a grid height

    global samples_x, samples_y, samples_z
    samples_x = np.random.uniform(0, ocean_size, num_samples)
    samples_y = np.random.uniform(0, ocean_size, num_samples)
    samples_z = act_height(samples_x, samples_y)


@jit(nopython=True)  # just in time compiler, for quickness
def calc_idw_height(xi, yi, p):
    sum_weight = 0.0
    sum_height_weight = 0.0
    for si in range(num_samples):
        distance = np.hypot(
            grid_x[xi, xi] - samples_x[si], grid_y[yi, yi] - samples_y[si]
        )
        if distance == 0:
            return samples_z[si]
        weight = 1 / np.power(distance, p)  # calculate weights
        sum_weight += weight
        sum_height_weight += samples_z[si] * weight
    return sum_height_weight / sum_weight


def est_height(p):  # helper function
    global est_z
    est_z = np.zeros_like(grid_x)  # make a grid of zeros with the dimensions of grid_x
    for xi in range(num_intervals):  # for x in the number of intervals range
        for yi in range(num_intervals):  # for y in the number of intervals range
            est_z[xi, yi] = calc_idw_height(xi, yi, p)  # use idw to calculate height
    return est_z


def plot(idw_plot_type):

    if idw_plot_type == 1:  # make plot with actual z
        mlab.surf(grid_x, grid_y, grid_z, colormap="ocean")

    if idw_plot_type == 2:  # make plot with IDW z
        mlab.surf(grid_x, grid_y, est_z, colormap="ocean")

    if idw_plot_type == 3:  # make plot with actual z, wireframe type
        mlab.surf(grid_x, grid_y, grid_z, colormap="Blues", representation="wireframe")

        mlab.surf(grid_x, grid_y, est_z, colormap="Reds", representation="wireframe")

    if (
        idw_plot_type == 1 or idw_plot_type == 2
    ):  # make plot and show random samples picked
        mlab.points3d(samples_x, samples_y, samples_z, scale_factor=3, color=(1, 0, 0))

    mlab.show()


def main():
    init_samples()
    # TODO: Adjust the p (power) value in the following line
    est_height(p=9)
    # TODO: Change the plot type (1,2,3) in the following line
    plot(idw_plot_type=2)


if __name__ == "__main__":
    main()
