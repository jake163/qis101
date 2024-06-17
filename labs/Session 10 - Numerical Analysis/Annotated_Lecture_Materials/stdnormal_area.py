#!/usr/bin/env python3
# stdnormal_area.py

import numpy as np
import scipy.integrate  # import scipy integrate module


def f(x):  # this is our function of interest
    return 1 / np.sqrt(2 * np.pi) * np.exp(-(x**2) / 2)


def main():
    integral = scipy.integrate.quad(f, -1, 1)[
        0
    ]  # we are integrating f from -1 to 1 up to
    # first standard deviation

    # See https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
    print(f"Normal CDF with 1st sigma = {integral}")  # prints evaluated integral, float


if __name__ == "__main__":
    main()
