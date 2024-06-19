#!/usr/bin/env python3
# plot_polynomial.py

import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Poly, real_roots, Derivative, lambdify, latex  # from module

# import all those functions, tells users what functions you're using from sympy
import sys
import os


def plot(ax):
    # Declare x to be a sympy symbol, not just a python variable
    x = symbols("x")

    # Declare the polynomial "fn" by providing the coefficients
    # of each term in in decreasing (exponent) order
    fn = Poly([1, -2, -120, 22, 2119, 1980], x)

    # Find the real-only roots of the polynomial
    # and store in a numpy array of floats
    fn_zeros = np.asarray([float(r) for r in real_roots(fn)])

    # Find the symbolic first derivative of "fn" and locate the real-only
    # zeros of this derivative to find the extrema (tangent) points
    fn_d1 = Derivative(fn, x, evaluate=True)
    fn_d1_zeros = np.asarray([float(r) for r in real_roots(fn_d1)])

    # Combine the zeros of "fn" and the zeros of the derivative of "fn" into a
    # a single numpy array, then sort that array in increasing order. This array
    # now contains the x-coordinate of interesting points in the "fn" polynomial
    x_pts = np.sort(np.concatenate((fn_zeros, fn_d1_zeros)))

    # Get the minimum and maximum of the interesting points array
    x_min, x_max = (
        x_pts[0] - 1,
        x_pts[-1] + 1,
    )  # -1 index value takes you to the end of a
    # list (last element).
    print(f"x_min = {x_min:.4f}, x_max = {x_max:.4f}")

    xa = np.linspace(x_min, x_max, 1000)  # x domain as array, 1000 subdomains

    # Label the graph and draw (0,0) axis lines
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color="gray")
    ax.axvline(0, color="gray")

    # Create a numpy callable (numeric) function from the symbolic "fn" polynomial
    fn_lambda = lambdify(
        x, fn.as_expr(), modules="numpy"
    )  # turn symbolic sympy function
    # into numeric callable numpy function

    ax.plot(xa, fn_lambda(xa), linewidth=2)  # pass in x array, load up x values,
    # get back x array

    # Plot the zeros and derivative roots on the line graph
    ax.scatter(fn_zeros, fn_lambda(fn_zeros), color="red")
    # scatter plot doesn't connect points, make zeros red
    ax.scatter(
        fn_d1_zeros, fn_lambda(fn_d1_zeros), color="green"
    )  # make critical points
    # green

    # Set the graph title to the polynomial expressed in LaTeX format
    ax.set_title(f"$y = {latex(fn.as_expr())}$")


def main():  # function executable in the command line
    fig = plt.figure(
        os.path.basename(sys.argv[0])
    )  ##basename(path) returns tail of path
    # in python
    gs = fig.add_gridspec(1, 1)  # we are making 1 graph

    ax = fig.add_subplot(gs[0, 0])  # it is the first/only subplot
    plot(ax)  # pass in ax, adds axes

    plt.show()  # shows the complete plot


if __name__ == "__main__":  # when re run standalone (not imported), main() is executed
    main()
