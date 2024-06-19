#!/usr/bin/env python3
# dirichlet_function.py

import mpmath  # import module mpmath

mpmath.mp.dps = 2000  # dps = decimal places, 2000 of them


def dirichlet_function(x):  # evaluate dirichlet function at given x
    k = 100  # specified k and n
    n = 1e10
    f = mpmath.power(
        mpmath.cos(mpmath.factorial(k) * mpmath.pi * x), n
    )  # dirichlet function at
    # specified k and n
    return mpmath.chop(f)  # chops of small real or imaginary parts of f


def main():
    print(
        f"f(2) = {dirichlet_function(2)}"
    )  # systematically call function, evaluate at
    # desired values
    print(f"f(2.5) = {dirichlet_function(2.5)}")
    print(f"f(sqrt(2)) = {dirichlet_function(mpmath.sqrt(2))}")
    print(f"f(e) = {dirichlet_function(mpmath.e)}")


if __name__ == "__main__":
    main()
