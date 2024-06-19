#!/usr/bin/env python3
# quadratic_regression_sklearn.py


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import sys
import os


def fit_linear(vec_x, vec_y):  # linear fit function, pass in vec_x and vec_y
    vec_x = vec_x.reshape(-1, 1)  # x array is reshaped to column vector
    model = LinearRegression().fit(vec_x, vec_y)  # pass in indep and dep,
    # output is a tuple
    m = model.coef_  # unpack tuple element
    b = model.intercept_
    return m, b  # return tuple (slope, intercept)


def fit_quadratic(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    # degree two is the degree of our polynomial fit function, multiply
    # x values so they are close in range to y, then later
    # undoes that, so we can minimize roundoff error
    transformer.fit(vec_x)  # fit polynomial to data
    vec_x_ = transformer.transform(vec_x)  # redefine vec_x
    model = LinearRegression().fit(vec_x_, vec_y)  # apply the linear regr
    b, a = model.coef_  # tuple of coefficients
    c = model.intercept_  # intercept
    return a, b, c  # return tuple of parameters


def f(a, b, c, x):
    return a * x**2 + b * x + c


def plot(ax):
    vec_x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    vec_y = np.array([205, 430, 677, 945, 1233, 1542, 1872, 2224])

    x = np.linspace(np.min(vec_x), np.max(vec_x), 1000)

    a, b, c = fit_quadratic(vec_x, vec_y)
    ax.plot(x, a * x**2 + b * x + c, label="Quadratic")

    print(f"y = ({a:.4f})x^2 + ({b:.4f})x + ({c:.4})")
    print(f"Tape counter at 65 mins = {f(a,b,c,6.5):,.4f}")

    m, b = fit_linear(vec_x, vec_y)
    ax.plot(x, m * x + b, label="Linear")

    ax.scatter(vec_x, vec_y, color="red")

    ax.set_title("Tape Counter Per Minute")
    ax.set_xlabel("Elapsed time x10 (min)")
    ax.set_ylabel("Tape Counter")
    ax.legend()


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
