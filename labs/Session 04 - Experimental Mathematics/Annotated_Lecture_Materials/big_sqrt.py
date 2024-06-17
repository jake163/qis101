#!/usr/bin/env python3
# big_sqrt.py

# From http://mpmath.org
from mpmath import mp, mpf, nstr  # from module import functions


def square_root(x):
    lowEnd = mpf(0)  # real float (decimal number) of 0
    highEnd = mpf(x)

    estimate = mpf(highEnd + lowEnd / 2)
    estimateSquared = mpf(estimate * estimate)

    epsilon = mpf(1e-14)

    while abs(estimateSquared - x) > epsilon:  # implements Newton method provided
        # we are still above the error limit
        if estimateSquared > x:
            highEnd = estimate  # estimate becomes new high end
        else:
            lowEnd = estimate  # estimate becomes new low end

        estimate = (highEnd + lowEnd) / 2  # makes new estimate
        estimateSquared = estimate * estimate  # makes new estimate squared

        if highEnd == lowEnd:
            break

    return estimate


def main():
    mp.dps = 200  # dps = decimal places, our function decimal outputs will have a
    # precision of 200 dps

    x = 33590351381261822622218163873528556813698947665687615688767589021060440979380129292322236643684251591

    x_sqrt = square_root(x)

    print(f"Estimated square root of \n {x}")
    print(f"is \n {nstr(x_sqrt, 100)}")  # \n tells it to not print what is there
    # literally, converts x_sqrt from mpf to string to 100 decimal points


if __name__ == "__main__":
    main()
