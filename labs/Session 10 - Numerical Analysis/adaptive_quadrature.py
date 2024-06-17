#!/usr/bin/env python3
# adaptive_quadrature.py

import time


def f(x):
    # This is the function we are numerically integrating
    return 5 * pow(x, 3) - 9 * pow(x, 2) + 11


def F(x):
    # This is the exact analytic integral of our function
    return 5 * pow(x, 4) / 4 - 3 * pow(x, 3) + 11 * x


def midpoint_fixed(a, b):
    x = a
    dx = (b - a) / 1e6  # one million intervals of equal x lengths
    area = 0
    while x < b:
        area += f(x + dx / 2) * dx  # for midpoint of each interval, calculate area
        x += dx  # keep moving x along the interval
    return area


def midpoint_adaptive(a, b):
    x = a  # starting at lower bound
    dx = 1
    area = 0
    while x < b:  # while we're in the domain of interest
        f1 = f(x)  # our function at a given x
        f2 = f(x + dx)
        # Keep halving dx if current delta is too great
        while (
            abs((f2 - f1) / f1) > 1e-3
        ):  # "relative error" of f2 compared to f1, i.e. we don't
            # want f(x) to change too much in the subinterval we have
            dx /= 2  # iteratively halve dx
            f2 = f(x + dx)  # calculate new f2
        # Use the midpoint rule
        area += (
            f(x + dx / 2) * dx
        )  # if change is within error threshold, calculate lengths of
        # the "heights" at x
        x += dx  # walk along x in increments of dx
        # Expand current interval width
        dx *= 2  # increase dx, to improve runtime. If dx becomes too big in a certain x range,
        # it will go back into the while loop and shrink again
    return area


def main():
    a = 0  # bounds of the integral
    b = 10

    area_actual = F(b) - F(a)  # analytical solution to integral
    print(f"\nExact integral using analytic calculus = {area_actual}")
    print()

    start_time = (
        time.process_time()
    )  # how long did the midpoint rule take, fixed width?
    area_fixed = midpoint_fixed(a, b)
    elapsed_time = time.process_time() - start_time
    err = (area_fixed - area_actual) / area_actual * 100
    print(f"Estimated integral using fixed width midpoint rule = {area_fixed}")
    print(f"Fixed width midpoint rule error = {err:.8f}")
    print(f"Time (sec) Fixed = {elapsed_time:.3f}")
    print()

    start_time = time.process_time()  # time the adaptive midpoint method
    area_adaptive = midpoint_adaptive(a, b)
    elapsed_time = time.process_time() - start_time
    err = (area_adaptive - area_actual) / area_actual * 100
    print(f"Estimated integral using adaptive width midpoint rule = {area_adaptive}")
    print(f"Adaptive width midpoint rule error = {err:.8f}")
    print(f"Time (sec) Adaptive = {elapsed_time:.3f}")
    print()


if __name__ == "__main__":
    main()
