#!/usr/bin/env python3
# lattice_circle.py

import numpy as np
from numba import jit

# See https://en.wikipedia.org/wiki/Gauss_circle_problem


@jit(nopython=True)  # read this function in compiler code
def lattice_points(radius):
    num_points = 0
    radius_squared = radius**2  # square radius
    for x in range(-radius, radius + 1):  # possible x values, circle centered at origin
        for y in range(-radius, radius + 1):
            if x**2 + y**2 <= radius_squared:  # if point (x,y) inside circle
                num_points += 1  # add to counter
    return num_points


def main():
    for radius in range(1000, 10001, 1000):  # iterate through list from 1000 to 10000
        # increments of 1000
        act_points = lattice_points(
            radius
        )  # function gives us lattice points, taking in
        # radius input
        est_points = int(
            np.pi * radius**2 + 2 * np.sqrt(2 * np.pi * radius)
        )  # N(r) for
        # each radius in range(), estimate number of points
        print(
            f"Radius = {radius:>6,}"
            f"  Act Points = {act_points:>12,}"  # print actual result, right justified, with
            # commas
            f"  Est Points = {est_points:>12,}"
            f"  % Rel. Err = {(act_points - est_points)/est_points:0.4%}"  # print percentage
            # error with 4 digits after decimal
        )


# gauss' estimate improves with increasing radius, and E(r) converges to gauss' proposed
# value for large r
if __name__ == "__main__":
    main()
